from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
   
    path('feed/', views.FeedView.as_view(), name='feed'),
    path('feed/<int:pk>/', views.FeedDetailView.as_view(), name='feed_detail'),
    path('event/', views.EventView.as_view(), name='event'),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('cpd_score_board/', views.ScoreBoardView.as_view(), name='cpd_score_board'),
    path('cpd_score_board/<int:pk>/', views.ScoreBoardDetailView.as_view(), name='cpd_score_board_detail'),
    path('voting/', views.VotingView.as_view(), name='voting'),
    path('voting/<int:pk>/', views.VotingDetailView.as_view(), name='voting_detail'),
        
    
]