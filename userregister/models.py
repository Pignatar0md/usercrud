# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	secr_question = models.CharField(max_length=30)
	secr_answer = models.CharField(max_length=30)

	def __str__(self):
		return self.username

	def __str__(self):
		return self.password

	def __str__(self):
		return self.secr_question

	def __str__(self):
		return self.secr_answer