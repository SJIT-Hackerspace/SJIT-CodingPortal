from django.conf.urls import url
from . import views


urlpatterns = [
	
	url(r'^csequiz/$',views.csequiz,name = 'csequiz'),
	url(r'^itquiz/$',views.itquiz,name = 'itquiz'),
	url(r'^eeequiz/$',views.eeequiz,name = 'eeequiz'),
	url(r'^ecequiz/$',views.ecequiz,name = 'ecequiz'),
	url(r'^mechquiz/$',views.mechquiz,name = 'mechquiz'),

]
