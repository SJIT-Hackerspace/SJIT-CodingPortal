from django.shortcuts import render
from django.template.response import TemplateResponse
from Questions.models import *
from TestAllocation.models import *
import datetime
from django.http import HttpResponse

# Create your views here.
def mcq(request):
	ob=QuizQuestion.objects.all().order_by('?')[:4]
	return TemplateResponse(request,"mcq.html",{'ob':ob})


def index(request):
	# ob = Quiz.objects.all().order_by('StartTime')

	timeobj = datetime.datetime.now().strftime("%I:%M")
	ampm = datetime.datetime.today().strftime("%r")
	notation = ""
	if 'AM' in ampm:
		notation="a.m."
	else:
		notation="p.m."
	
	time = str(timeobj)+" "+notation

	t = datetime.datetime.today()
	d = datetime.date.today()

	ob = Quiz.objects.all().filter(StartDate__lte=d,StartTime__lt=t,EndDate__gte=d,EndTime__gt=t)

	obj = Quiz.objects.all().order_by('StartTime')
	return render(request,"blank.html",{'tests':ob,'time':time,'testsall':obj})


def test(request):
	# name = request.POST['testname']
	# timeobj = datetime.datetime.now().strftime("%I:%M")
	# ampm = datetime.datetime.today().strftime("%r")
	# notation = ""
	# if 'AM' in ampm:
	# 	notation="a.m."
	# else:
	# 	notation="p.m."
	
	# time = str(timeobj)+" "+notation

	# t = datetime.datetime.today()
	# d = datetime.date.today()
	# ob = Quiz.objects.all().filter(StartDate__lte=d,StartTime__lt=t,EndDate__gte=d,EndTime__gt=t)


	quiz_obj = Quiz.objects.all().order_by('StartTime')
	programming_obj = Programming.objects.all().order_by('StartTime')
	verbal_obj = Verbal.objects.all().order_by('StartTime')


	for testnames in quiz_obj :
		if testnames.TestName in request.POST:
			ob=QuizQuestion.objects.all().order_by('?')[:4]
			return TemplateResponse(request,"mcq.html",{'ob':ob})	

	
	for testnames in programming_obj :
		if testnames.TestName in request.POST:
			ob=ProgrammingQuestion.objects.all().order_by('?')[:4]
			return TemplateResponse(request,"ide.html",{'ob':ob})	


	for testnames in verbal_obj :
		if testnames.TestName in request.POST:
			ob=VerbalQuestion.objects.all().order_by('?')[:4]
			return TemplateResponse(request,"mcq.html",{'ob':ob})								


	return HttpResponse("")	


def randcheck(request):
	return render(request,'blank.html')	


def score(request):
	quiz_obj = QuizQuestion.objects.all()
	programming_obj = ProgrammingQuestion.objects.all()
	verbal_obj = VerbalQuestion.objects.all()

	score = 0
	for questions in quiz_obj:

		if questions.question in request.POST:
			if questions.Answer in request.POST:
				score += 1


	for questions in programming_obj:
		if questions.question in request.POST:
			print(request.POST.get(str(questions.question+'radio')))


	for questions in verbal_obj:
		if questions.question in request.POST:
			print(request.POST.get(str(questions.question+'radio')))							



	return TemplateResponse(request,'score.html',{'score':score})			