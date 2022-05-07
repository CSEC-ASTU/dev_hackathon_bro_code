from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import render
from .forms import SearchForm
from .models import CpdScoreBoard, DevScoreBoard, Feed, Event, Voting


class CpdScoreBoardView(ListView):
    def __init__(self):
        self.model = CpdScoreBoard
        self.template_name = 'core/cpd_score_board/list.html'
        self.context_object_name = 'cpd_score_board'
        self.form_class = SearchForm
        self.queryset = self.model.objects.filter(is_active=True)
        self.paginate_by = 10
        self.paginate_orphans = 1
    
    def get_queryset(self):
        queryset = self.model.objects.filter(is_active=True)
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(title__icontains=query, is_active=True)
        return queryset
        

class CpdScoreBoardDetailView(DetailView):
    def __init__(self):
        self.model = CpdScoreBoard
        self.template_name = 'core/cpd_score_board/detail.html'
        self.context_object_name = 'cpd_score_board'



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


class FeedView(ListView):
    def __init__(self):
        self.model = Feed
        self.template_name = 'core/feed/feed.html'
        self.context_object_name = 'feed'
        self.form_class = SearchForm
        self.queryset = self.model.objects.filter(is_active=True)
        self.paginate_by = 10
        self.paginate_orphans = 1

    def get_queryset(self):
        queryset = self.model.objects.filter(is_active=True)
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(title__icontains=query, is_active=True)
        return queryset

class FeedDetailView(DetailView):
    def __init__(self):
        self.model = Feed
        self.template_name = 'core/feed/detail.html'
        self.context_object_name = 'feed'
        

class EventView(ListView):
    def __init__(self):
        self.model = Event
        self.template_name = 'core/event/event.html'
        self.context_object_name = 'event'
        self.form_class = SearchForm
        self.queryset = self.model.objects.filter(is_active=True)
        self.paginate_by = 10
        self.paginate_orphans = 1
    
    def get_queryset(self):
        queryset = self.model.objects.filter(is_active=True)
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(title__icontains=query, is_active=True)
        return queryset

class EventDetailView(DetailView):
    def __init__(self):
        self.model = Event
        self.template_name = 'core/event/detail.html'
        self.context_object_name = 'event'


class VoteView(ListView):
    def __init__(self):
        self.model = Voting
        self.template_name = 'core/vote/vote.html'
        self.context_object_name = 'vote'
        self.form_class = VoteForm
        self.queryset = self.model.objects.filter(is_active=True)
        self.paginate_by = 10
        self.paginate_orphans = 1
    
  
    def post(self, request, *args, **kwargs):
        candidate_id = request.POST.get('candidate_id')
        action = request.POST.get('action')
        if action == 'vote':
            candidate = queryset.get(candidate=candidate_id)
            candidate.votes += 1
            candidate.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        elif action == 'unvote':
            candidate = queryset.get(id=candidate_id)
            candidate.votes -= 1
            candidate.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        

    

    
        
        
