from django.shortcuts import render
from django.template.response import TemplateResponse
from Questions.models import *
# Create your views here.
def index(request):
	ob=QuizQuestion.objects.all().order_by('?')[:4]
	return TemplateResponse(request,"index.html",{'ob':ob})