# _*_encoding:utf-8_*_
from django.conf.urls import url, include
from .views import OrgView,AddUserAskView,OrgHomeView,OrgCourseView,OrgDescView,OrgTeacherView,AddFavView
from .forms import  UserAskForm
from django.views.generic import TemplateView

urlpatterns = [
    #课程机构列表
    url(r'^list/$', OrgView.as_view(), name="org_list"),
    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask"),
    url(r'^home/(?P<org_id>.*)/$', OrgHomeView.as_view(), name="org_home"),
    url(r'^course/(?P<org_id>.*)/$', OrgCourseView.as_view(), name="org_course"),
    url(r'^desc/(?P<org_id>.*)/$', OrgDescView.as_view(), name="org_desc"),
    url(r'^teacher/(?P<org_id>.*)/$', OrgTeacherView.as_view(), name="org_teacher"),
    #机构收藏
    url(r'^add_fav/$', AddFavView.as_view(), name="add_fav"),

]