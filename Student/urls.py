from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
   
    url(r'^$',views.index,name='index'),
    url(r'^mcq$',views.mcq,name='mcq'),
    url(r'^test$',views.test,name='test'),
    url(r'^rand$',views.randcheck,name='randcheck'),
    url(r'^submit_test$',views.score,name='score'),
    
]