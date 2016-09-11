from django.db import models

# Create your models here.

class Verbal_SubCategories(models.Model):
	name = models.CharField((u"Tag Name"),max_length=200)
	

	def __str__(self):
		return self.name

class Quiz_SubCategories(models.Model):
	name = models.CharField((u"Tag Name"),max_length=200)
	

	def __str__(self):
		return self.name

class Programming_SubCategories(models.Model):
	name = models.CharField((u"Tag Name"),max_length=200)
	

	def __str__(self):
		return self.name

class Batches(models.Model):
	batch = models.CharField(max_length = 100)

	def __str__(self):
		return self.batch


class ProgrammingQuestion(models.Model):
	
	tags = Programming_SubCategories.objects.values_list()
	question = models.TextField()
	TestCases = models.CharField((u"Test Cases"),max_length=200)
	Output = models.CharField(max_length=200)
	subCategory = models.CharField(max_length=200,choices = tuple(tags))

	def __str__(self):
		return self.question+self.subCategory

class Quiz(models.Model):
	
	tags = Quiz_SubCategories.objects.values_list()
	question = models.TextField()
	op1 = models.CharField((u"Option1"),max_length=200)
	op2 = models.CharField((u"Option2"),max_length=200)
	op3 = models.CharField((u"Option3"),max_length=200)
	op4 = models.CharField((u"Option4"),max_length=200)
	Answer = models.CharField(max_length=200)
	subCategory = models.CharField(max_length=200,choices = tuple(tags))

	def __str__(self):
		return self.question+self.op1+self.op2+self.op3+self.op4+self.subCategory

class Verbal(models.Model):
	tags = Verbal_SubCategories.objects.values_list()
	question = models.TextField()
	op1 = models.CharField((u"Option1"),max_length=200)
	op2 = models.CharField((u"Option2"),max_length=200)
	op3 = models.CharField((u"Option3"),max_length=200)
	op4 = models.CharField((u"Option4"),max_length=200)
	Answer = models.CharField(max_length=200)
	subCategory = models.CharField(max_length=200,choices = tuple(tags))

	def __str__(self):
		return self.question+self.op1+self.op2+self.op3+self.op4+self.subCategory


class Test(models.Model):
	dept = ((1,'CSE'),(2,'CIVIL'),(3,'EEE'),(4,'ECE'),(5,'IT'),(6,'MECH'))
	quiztags = Quiz_SubCategories.objects.values_list()
	pgmtags = Programming_SubCategories.objects.values_list()
	batch = Batches.objects.values_list()
	TestName = models.CharField(max_length=200)
	QuizTagName = models.IntegerField((u"Quiz Tags"),choices = tuple(quiztags))
	ProgrammingTagName = models.IntegerField((u"Programming Tags"),choices = tuple(pgmtags))
	StartDate = models.DateField((u"Start Date"), blank=True)
	StartTime = models.TimeField((u"Start Time"), blank=True)
	EndDate = models.DateField((u"End Date"), blank=True)
	EndTime = models.TimeField((u"End Time"), blank=True)
	Batch = models.IntegerField(choices = tuple(batch))
	Department = models.CharField(max_length=200,choices = dept)


	def __str__(self):
		return str(self.TestName)+" "+str(self.quiztags[int(self.QuizTagName)-1][1])+" "+str(self.pgmtags[int(self.ProgrammingTagName)-1][1])+" "+str(self.StartDate)+" "+str(self.StartTime)+" "+str(self.EndDate)+" "+str(self.EndTime)+" "+str(self.batch[int(self.Batch)-1][1])+" "+str(self.dept[int(self.Department)-1][1])








class Students(models.Model):
	name = models.CharField(max_length=100)
	rollno = models.CharField(max_length=6)
	dept = models.CharField(max_length=6)
	year = models.CharField(max_length=5)
	Question_solved = models.TextField()
	Question_partially_solved = models.TextField()
	total_score = models.IntegerField()


	def __str__(self):
		return self.name+self.rollno+self.dept+self.year+self.Question_solved+self.Question_partially_solved


class User(models.Model):
	name = models.CharField(max_length=100)
	rollno = models.CharField(max_length=6)
	dept = models.CharField(max_length=6)
	year = models.CharField(max_length=5)

	def __str__(self):
		return self.name+self.rollno+self.dept+self.year
	


						