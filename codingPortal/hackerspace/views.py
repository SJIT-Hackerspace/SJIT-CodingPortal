from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import Questions
from django.core import serializers
import xml.etree.ElementTree as ET
import json
# Create your views here.
def index(request):
	# data = "<data>  				<question>    					this is a question lol!   				</question>				<output>				1				</output>			</data>"
	data = Questions.objects.values_list('testcases', flat=True).filter(question="Question")
	# data = instance['testcases']
	root = ET.fromstring(str(data[0]))
	testcases=root[0].text
	output=root[1].text

	return TemplateResponse(request,"view.html",{'testcase':testcases,'output':output})