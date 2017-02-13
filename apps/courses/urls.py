# _*_encoding:utf-8_*_
from django.conf.urls import url, include

from django.views.generic import TemplateView
from .views import CourseListView,CourseDetailView
urlpatterns = [
    #课程机构列表
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    #课程详情页
    url(r'^detail/(?P<course_id>.*)/$', CourseDetailView.as_view(), name="course_detail"),
]