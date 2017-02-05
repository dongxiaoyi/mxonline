#_*_encoding:utf-8_*_
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
import datetime
class ProfileBase(type):
    def __new__(cls, name, bases, attrs):
        module = attrs.pop('__module__')
        parents = [b for b in bases if isinstance(b, ProfileBase)]
        if parents:
            fields = []
            for obj_name, obj in attrs.items():
                if isinstance(obj, models.Field): fields.append(obj_name)
                User.add_to_class(obj_name, obj)
            UserAdmin.fieldsets = list(UserAdmin.fieldsets)
            UserAdmin.fieldsets.append((name, {'fields': fields}))
        return super(ProfileBase, cls).__new__(cls, name, bases, attrs)

class Profile(object):
    __metaclass__ = ProfileBase
# Create your models here.

class MyUser(Profile):
    nick_name = models.CharField(max_length=50,verbose_name=u'昵称',default="")
    #USERNAME_FIELD = 'nick_name'
    birthday = models.DateField(verbose_name=u'生日',null=True,blank=True)
    is_active = True
    gender = models.CharField(choices=(('male',u'男'),('female',u'女')),default='female',max_length=6,verbose_name=u'性别')
    address = models.CharField(max_length=100,default="",verbose_name=u'地址')
    mobile = models.CharField(max_length=11,null=True,blank=True,verbose_name=u'手机号码')
    image = models.ImageField(upload_to="image/%Y/%m",default=u'image/defaule.png',max_length=100,verbose_name=u'头像')


    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username


class EmaliVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u'验证码')
    email = models.EmailField(max_length=50,verbose_name=u'邮箱')
    send_type = models.CharField(verbose_name=u'验证码类型',choices=(('register',u'注册'),('forget',u'找回密码')),max_length=10)
    send_time = models.DateTimeField(verbose_name='发送时间',default=datetime.datetime.now)

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return '{0}({1})'.format(self.code,self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name=u'标题')
    image = models.ImageField(upload_to='banner/%Y/%m',verbose_name=u'轮播图',max_length=100)
    url = models.URLField(max_length=200,verbose_name=u'访问地址')
    index = models.IntegerField(default=100,verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.datetime.now,verbose_name=u'添加时间')


    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name