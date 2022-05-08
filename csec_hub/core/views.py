from ast import Sub
import re
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import redirect, render
from .forms import SearchForm, VotingForm, SubscriptionForm
from .models import ScoreBoard, Feed, Event, Voting
from .filters import ScoreBoardFilter


class ScoreBoardView(ListView):
    def __init__(self):
        self.model = ScoreBoard
        self.template_name = 'core/score_board/list.html'
        self.context_object_name = 'score_board'
        self.queryset = self.model.objects.filter(is_active=True)
        self.paginate_by = 10
        self.paginate_orphans = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ScoreBoardFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ScoreBoardDetailView(DetailView):
    def __init__(self):
        self.model = ScoreBoard
        self.template_name = 'core/score_board/detail.html'
        self.context_object_name = 'score_board'


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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_clas
        context['queryset'] = self.get_queryset()
        return context
        
class FeedDetailView(DetailView):
    def __init__(self):
        self.model = Feed
        self.template_name = 'core/feed/detail.html'
        self.context_object_name = 'feed'

    def post(self, request, *args, **kwargs):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            current_user = request.user
            form.user = current_user
            if current_user not in form.feed.subscribers.all():
                if form.user.telegram_username != form.cleaned_data['tg_user_name']:
                    form.user.telegram_username = form.cleaned_data['tg_user_name']
                form.feed = self.get_object()
                form.feed.subscribers.add(current_user)
                form.save()
                return redirect('core:feed_detail', pk=form.feed.feed_type.pk)
            else:
                return redirect('core:feed_detail', pk=form.feed.feed_type.pk)
        
        return render(request, 'core/feed/detail.html', {'form': form})

                
        

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
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        context['queryset'] = self.get_queryset()
        return context
    


class EventDetailView(DetailView):
    def __init__(self):
        self.model = Event
        self.template_name = 'core/event/detail.html'
        self.context_object_name = 'event'
    def post(self, request, *args, **kwargs):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:event_detail', pk=self.kwargs['pk'])
        return render(request, self.template_name, {'form': form})

            

class VotingView(ListView):
    def __init__(self):
        self.model = Voting
        self.template_name = 'core/vote/vote.html'
        self.context_object_name = 'vote'
        self.queryset = self.model.objects.filter(is_active=True)
        self.paginate_by = 10
        self.paginate_orphans = 1
    
class VotingDetailView(DetailView):
    def __init__(self):
        self.model = Voting
        self.template_name = 'core/vote/detail.html'
        self.context_object_name = 'vote'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = VotingForm()            
        return context
    
    def post(self, request, *args, **kwargs):
        form = VotingForm(request.POST)
        voters = Voting.objects.filter(is_active=True, voted_by__id=kwargs['pk'])
        if form.is_valid():
            vote = form.save(commit=False)
            vote.candidate = self.get_object()
            if request.user.is_authenticated and request.user not in voters:
                vote.voted_by = request.user
                vote.save()
                return render(request, 'core/vote/detail.html', {'vote': vote})
            else:
                return render(request, 'core/vote/detail.html', {'vote': vote, 'form': form, 'error': 'You have already voted'})
        else:
            return render(request, 'core/vote/detail.html', {'vote': vote, 'form': form, 'error': 'Please fill the form correctly'})

    