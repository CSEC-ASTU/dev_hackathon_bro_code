from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
   
    path('feed/', views.FeedView.as_view(), name='feeds'),
    path('feed/<int:pk>/', views.FeedDetailView.as_view(), name='feed_detail'),
    path('event/', views.EventView.as_view(), name='events'),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('score_board/', views.ScoreBoardView.as_view(), name='score_board'),
    path('score_board/<int:pk>/', views.ScoreBoardDetailView.as_view(), name='score_board_detail'),



    path('',views.hompage,name = 'indexpage'),
  
  
    path('about',views.about,name = 'about'),

    path('contact',views.contact,name = 'contact'),
    path('faq',views.faq,name = 'faq'),

    # path('register',views.register,name = 'register'),
    # path('signin',views.signin,name = 'signin'),
    path('hall-of-fame',views.hallOfFame,name = 'hall-of-fame'),
    path('fame-detail',views.fameDetail,name = 'fame-detail'),
]

