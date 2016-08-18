from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^hackerspace/$',views.index,name='hackerspace')
]
