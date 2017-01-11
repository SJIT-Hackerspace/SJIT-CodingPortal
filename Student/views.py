from django.shortcuts import render
from django.template.response import TemplateResponse
from Questions.models import *
from TestAllocation.models import *
import datetime
from django.http import HttpResponse
import requests
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
	ob2 = Programming.objects.all().filter(StartDate__lte=d,StartTime__lt=t,EndDate__gte=d,EndTime__gt=t)

	obj = Quiz.objects.all().order_by('StartTime')
	return render(request,"blank.html",{'tests':ob,'time':time,'testsall':obj,'prog':ob2})


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
			return TemplateResponse(request,"code_interface.html",{'ob':ob,'min':50000})	


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




def save_source(request):
	qno = request.session["qno"]
	request.session.modified = True
	request.session["source"][str(qno)]=str(request.POST["source"])
	request.session["language"][str(qno)]=str(request.POST["language"])
	request.session["min"]=request.POST["time"]

	return redirect("/student/ide")
	# return HttpResponse(request.POST["time"])

def usernames(request):
	ob=Attended.objects.all()
	return TemplateResponse(request,"user.html",{'ob':ob})
def navigate(request):
	if '1' in request.POST:
		request.session["qno"]="0"
	if '2' in request.POST:
		request.session["qno"]="1"
	if '3' in request.POST:
		request.session["qno"]="2"
	if '4' in request.POST:
		request.session["qno"]="3"
	if '5' in request.POST:
		request.session["qno"]="4"	
	request.session["min"]=request.POST["time"]
	
	return redirect("/student/ide")
	# return HttpResponse(request.POST["time"])


def ide(request):
	try:
	
		if "score" not in request.session:
			request.session["score"] = str("0")
		if "qno" not in request.session:		
			request.session["qno"] = str("0")
		if "count" not in request.session:		
			request.session["count"] = str("0")
		if "attended" not in request.session:
			request.session["attended"]=[]				
			del request.session["attended"][:]
		if "source" not in request.session:
			request.session["source"]={}			
			request.session.modified = True
			request.session["source"][0]="^"
			request.session["source"][1]="^"
			request.session["source"][2]="^"
			request.session["source"][3]="^"
			request.session["source"][4]="^"
		if "language" not in request.session:
			request.session["language"]={} 	
			request.session.modified = True		
			request.session["language"][0]=""
			request.session["language"][1]=""
			request.session["language"][2]=""
			request.session["language"][3]=""
			request.session["language"][4]=""
		if "min" not in request.session:
			request.session["min"]="3600000"			


		user = request.session["user"]
		json_data = open('student/static/quest.json','r').read()
		qno = int(request.session["qno"])
		question = json_data.split("splitkey")
		testcases = question[qno].split("testt")
		testcase = testcases[1].split("out") 
		output = testcase[1].split("sub")
		question = question[qno].split("testt")
	
		return render(request,"code_interface.html",{'user':user,'question':question[0],'testcases':testcase[0],'output':output[0],'submit':output[1],'attended':request.session["attended"],'count':request.session["count"],'qno':request.session["qno"],'source_code':json.dumps(request.session["source"][(qno)]),'lang':json.dumps(request.session["language"][(qno)]),'min':request.session["min"]})
		# return HttpResponse(json.dumps(request.session["source"]['0']))		
	except :
		try:
			return render(request,"code_interface.html",{'user':user,'question':question[0],'testcases':testcase[0],'output':output[0],'submit':output[1],'attended':request.session["attended"],'count':request.session["count"],'qno':request.session["qno"],'source_code':json.dumps(request.session["source"][str(qno)]),'lang':json.dumps(request.session["language"][str(qno)]),'min':request.session["min"]})
		except:
			return HttpResponse(" ")			

	# return HttpResponse(json_data)





def get(request):
	requestdict = request.POST
	source = requestdict["source"]
	lang = requestdict["lang"]
	testcases = requestdict["testcases"]
	output=requestdict.get("output")
	timeout=1
	
	url = "api.hackerrank.com/checker/submission.json"
	api_key = "hackerrank|161256-622|faa76a548e2dce2ef37df6a68d4dc0c75bd760f3"
	r = requests.post("http://api.hackerrank.com/checker/submission.json", data = {
	    "source" : source,
	    "lang" : lang,
	    "testcases" : testcases,
	    "api_key" : api_key
	})
	result = r.json()
	try:
		out=int(result['result']['stdout'][0])

	

		output=int(output)
		if(output==out):
			return HttpResponse("Success<br>  Output: "+result['result']['stdout'][0]+ "<br>" +"Compile Time: "+str(result['result']['time'][0])	)
		else:
			return HttpResponse("Wrong Answer. Try Again!"+"<br>"+"Your Output:"+(result['result']['stdout'][0]))
	
		#return HttpResponse(out)	
	except TypeError:	
		return HttpResponse(result['result']['compilemessage'])	
		#return HttpResponse("Compile error:<br>"+result['result']['compilemessage'])
	except KeyError:
		return HttpResponse("Key error<br> Output format not recognized")	
	except ValueError:
		out=str(result['result']['stdout'][0])

	

		output=str(output)
		if(output==out):
			return HttpResponse("Success<br>  Output: "+result['result']['stdout'][0]+ "<br>" +"Compile Time: "+str(result['result']['time'][0])	)
		else:
			return HttpResponse("Wrong Answer. Try Again!"+"<br>"+"Your Output:"+(result['result']['stdout'][0]))
	
			

	except:
		return HttpResponse("Compile error<br> Unexcpected output (output type not allowed)")


def sub(request):
	
	requestdict = request.POST
	source = requestdict["source"]
	lang = requestdict["lang"]
	testcases = requestdict["testcases"]
	output=requestdict.get("output")
	timeout=1
	
	url = "api.hackerrank.com/checker/submission.json"
	api_key = "hackerrank|161256-622|faa76a548e2dce2ef37df6a68d4dc0c75bd760f3"
	r = requests.post("http://api.hackerrank.com/checker/submission.json", data = {
	    "source" : source,
	    "lang" : lang,
	    "testcases" : testcases,
	    "api_key" : api_key
	})
	result = r.json()
	qno = request.session["qno"]
	request.session["attended"].append(qno)
	next_q = int(qno)
	next_q+=1
	attended = request.session["count"]
	attended= int(attended)
	attended+=1
	
	if next_q == 5 and attended < 5 :
		next_q = 0
	while str(next_q) in request.session["attended"]:		
		if next_q-1< 5:
			next_q+=1
		if next_q-1 == 5:
			next_q=0				


	request.session["qno"] = str(next_q)	
	request.session["count"] = str(attended)
	request.session["min"]=request.POST["time"]

	try:
		out=int(result['result']['stdout'][0])

	

		output=int(output)
		if(output==out):
			scores = request.session["score"]
			score = int(scores)
			score+=1
			request.session["score"] = str(score)
			qno = request.session["qno"]
		if "5" in request.session["count"]:
			user_score = request.session["score"]
			user = request.session["user"]
			student = StudentRecord.objects.get(user_name=request.session["user"])
			student.score=int(request.session["score"])
			student.save()
			
			with open('student/static/report.json', 'a') as f:
				data={
				user:user_score
				}
				json.dump(data,f)

			return TemplateResponse(request,"student_score.html",{'score':user_score,'user':user})
		return redirect("/student/ide")
		
		#return HttpResponse(out)	
	except TypeError:	
		if "5" in request.session["count"]:
			try:
				user_score = request.session["score"]
				user = request.session["user"]
				mins = request.POST["time"]
				student = StudentRecord.objects.get(user_name=request.session["user"],testName="Training Need Analysis")
				student.score=int(request.session["score"])
				student.time = int((3600000-int(mins))/1000)
				student.save()
				return TemplateResponse(request,"404.html",{})
			except:
				return TemplateResponse(request,"404.html",{})
		return redirect("/student/ide")
		#return HttpResponse("Compile error:<br>"+result['result']['compilemessage'])
	except KeyError:
		if "5" in request.session["count"]:
			try:
				user_score = request.session["score"]
				user = request.session["user"]
				mins = request.POST["time"]
				student = StudentRecord.objects.get(user_name=request.session["user"],testName="Training Need Analysis")
				student.score=int(request.session["score"])
				student.time = int((3600000-int(mins))/1000)
				student.save()
				return TemplateResponse(request,"404.html",{})
			except:
				return TemplateResponse(request,"404.html",{})
		return redirect("/student/ide")
	except ValueError:

		out=str(result['result']['stdout'][0])

	

		output=str(output)
		if(output==out):
			scores = request.session["score"]
			score = int(scores)
			score+=1
			request.session["score"] = str(score)
			qno = request.session["qno"]
		if next_q==5:
			try:
				user_score = request.session["score"]
				user = request.session["user"]
				mins = request.POST["time"]
				student = StudentRecord.objects.get(user_name=request.session["user"],testName="Training Need Analysis")
				student.score=int(request.session["score"])
				student.time = int((3600000-int(mins))/1000)
				student.save()
				return TemplateResponse(request,"404.html",{})
			except:
				return TemplateResponse(request,"404.html",{})
		return redirect("/student/ide")				
	except:
		if "5" in request.session["count"]:

			try:
				user_score = request.session["score"]
				user = request.session["user"]
				mins = request.POST["time"]
				student = StudentRecord.objects.get(user_name=request.session["user"],testName="Training Need Analysis")
				student.score=int(request.session["score"])
				student.time = int((3600000-int(mins))/1000)
				student.save()
				return TemplateResponse(request,"404.html",{})
			except:
				return TemplateResponse(request,"404.html",{})									
		return redirect("/student/ide")

def finish(request):
	try:
		attended = Attended(testName="Training Need Analysis",user_name = request.session["user"])
		attended.save()

		user_score = request.session["score"]
		user = request.session["user"]
		mins = request.POST["time"]
		student = StudentRecord.objects.get(user_name=request.session["user"],testName="Training Need Analysis")
		student.score=int(request.session["score"])
		student.time = int((3600000-int(mins))/1000)
		student.save()
	
		return TemplateResponse(request,"404.html",{})
	except:
		return TemplateResponse(request,"404.html",{})						
