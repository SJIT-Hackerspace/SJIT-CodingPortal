from django.db import models
from Subcategories.models import *
# Create your models here.

class QuizFile(models.Model):
	quiz_tags = QuizSubCategories.objects.values_list()
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')
	subCategory = models.IntegerField(choices = tuple(quiz_tags))

	class Meta:
		verbose_name = 'Quiz'
		verbose_name_plural = 'Quiz'


class VerbalFile(models.Model):
	verb_tags = VerbalSubCategories.objects.values_list()
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')
	subCategory = models.IntegerField(choices = tuple(verb_tags))

	class Meta:
		verbose_name = 'Verbal'
		verbose_name_plural = 'Verbal'


class ProgrammingFile(models.Model):
	prog_tags = ProgrammingSubCategories.objects.values_list()
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')
	subCategory = models.IntegerField(choices = tuple(prog_tags))


	class Meta:
		verbose_name = 'Programming'
		verbose_name_plural = 'Programming'
