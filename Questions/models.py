from django.db import models
from Subcategories.models import *
# Create your models here.
class ProgrammingQuestion(models.Model):
	
	tags = ProgrammingSubCategories.objects.values_list()
	question = models.TextField()
	TestCases = models.CharField((u"Test Cases"),max_length=200)
	Output = models.CharField(max_length=200)
	subCategory = models.IntegerField(choices = tuple(tags))

	class Meta:
		verbose_name = 'Programming'
		verbose_name_plural = 'Programming'

	def __str__(self):
		return self.question+str(self.subCategory)

class QuizQuestion(models.Model):
	
	tags = QuizSubCategories.objects.values_list()
	question = models.TextField()
	op1 = models.CharField((u"Option1"),max_length=200)
	op2 = models.CharField((u"Option2"),max_length=200)
	op3 = models.CharField((u"Option3"),max_length=200)
	op4 = models.CharField((u"Option4"),max_length=200)
	Answer = models.CharField(max_length=200)
	subCategory = models.IntegerField(choices = tuple(tags))

	class Meta:
		verbose_name = 'Quiz'
		verbose_name_plural = 'Quiz'

	def __str__(self):
		return self.question+self.op1+self.op2+self.op3+self.op4+str(self.subCategory)

class VerbalQuestion(models.Model):
	tags = VerbalSubCategories.objects.values_list()
	question = models.TextField()
	op1 = models.CharField((u"Option1"),max_length=200)
	op2 = models.CharField((u"Option2"),max_length=200)
	op3 = models.CharField((u"Option3"),max_length=200)
	op4 = models.CharField((u"Option4"),max_length=200)
	Answer = models.CharField(max_length=200)
	subCategory = models.IntegerField(choices = tuple(tags))

	class Meta:
		verbose_name = 'Verbal'
		verbose_name_plural = 'Verbal'

	def __str__(self):
		return self.question+self.op1+self.op2+self.op3+self.op4+str(self.subCategory)
