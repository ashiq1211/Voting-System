from django.urls import path
from django.urls import path
from . import views
urlpatterns=[
    path('',views.vote,name='vote'),
    path('poll',views.poll,name='poll'),
    path('ended',views.ended,name='ended'),
     
]