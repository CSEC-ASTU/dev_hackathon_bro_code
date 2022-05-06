from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import CpdScorBoard,DevScoreBoard,Feed

class FeedAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)

admin.site.register(Feed, FeedAdmin)
