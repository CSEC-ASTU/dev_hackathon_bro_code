from multiprocessing import Event
from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import ScoreBoard,Feed, FeedType, Event

class FeedAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ('title', 'type', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_filter = ('type', 'posted_by','tags', 'is_active')
    search_fields = ('title', 'body', 'tags')

admin.site.register(Feed, FeedAdmin)

@admin.register(ScoreBoard)
class ScoreBoardAdmin(SummernoteModelAdmin):


    fieldsets = (
        ('Score Board', {
            'fields': ('title', 'scoreboard_date','body', 'posted_by', 'is_active','tags')
        }),
        ('Meta Data', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    summernote_fields = ('body',)
    readonly_fields = ['created_at','updated_at',]
    list_display = ('title', 'posted_by','body', 'created_at', 'updated_at', 'is_active','scoreboard_date' )
    
    list_filter = ('posted_by', 'created_at', 'updated_at', 'is_active','scoreboard_date')
    search_fields = ('title', 'posted_by__username', 'created_at', 'updated_at', 'is_active')
    list_per_page = 10
    ordering = ('-created_at',)
    list_display_links = ('title',)
    list_editable = ('is_active',)
    list_select_related = ('posted_by',)

@admin.register(FeedType)
class FeedTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at', 'is_active')
    list_filter = ('name', 'description', 'created_at', 'updated_at', 'is_active')
    search_fields = ('name', 'description', 'created_at', 'updated_at', 'is_active')
    list_per_page = 10
    ordering = ('-created_at',)
    list_display_links = ('name',)
    list_editable = ('is_active',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_by', 'created_at', 'updated_at', 'is_active', 'is_completed')
    list_filter = ('posted_by', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title', 'posted_by__username', 'created_at', 'updated_at', 'is_active', 'is_completed')
    list_editable = ('is_completed',)   
