from django.db import models

# Create your models here.
class ToDoList(models.Model):
	list_name = models.CharField(max_length=100)
	# tasks = models.ForeignKey(Task, on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.list_name

class Task(models.Model):
	task_name = models.CharField(max_length=100)
	completed = models.BooleanField(default=False)
	parent_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

	def __str__(self):
		return self.task_name
