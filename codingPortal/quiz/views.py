from django.shortcuts import render
from .models import CSEQuestion,ITQuestion,EEEQuestion,ECEQuestion,MECHQuestion
from django.template.response import TemplateResponse
# Create your views here.
def csequiz(request):
	
	ob = CSEQuestion.objects.all().filter(tags="Arrays")
	return TemplateResponse(request,"csequiz.html",{'ob':ob})


def itquiz(request):
	
	ob = CSEQuestion.objects.all().filter(tags="Arrays")
	return TemplateResponse(request,"itquiz.html",{'ob':ob})


def eeequiz(request):
	
	ob = CSEQuestion.objects.all().filter(tags="Arrays")
	return TemplateResponse(request,"eeequiz.html",{'ob':ob})



def ecequiz(request):
	
	ob = CSEQuestion.objects.all().filter(tags="Arrays")
	return TemplateResponse(request,"ecequiz.html",{'ob':ob})



def mechquiz(request):
	
	ob = CSEQuestion.objects.all().filter(tags="Arrays")
	return TemplateResponse(request,"mechquiz.html",{'ob':ob})				