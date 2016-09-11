from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import *
from django.core import serializers
import xml.etree.ElementTree as ET
import json,time
# Create your views here.
def dummy(request):
    ob = Test.objects.all()
    return TemplateResponse(request,"dummy.html",{'ob':ob,'time':(time.strftime("%H:%M:%S")),'date':time.strftime("%Y-%m-%d")})
def index(request):
    """"
	# data = "<data>  				<question>    					this is a question lol!   				</question>				<output>				1				</output>			</data>"
	data = CodingQuestion.objects.values_list('testcases', flat=True).filter(question="Read And Array and return the Sorted Array")
	# data = instance['testcases']
	root = ET.fromstring(str(data[0]))
	testcases=root[0].text
	output=root[1].text
"""
    return TemplateResponse(request,"view.html",{'testcase':testcases,'output':output})



def dataupload(request):

	# data = Students(name="student",rollno="13cs1142",dept="cse",year="IV",Question_solved="question1",Question_partially_solved="question2",total_score=100)
	# data.save()

	# data = Students.objects.all()
    data="dasd"
    return TemplateResponse(request,"hackerspace.html",{'ob':data})


def staff(request):
	return render(request,"staff.html",{})



def register(request):
    try:
    	registration_details = request.POST
    	if( registration_details['password'] == registration_details['rpassword'] ):
        	user = User.objects.create_user(username=registration_details['username'],password=registration_details['password'])
        	user.save();
        	#userscore=ScoreBoard.
        	return render(request,"login.html",{})
    except:
    	return HttpResponse("Already Registered") 

def login(request):
	return render(request,"login.html",{})

def validate(request):
    form_details = request.POST
    user 	 = authenticate(username=form_details['username'],password=form_details['password']);
    
    if user is not None:
        if user.is_active:

        	return render(request,"student.html",{'username':user})
    else:
    	return HttpResponse("not registered")    		