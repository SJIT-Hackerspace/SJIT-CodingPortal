from django.db import models

# Create your models here.
class Questions(models.Model):
	question = models.TextField()
	testcases = models.TextField()
	tags = models.CharField(max_length=200)

	def __str__(self):
		return self.question+self.testcases+self.tags