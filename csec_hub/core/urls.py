from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('',views.hompage,name = 'indexpage'),
  
  
    path('about',views.about,name = 'about'),

    path('contact',views.contact,name = 'contact'),
    path('faq',views.faq,name = 'faq'),

    path('register',views.register,name = 'register'),
    path('signin',views.signin,name = 'signin'),
    path('hall-of-fame',views.hallOfFame,name = 'hall-of-fame'),
    path('fame-detail',views.fameDetail,name = 'fame-detail'),
]

urlpatterns += [
   
    path('feeds/', views.FeedView.as_view(), name='feeds'),
    path('feed-detail/<int:pk>/', views.FeedDetailView.as_view(), name='feed-detail'),
    path('events/', views.EventView.as_view(), name='events'),
    path('event-detail/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('score_board/', views.ScoreBoardView.as_view(), name='score_board'),
    path('score_board/<int:pk>/', views.ScoreBoardDetailView.as_view(), name='score_board_detail'),
]