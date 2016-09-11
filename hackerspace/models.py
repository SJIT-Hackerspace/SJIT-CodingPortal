from django.db import models

# Create your models here.






# class Programming(models.Model):
	
# 	tags = Programming_SubCategories.objects.values_list()
# 	question = models.TextField()
# 	TestCases = models.CharField((u"Test Cases"),max_length=200)
# 	Output = models.CharField(max_length=200)
# 	subCategory = models.CharField(max_length=200,choices = tuple(tags))

# 	def __str__(self):
# 		return self.question+self.subCategory

# class Quiz(models.Model):
	
# 	tags = Quiz_SubCategories.objects.values_list()
# 	question = models.TextField()
# 	op1 = models.CharField((u"Option1"),max_length=200)
# 	op2 = models.CharField((u"Option2"),max_length=200)
# 	op3 = models.CharField((u"Option3"),max_length=200)
# 	op4 = models.CharField((u"Option4"),max_length=200)
# 	Answer = models.CharField(max_length=200)
# 	subCategory = models.CharField(max_length=200,choices = tuple(tags))

# 	def __str__(self):
# 		return self.question+self.op1+self.op2+self.op3+self.op4+self.subCategory

# class Verbal(models.Model):
# 	tags = Verbal_SubCategories.objects.values_list()
# 	question = models.TextField()
# 	op1 = models.CharField((u"Option1"),max_length=200)
# 	op2 = models.CharField((u"Option2"),max_length=200)
# 	op3 = models.CharField((u"Option3"),max_length=200)
# 	op4 = models.CharField((u"Option4"),max_length=200)
# 	Answer = models.CharField(max_length=200)
# 	subCategory = models.CharField(max_length=200,choices = tuple(tags))

# 	def __str__(self):
# 		return self.question+self.op1+self.op2+self.op3+self.op4+self.subCategory





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
	


						