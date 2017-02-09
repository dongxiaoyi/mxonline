#_*_coding:utf-8_*_

from users.models import EmaliVerifyRecord
from random import Random
from django.core.mail import send_mail
from mxonline.settings import DEFAULT_FROM_EMAIL

def send_register_email(email,send_type="register"):
    email_record = EmaliVerifyRecord()
    code = generic_random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""
    if send_type == "register":
        email_title = "慕学在线网激活链接"
        email_body = "请点击下面的链接激活你的账号：http://localhost:8001/active/{0}".format(code)
        send_status = send_mail(email_title,email_body,DEFAULT_FROM_EMAIL,[email])
        if send_status:
            print "send_email!"
        else:
            print "send false!"
    elif send_type == "forget":
        email_title = "慕学在线网注册密码重置链接"
        email_body = "请点击下面的链接重置你的账号：http://localhost:8001/reset/{0}".format(code)
        send_status = send_mail(email_title,email_body,DEFAULT_FROM_EMAIL,[email])

def generic_random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0,length)]
    return str