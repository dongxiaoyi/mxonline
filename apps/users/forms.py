#_*_coding:utf-8_*_
from django import forms
from captcha.fields import CaptchaField
class LoginForm(forms.Form):
    #required字段判断字段是否为空，如果为空，则报错
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)
class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})
class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})

class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True,min_length=5)
    password2 = forms.CharField(required=True,min_length=5)
