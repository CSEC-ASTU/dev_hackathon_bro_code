from multiprocessing import Event
from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import ScoreBoard,Feed, FeedType, Event, Subscription

class FeedAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ('title', 'type', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_filter = ('type', 'posted_by','tags', 'is_active')
    search_fields = ('title', 'body', 'tags')

admin.site.register(Feed, FeedAdmin)
class ScoreBoardAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ('title', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_filter = ('posted_by', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title', 'posted_by__username', 'created_at', 'updated_at', 'is_active')
    list_per_page = 10
    ordering = ('-created_at',)
    list_display_links = ('title',)
    list_editable = ('is_active',)
    list_select_related = ('posted_by',)

admin.site.register(ScoreBoard, ScoreBoardAdmin)

@admin.register(FeedType)
class FeedTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at', 'is_active')
    list_filter = ('name', 'description', 'created_at', 'updated_at', 'is_active')
    search_fields = ('name', 'description', 'created_at', 'updated_at', 'is_active')
    list_per_page = 10
    ordering = ('-created_at',)
    list_display_links = ('name',)
    list_editable = ('is_active',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'feed', 'created_at', 'updated_at', 'is_active')
    list_filter = ('user', 'feed', 'created_at', 'updated_at', 'is_active')
    search_fields = ('user', 'feed', 'created_at', 'updated_at', 'is_active')
    list_per_page = 10
    ordering = ('-created_at',)
    list_display_links = ('user', 'feed')
    list_editable = ('is_active',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_by', 'created_at', 'updated_at', 'is_active', 'is_completed')
    list_filter = ('posted_by', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title', 'posted_by__username', 'created_at', 'updated_at', 'is_active', 'is_completed')
    list_editable = ('is_completed',)   
