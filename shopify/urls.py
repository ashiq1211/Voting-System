from django.urls import path
from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('viewProduct',views.viewProduct,name='viewProduct'),
    # path('ended',views.ended,name='ended'),
     
]