from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
   
    url(r'^$',views.index,name='index'),
    url(r'^mcq$',views.mcq,name='mcq'),
    url(r'^test$',views.test,name='test'),
    url(r'^rand$',views.randcheck,name='randcheck'),
    url(r'^submit_test$',views.score,name='score'),

    url(r'^get/$',views.get,name='get'),
	url(r'^sub/$',views.sub,name='sub'),
	url(r'^finish/$',views.finish,name='finish'),
	
	url(r'save_source/$',views.save_source,name="save_source"),
    
]