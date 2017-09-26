from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}

		if len(postData['name']) == 0:
			errors["name"] = "Please enter a name."
		if len(postData['name']) < 5:
			errors["name"] = "Name must be longer than 5 characters."

		if len(postData['desc']) == 0:
			errors["desc"] = "You must enter a description."
		if len(postData['desc']) < 15:
			errors["desc"] = "Your description must be at least 15 characters long."

		return errors


class Course(models.Model):
	name = models.CharField(max_length=255)
	desc = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = CourseManager()
	def __repr__(self):
		return ("<User object: id:{} {} {}>".format(self.id, self.name, self.desc))