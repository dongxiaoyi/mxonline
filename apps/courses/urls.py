# _*_encoding:utf-8_*_
from django.conf.urls import url, include

from django.views.generic import TemplateView
from .views import CourseListView,CourseDetailView,CourseInfoView,CommentsView,AddCommentsView
urlpatterns = [
    #课程机构列表
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    #课程详情页
    url(r'^detail/(?P<course_id>.*)/$', CourseDetailView.as_view(), name="course_detail"),
    #章节信息
    url(r'^info/(?P<course_id>.*)/$', CourseInfoView.as_view(), name="course_info"),
    #课程评论
    url(r'^comment/(?P<course_id>.*)/$', CommentsView.as_view(), name="course_comment"),
    #添加课程评论
    url(r'^add_comment/$', AddCommentsView.as_view(), name="course_addcomment"),

]