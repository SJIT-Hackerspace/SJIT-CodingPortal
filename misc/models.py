from django.db import models

# Create your models here.
class Batches(models.Model):
	batch = models.CharField(max_length = 100)

	class Meta:
		verbose_name = 'Batch'
		verbose_name_plural = 'Batches'

	def __str__(self):
		return self.batch

class Department(models.Model):
	Department = models.CharField(max_length=100)


	class Meta:
		verbose_name = 'Department'
		verbose_name_plural = 'Departments'

	def __str__(self):
		return self.Department		