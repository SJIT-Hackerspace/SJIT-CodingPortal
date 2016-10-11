from django.shortcuts import render
from django.template.response import TemplateResponse
from Questions.models import *
from TestAllocation.models import *
import datetime
# Create your views here.
def mcq(request):
	ob=QuizQuestion.objects.all().order_by('?')[:4]
	return TemplateResponse(request,"mcq.html",{'ob':ob})


def index(request):
	# ob = Quiz.objects.all().order_by('StartTime')

	timeobj = datetime.date.today().strftime("%b. %d, %Y %I:%M")
	ampm = datetime.date.today().strftime("%r")
	notation = ""
	if 'AM' in ampm:
		notation="a.m."
	else:
		notation="p.m."
	
	time = str(timeobj)+" "+notation

	t = datetime.date.today().strftime("%r")
	d = datetime.date.today()

	ob = Quiz.objects.all().filter(EndDate__lte=d,EndTime__gte=t)

	obj = Quiz.objects.all().order_by('StartTime')
	return render(request,"index.html",{'tests':ob,'time':time,'testsall':obj})