# _*_encoding:utf-8_*_
from django.conf.urls import url
from django.views.generic import TemplateView
from .views import UserInfoView,ImageUploadView,UpdatePwdView,SendEmailCodeView,UpdateEmailView,MyCourseView

urlpatterns = [
    #用户信息
    url(r'^info/$', UserInfoView.as_view(), name="user_info"),

    # 用户头像上传
    url(r'^image-upload/$', ImageUploadView.as_view(), name="image_upload"),

    # 用户个人中心修改密码
    url(r'^update_password/$', UpdatePwdView.as_view(), name="update_password"),

    # 发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),

    # 修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),

    # 我的课程
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),
]