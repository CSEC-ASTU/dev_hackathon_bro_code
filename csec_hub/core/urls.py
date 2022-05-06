from django.urls import path
from . import views


urlpatterns = [
    path('',views.hompage,name = 'indexpage'),
    path('events',views.events,name = 'events'),
    path('feeds',views.feeds,name = 'feeds'),
    path('about',views.about,name = 'about'),

    path('contact',views.contact,name = 'contact'),
    path('faq',views.faq,name = 'faq'),

    path('event-detail',views.eventDetail,name = 'event-detail'),
    path('feed-detail',views.feedDetail,name = 'feed-detail'),

]