from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'destination', 'rating', 'short_comment', 'created_at')
    list_filter = ('rating', 'destination', 'created_at')
    search_fields = ('user__username', 'anonymous_user', 'comment')
    ordering = ('-created_at',)

    def get_username(self, obj):
        return obj.user.username if obj.user else obj.anonymous_user or "Anonymous"
    get_username.short_description = "User"

    def short_comment(self, obj):
        return (obj.comment[:50] + '...') if len(obj.comment) > 50 else obj.comment
    short_comment.short_description = "Comment"
