from django.db import models

# Create your models here.

class CSEQuestion(models.Model):
	question = models.TextField()
	choice1 = models.CharField(max_length=500,default='a')
	choice2 = models.CharField(max_length=500,default='b')
	choice3 = models.CharField(max_length=500,default='c')
	choice4 = models.CharField(max_length=500,default='d')
	answer = models.CharField(max_length=10)
	tags = models.CharField(max_length=200)



	def __str__(self):
		return self.question+self.choice1+self.choice2+self.choice3+self.choice4+self.tags+self.answer


class EEEQuestion(models.Model):
	question = models.TextField()
	choice1 = models.CharField(max_length=500,default='a')
	choice2 = models.CharField(max_length=500,default='b')
	choice3 = models.CharField(max_length=500,default='c')
	choice4 = models.CharField(max_length=500,default='d')
	answer = models.CharField(max_length=10)
	tags = models.CharField(max_length=200)



	def __str__(self):
		return self.question+self.choice1+self.choice2+self.choice3+self.choice4+self.tags+self.answer




class ECEQuestion(models.Model):
	question = models.TextField()
	choice1 = models.CharField(max_length=500,default='a')
	choice2 = models.CharField(max_length=500,default='b')
	choice3 = models.CharField(max_length=500,default='c')
	choice4 = models.CharField(max_length=500,default='d')
	answer = models.CharField(max_length=10)
	tags = models.CharField(max_length=200)



	def __str__(self):
		return self.question+self.choice1+self.choice2+self.choice3+self.choice4+self.tags+self.answer



class ITQuestion(models.Model):
	question = models.TextField()
	choice1 = models.CharField(max_length=500,default='a')
	choice2 = models.CharField(max_length=500,default='b')
	choice3 = models.CharField(max_length=500,default='c')
	choice4 = models.CharField(max_length=500,default='d')
	answer = models.CharField(max_length=10)
	tags = models.CharField(max_length=200)



	def __str__(self):
		return self.question+self.choice1+self.choice2+self.choice3+self.choice4+self.tags+self.answer	

class MECHQuestion(models.Model):
	question = models.TextField()
	choice1 = models.CharField(max_length=500,default='a')
	choice2 = models.CharField(max_length=500,default='b')
	choice3 = models.CharField(max_length=500,default='c')
	choice4 = models.CharField(max_length=500,default='d')
	answer = models.CharField(max_length=10)
	tags = models.CharField(max_length=200)


	def __str__(self):
		return self.question+self.choice1+self.choice2+self.choice3+self.choice4+self.tags+self.answer			