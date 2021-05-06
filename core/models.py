from django.db import models
from django.contrib.auth.models import User

class AuthorInfo(models.Model):
    title_ch = models.CharField(max_length=100, blank=True)
    title_en = models.CharField(max_length=100, blank=True)
    xueyuan = models.CharField(max_length=100, blank=True)
    zhuanye = models.CharField(max_length=100, blank=True)
    xuehao = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    laoshi = models.CharField(max_length=100, blank=True)
    riqi = models.DateField()
    outputname = models.CharField(max_length=100,blank=True)


class AbstractInfo(models.Model):
    keyword_ch = models.CharField(max_length=100,blank=True)
    abstract_ch = models.TextField(max_length=2000,blank=True)

    keyword_en = models.CharField(max_length=100,blank=True)
    abstract_en = models.TextField(max_length=2000,blank=True)


class ContentInfo(models.Model):
    content1 = models.TextField(max_length=2000, blank=True)
    content2 = models.TextField(max_length=2000,blank=True)
    content3 = models.TextField(max_length=2000, blank=True)
    content4 = models.TextField(max_length=2000, blank=True)
    content5 = models.TextField(max_length=2000, blank=True)
    content6 = models.TextField(max_length=2000, blank=True)
    content7 = models.TextField(max_length=2000, blank=True)



class PaperAfter(models.Model):
    bibliography = models.TextField(max_length=1000,blank=True)
    acknowledgment = models.TextField(max_length=1000,blank=True)



