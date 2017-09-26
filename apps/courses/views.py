# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages

# Create your views here.
def index(request):
	context= {
		"courses" : Course.objects.all()
	}
	return render(request, "courses/index.html", context)

def add(request):
	errors = Course.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags='dookie')
			return redirect('/')
	else:
		course = Course.objects.create()
		course.name = request.POST['name']
		course.desc = request.POST['desc']
		course.save()
		return redirect('/')

def remove(request, course_id):
	context ={
		"course" : Course.objects.get(id = course_id)
	}
	return	render(request, "courses/remove.html", context)

def delete(request, course_id):
	deletecourse = Course.objects.get(id = course_id)
	deletecourse.delete()
	return redirect('/')