from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
   
    url(r'^student$',views.index,name='index'),
    url(r'^mcq$',views.mcq,name='mcq'),
    
]