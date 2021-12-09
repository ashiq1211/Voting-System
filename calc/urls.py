from django.urls import path
from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('dest',views.dest,name='dest'),
     path('register',views.register,name='register'),
     path('login',views.login,name='login'),
     path('logout',views.logout,name='logout')
]