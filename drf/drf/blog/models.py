# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=300)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(null=True, blank=True)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self, post_data):
        print post_data
        self.published_date = timezone.now()
        self.save()
        return self


    def __str__(self):
        return self.title

    def getPosts(self):
        self.objects.all()
        return self
    def getName(self):
        return "shail"
