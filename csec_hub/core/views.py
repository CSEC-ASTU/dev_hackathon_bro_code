from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import render


from .models import ScoreBoard, Feed, Event


def hompage(request):
    return render(request,'index.html',context={})



def about(request):
    return render(request,'about.html',context={})

def contact(request):
    return render(request,'contact.html',context={})

def faq(request):
    return render(request,'faq.html',context={})


def hallOfFame(request):
    return render(request,'hall-of-fame.html',context={})


def fameDetail(request):
        return render(request,'fame-detail.html',context={})





def register(request):
    return render(request,'register.html',context={})

def signin(request):
        return render(request,'signin.html',context={})






class ScoreBoardView(ListView):
    def __init__(self):
        self.model = ScoreBoard
        self.template_name = 'scoreboard.html'
        self.context_object_name = 'score_board'
        self.queryset = self.model.objects.filter(is_active=True)
        self.paginate_by = 10
        self.paginate_orphans = 5



class ScoreBoardDetailView(DetailView):
    def __init__(self):
        self.model = ScoreBoard
        self.template_name = 'core/cpd_score_board/detail.html'
        self.context_object_name = 'cpd_score_board'
        self.queryset = self.model.objects.filter(is_active=True)

class FeedView(ListView):
    def __init__(self):
        self.model = Feed
        self.template_name = 'feeds.html'
        self.context_object_name = 'feed'
        self.queryset = self.model.objects.filter(is_active=True)
        self.paginate_by = 10
        self.paginate_orphans = 5

class FeedDetailView(DetailView):
    def __init__(self):
        self.model = Feed
        self.template_name = 'feedDetail.html'
        self.context_object_name = 'feed'
        self.queryset = self.model.objects.filter(is_active=True)

class EventView(ListView):
    def __init__(self):
        self.model = Event
        self.template_name = 'events.html'
        self.context_object_name = 'event'
        self.queryset = self.model.objects.filter(is_active=True)
        self.paginate_by = 10
        self.paginate_orphans = 5

class EventDetailView(DetailView):
    def __init__(self):
        self.model = Event
        self.template_name = 'eventDetail.html'
        self.context_object_name = 'event'
        self.queryset = self.model.objects.filter(is_active=True)
        

        
        

