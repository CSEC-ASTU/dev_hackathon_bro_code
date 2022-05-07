from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import CpdScorBoard,DevScoreBoard,Feed, FeedType

class FeedAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ('title', 'type', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_filter = ('type', 'posted_by','tags', 'is_active')
    search_fields = ('title', 'body', 'tags')

admin.site.register(Feed, FeedAdmin)

@admin.register(CpdScorBoard)
class CpdScorBoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_filter = ('posted_by', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title', 'posted_by__username', 'created_at', 'updated_at', 'is_active')
    list_per_page = 10
    ordering = ('-created_at',)
    list_display_links = ('title',)
    list_editable = ('is_active',)
    list_select_related = ('posted_by',)
@admin.register(DevScoreBoard)
class DevScoreBoardAdmin(admin.ModelAdmin):
    # field set
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'posted_by', 'created_at', 'updated_at', 'is_active')
        }),
        ('Content', {
            'fields': ('body',)
        }),
        ('Tags', {
            'fields': ('tags',)
        }),
    )
    
    list_display = ('title', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_filter = ('posted_by', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title', 'posted_by__username', 'created_at', 'updated_at', 'is_active')
    list_per_page = 10
    ordering = ('-created_at',)
    list_display_links = ('title',)

@admin.register(FeedType)
class FeedTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at', 'is_active')
    list_filter = ('name', 'description', 'created_at', 'updated_at', 'is_active')
    search_fields = ('name', 'description', 'created_at', 'updated_at', 'is_active')
    list_per_page = 10
    ordering = ('-created_at',)
    list_display_links = ('name',)
    list_editable = ('is_active',)
