# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import User


def index(request):
    user_list = User.objects.all()
    context = {
    	'user_list': user_list,
    }
    return render(request, 'userregister/index.html', context)


def detail(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	return render(request, "userregister/detail.html", {'user': user})

def new(request):
	return render(request, "userregister/new.html")

def save(request):
	name = request.POST['username']
	passw = request.POST['password']
	secquest = request.POST['question']
	secansw = request.POST['answer']
	q = User(username=name, password=passw, secr_question=secquest, secr_answer=secansw)
	q.save()
	return HttpResponseRedirect(reverse('userregister:index'))

def update(request):
	ide = request.POST['userid']
	name = request.POST['username']
	passw = request.POST['password']
	secquest = request.POST['question']
	secansw = request.POST['answer']
	q = User(id=ide, username=name, password=passw, secr_question=secquest, secr_answer=secansw)
	q.save()
	return HttpResponseRedirect(reverse('userregister:index'))

def delete(request, user_id):
	q = User.objects.get(pk=user_id)
	q.delete()
	return HttpResponseRedirect(reverse('userregister:index'))