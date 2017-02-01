#_*_coding:utf-8_*_
import xadmin

from models import Course,CourseResource,Vidoe,Lesson

class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_times','students','fav_num','image','click_nums','add_time','add_time']
    #搜索框
    search_fields = ['name','desc','detail','degree','learn_times','students','fav_num','image','click_nums']
    #过滤器
    list_filter = ['name','desc','detail','degree','learn_times','students','fav_num','image','click_nums','add_time','add_time']

xadmin.site.register(Course,CourseAdmin)

class LessonAdmin(object):
    list_display = ['course','name','add_time',]
    #搜索框
    search_fields = ['course','name',]
    #过滤器
    list_filter = ['course','name','add_time',]

xadmin.site.register(Lesson,LessonAdmin)

class VidoeAdmin(object):
    list_display = ['lesson','name','add_time',]
    #搜索框
    search_fields = ['lesson','name',]
    #过滤器
    list_filter = ['lesson','name','add_time',]

xadmin.site.register(Vidoe,VidoeAdmin)

class CourseResourceAdmin(object):
    list_display = ['course','name','download','add_time',]
    #搜索框
    search_fields = ['lesson','name','download',]
    #过滤器
    list_filter = ['course','name','download','add_time',]

xadmin.site.register(CourseResource,CourseResourceAdmin)