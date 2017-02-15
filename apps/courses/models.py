#_*_encoding:utf-8_*_
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from organization.models import CourseOrg,Teacher

class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg,verbose_name='课程机构',null=True)
    name = models.CharField(max_length=50,verbose_name=u'课程名')
    desc = models.CharField(max_length=300,verbose_name=u'课程描述')
    detail= models.TextField(verbose_name=u'课程详情')
    teacher = models.ForeignKey(Teacher,verbose_name=u'课程讲师',null=True,blank=True)
    degree= models.CharField(verbose_name=u'难度',choices=(("cj","初级"),("zj","中级"),("gj","高级")),max_length=2)
    learn_times = models.IntegerField(default=0,verbose_name=u"学习时长（分钟数）")
    students= models.IntegerField(default=0,verbose_name=u'学习人数')
    fav_num = models.IntegerField(default=0,verbose_name=u'收藏人数')
    category = models.CharField(verbose_name=u'课程类别',max_length=20,default=u'后端开发')
    tag = models.CharField(default='',verbose_name=u'课程标签',max_length=10)
    image = models.ImageField(upload_to='courses/%Y/%m',verbose_name=u'封面图',max_length=100)
    click_nums = models.IntegerField(default=0,verbose_name=u'点击数')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    need_know = models.CharField(max_length=300,verbose_name=u'课程须知',default='')
    teacher_tell_you = models.CharField(max_length=300,verbose_name=u'讲师告诉你',default='')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name

    def get_zjs_nums(self):
        #获取课程章节数
        return self.lesson_set.all().count()

    def get_learn_users(self):
        #获取学习过课程的用户
        return self.usercourse_set.all()[:5]

    def get_teacher_num(self):
        return self.teacher_set.all().count()

    def get_course_lesson(self):
        #获取章节
        return self.lesson_set.all()

    def __unicode__(self):
        return '{0}'.format(self.name)


class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name=u'课程')
    name = models.CharField(max_length=100,verbose_name=u'章节名')
    learn_times = models.IntegerField(default=0,verbose_name=u"学习时长（分钟数）")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name

    def get_lesson_video(self):
        return self.vidoe_set.all()

    def __unicode__(self):
        return self.name


class Vidoe(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name=u'章节名')
    name = models.CharField(max_length=100, verbose_name=u'视频名称')
    url = models.CharField(max_length=200,default='',verbose_name=u'视频链接')
    learn_times = models.IntegerField(default=0,verbose_name=u"学习时长（分钟数）")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'名称')
    download = models.FileField(upload_to="course/resource/%Y/%m",verbose_name=u'资源文件',max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name