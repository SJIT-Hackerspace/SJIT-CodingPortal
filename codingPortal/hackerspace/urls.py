from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^hackerspace/$',views.index,name='hackerspace'),
	url(r'^dataupload/$',views.dataupload,name = 'dataupload'),
	url(r'^staff/$',views.staff,name = 'staff'),
	url(r'^login/$',views.login,name = 'login'),
	url(r'^register/$',views.register,name = 'register'),
	url(r'^validate/$',views.validate,name = 'validate'),

]
