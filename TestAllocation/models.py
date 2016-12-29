from django.db import models
from hackerspace.models import *
from misc.models import *
from Subcategories.models import *
from itertools import chain
# Create your models here.



class Programming(models.Model):
	dept = Department.objects.values_list()
	pgmtags = ProgrammingSubCategories.objects.values_list()
	batch = Batches.objects.values_list()
	TestName = models.CharField(max_length=200,default="")
	ProgrammingTagName = models.IntegerField((u"Programming Tags"),choices = tuple(pgmtags))
	StartDate = models.DateField((u"Start Date"), blank=True)
	StartTime = models.TimeField((u"Start Time"), blank=True)
	EndDate = models.DateField((u"End Date"), blank=True)
	EndTime = models.TimeField((u"End Time"), blank=True)
	Batch = models.IntegerField(choices = tuple(batch))
	Department = models.IntegerField(choices = tuple(dept))
	class Meta:
		verbose_name = 'Programming'
		verbose_name_plural = 'Programming'


	def __str__(self):
		return str(self.pgmtags[int(self.ProgrammingTagName)-1][1])+" "+str(self.StartDate)+" "+str(self.StartTime)+" "+str(self.EndDate)+" "+str(self.EndTime)+" "+str(self.batch[int(self.Batch)-1][1])+" "+str(self.dept[int(self.Department)-1][1])

class Quiz(models.Model):
	dept = Department.objects.values_list()
	quiztags = QuizSubCategories.objects.values_list()
	verbaltags = VerbalSubCategories.objects.values_list()
	tags = sorted(chain(quiztags, verbaltags))

	batch = Batches.objects.values_list()
	TestName = models.CharField(max_length=200)
	QuizTagName = models.IntegerField((u"Quiz Tags"),choices = tuple(tags))
	StartDate = models.DateField((u"Start Date"), blank=True)
	StartTime = models.TimeField((u"Start Time"), blank=True)
	EndDate = models.DateField((u"End Date"), blank=True)
	EndTime = models.TimeField((u"End Time"), blank=True)
	Batch = models.IntegerField(choices = tuple(batch))
	Department = models.IntegerField(choices = dept)
	class Meta:
		verbose_name = 'Quiz'
		verbose_name_plural = 'Quiz'
		


	def __str__(self):
		return str(self.quiztags[int(self.QuizTagName)-1][1])+" "+str(self.StartDate)+" "+str(self.StartTime)+" "+str(self.EndDate)+" "+str(self.EndTime)+" "+str(self.batch[int(self.Batch)-1][1])+" "+str(self.dept[int(self.Department)-1][1])

class Verbal(models.Model):
	dept = Department.objects.values_list()
	quiztags = QuizSubCategories.objects.values_list()
	verbaltags = VerbalSubCategories.objects.values_list()
	tags = sorted(chain(verbaltags))

	batch = Batches.objects.values_list()
	TestName = models.CharField(max_length=200)
	VerbalTagName = models.IntegerField((u"Verbal Tags"),choices = tuple(tags))
	StartDate = models.DateField((u"Start Date"), blank=True)
	StartTime = models.TimeField((u"Start Time"), blank=True)
	EndDate = models.DateField((u"End Date"), blank=True)
	EndTime = models.TimeField((u"End Time"), blank=True)
	Batch = models.IntegerField(choices = tuple(batch))
	Department = models.IntegerField(choices = dept)
	class Meta:
		verbose_name = 'Verbal'
		verbose_name_plural = 'Verbal'
		


	def __str__(self):
		return str(self.verbaltags[int(self.VerbalTagName)-1][1])+" "+str(self.StartDate)+" "+str(self.StartTime)+" "+str(self.EndDate)+" "+str(self.EndTime)+" "+str(self.batch[int(self.Batch)-1][1])+" "+str(self.dept[int(self.Department)-1][1])

