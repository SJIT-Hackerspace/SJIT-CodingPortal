from django.db import models

# Create your models here.
class VerbalSubCategories(models.Model):
	name = models.CharField((u"Tag Name"),max_length=200)
	class Meta:
		verbose_name = 'Verbal'
		verbose_name_plural = 'Verbal'
	

	def __str__(self):
		return self.name

class QuizSubCategories(models.Model):
	name = models.CharField((u"Tag Name"),max_length=200)
	class Meta:
		verbose_name = 'Quiz'
		verbose_name_plural = 'Quiz'


	def __str__(self):
		return self.name

class ProgrammingSubCategories(models.Model):
	name = models.CharField((u"Tag Name"),max_length=200)

	class Meta:
		verbose_name = 'Programming'
		verbose_name_plural = 'Programming'


	def __str__(self):
		return self.name