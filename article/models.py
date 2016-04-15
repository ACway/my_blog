# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.tag_nam
class Article(models.Model):
     title = models.CharField(max_length = 100) #博客题目
     category = models.CharField(max_length = 50,blank = True) #博客分类
     tag = models.ManyToManyField(Tag,blank=True)  #博客标签
     date_time = models.DateTimeField(auto_now_add = True)  #博客日期
     content = models.TextField(blank = True, null = True) #博客文章正文
     def get_absolute_url(self):
         path = reverse('detail',kwargs={'id':self.id})
         return "http://115.28.68.125:8080%s" %path
     def __unicode__(self):
         return self.title
     class Meta: #按时间下降排序
         ordering = ['-date_time']
