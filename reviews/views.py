from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import JsonResponse
from .models import Review
from .forms import ReviewForm
from destinations.models import Destination
from django.views.decorators.csrf import csrf_exempt


def index(request):
    reviews_list = Review.objects.all().order_by('-created_at')
    destination_id = request.GET.get("destination")
    rating = request.GET.get("rating")

    if destination_id:
        reviews_list = reviews_list.filter(destination_id=destination_id)
    if rating:
        reviews_list = reviews_list.filter(rating=rating)

    paginator = Paginator(reviews_list, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    destinations = Destination.objects.all()

    return render(request, "reviews/index.html", {
        "reviews": page_obj,
        "destinations": destinations,
    })


def review_list(request):
    destinations = Destination.objects.all()
    reviews = Review.objects.all()
    context = {
        "destinations": destinations,
        "reviews": reviews,
    }
    return render(request, "reviews/review_list.html", context)


def add_review(request):
    destinations = Destination.objects.all()
    ratings = range(1, 6)

    if request.method == "POST":
        destination_id = request.POST.get("destination")
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        is_anonymous = request.POST.get("anonymous") == "on" or not request.user.is_authenticated

        try:
            destination = Destination.objects.get(id=destination_id)
            user = request.user if request.user.is_authenticated and not is_anonymous else None
            anonymous_user = "Guest" if is_anonymous else None

            review = Review.objects.create(
                user=user,
                anonymous_user=anonymous_user,
                destination=destination,
                rating=int(rating),
                comment=comment
            )

            if anonymous_user == "Guest":
                anonymous_reviews = request.session.get('anonymous_reviews', [])
                if review.id not in anonymous_reviews:
                    anonymous_reviews.append(review.id)
                    request.session['anonymous_reviews'] = anonymous_reviews
                    request.session.modified = True

            messages.success(request, "Review added successfully!")
            return redirect("reviews:reviews")

        except Destination.DoesNotExist:
            messages.error(request, "Invalid destination selected.")

    return render(request, "reviews/add_review.html", {
        "destinations": destinations,
        "ratings": ratings
    })


def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    # Case 1: Logged-in user deleting their own review
    if review.user == request.user:
        review.delete()
        messages.success(request, "Review deleted successfully!")

    # Case 2: Anonymous review being deleted by the session owner
    elif review.user is None and review.anonymous_user == "Guest":
        anonymous_reviews = request.session.get('anonymous_reviews', [])
        if review.id in anonymous_reviews:
            anonymous_reviews.remove(review.id)
            request.session['anonymous_reviews'] = anonymous_reviews
            request.session.modified = True

            review.delete()
            messages.success(request, "Your anonymous review was deleted.")

        # Case 3: Admin deleting any anonymous review
        elif request.user.is_authenticated and request.user.is_superuser:
            review.delete()
            messages.success(request, "Anonymous review deleted by admin.")

        else:
            messages.error(request, "You are not authorized to delete this anonymous review.")

    # Case 4: Not authorized
    else:
        messages.error(request, "You are not authorized to delete this review.")

    return redirect("reviews:reviews")


def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    # Case 1: Logged-in user editing their own review
    if review.user:
        if review.user != request.user:
            messages.error(request, "You are not allowed to edit this review.")
            return redirect('reviews:reviews')

    # Case 2: Anonymous review edited by the session owner
    elif review.user is None and review.anonymous_user == "Guest":
        anonymous_reviews = request.session.get('anonymous_reviews', [])

        if review.id not in anonymous_reviews:
            # Case 3: Admin editing anonymous review
            if request.user.is_authenticated and request.user.is_superuser:
                pass  # Allow admin to proceed
            else:
                messages.error(request, "You are not allowed to edit this anonymous review.")
                return redirect('reviews:reviews')

    # Case 4: No valid permissions
    else:
        messages.error(request, "You are not allowed to edit this review.")
        return redirect('reviews:reviews')

    # Render form for POST or GET
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Your review has been updated!")
            return redirect('reviews:reviews')
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/edit_review.html', {'form': form, 'review': review})




@csrf_exempt
def like_review(request, review_id):
    if request.method == "POST":
        review = get_object_or_404(Review, id=review_id)
        liked_reviews = request.session.get('liked_reviews', [])

        if review.id in liked_reviews:
            return JsonResponse({'success': False, 'message': 'Already liked.', 'likes': review.likes})

        review.likes += 1
        review.save()

        liked_reviews.append(review.id)
        request.session['liked_reviews'] = liked_reviews
        request.session.modified = True

        return JsonResponse({'success': True, 'likes': review.likes})

    return JsonResponse({'success': False, 'message': 'Invalid request.'})

