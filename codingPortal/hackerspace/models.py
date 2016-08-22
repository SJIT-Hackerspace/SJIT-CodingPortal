from django.db import models

# Create your models here.
class CodingQuestion(models.Model):
	question = models.TextField()
	testcases = models.TextField()
	tags = models.CharField(max_length=200)
	score = models.IntegerField()


	def __str__(self):
		return self.question+self.testcases+self.tags

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
	


						