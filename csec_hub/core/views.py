from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import render

from .models import CpdScoreBoard, DevScoreBoard, Feed, Event


class CpdScoreBoardView(ListView):
    def __init__(self):
        self.model = CpdScoreBoard
        self.template_name = 'core/cpd_score_board/list.html'
        self.context_object_name = 'cpd_score_board'
        self.queryset = self.model.objects.filter(is_active=True)
        self.paginate_by = 10
        self.paginate_orphans = 5

class CpdScoreBoardDetailView(DetailView):
    def __init__(self):
        self.model = CpdScoreBoard
        self.template_name = 'core/cpd_score_board/detail.html'
        self.context_object_name = 'cpd_score_board'
        self.queryset = self.model.objects.filter(is_active=True)


class DevScoreBoardView(ListView):
    def __init__(self):
        self.model = DevScoreBoard
        self.template_name = 'core/dev_score_board/list.html'
        self.context_object_name = 'dev_score_board'
        self.queryset = self.model.objects.filter(is_active=True)
        self.paginate_by = 10
        self.paginate_orphans = 5

class DevScoreBoardDetailView(DetailView):
    def __init__(self):
        self.model = DevScoreBoard
        self.template_name = 'core/dev_score_board/detail.html'
        self.context_object_name = 'dev_score_board'
        self.queryset = self.model.objects.filter(is_active=True)

class FeedView(ListView):
    def __init__(self):
        self.model = Feed
        self.template_name = 'core/feed/feed.html'
        self.context_object_name = 'feed'
        self.queryset = self.model.objects.filter(is_active=True)
        self.paginate_by = 10
        self.paginate_orphans = 5

class FeedDetailView(DetailView):
    def __init__(self):
        self.model = Feed
        self.template_name = 'core/feed/detail.html'
        self.context_object_name = 'feed'
        self.queryset = self.model.objects.filter(is_active=True)

class EventView(ListView):
    def __init__(self):
        self.model = Event
        self.template_name = 'core/event/event.html'
        self.context_object_name = 'event'
        self.queryset = self.model.objects.filter(is_active=True)
        self.paginate_by = 10
        self.paginate_orphans = 5

class EventDetailView(DetailView):
    def __init__(self):
        self.model = Event
        self.template_name = 'core/event/detail.html'
        self.context_object_name = 'event'
        self.queryset = self.model.objects.filter(is_active=True)
        

        
        
