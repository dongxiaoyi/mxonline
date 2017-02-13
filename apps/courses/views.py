#_*_encoding:utf-8_*_
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import  ModelBackend
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Course
from django.shortcuts import render_to_response
from operation.models import UserFavorite
# Create your views here.


class CourseListView(View):
    def get(self,request):
        all_courses = Course.objects.all().order_by('-add_time')
        hot_courses = Course.objects.all().order_by('-click_nums')[:3]
        #排序功能
        sort = request.GET.get('sort','')
        if sort:
            if sort == 'students':
                all_courses = all_courses.order_by("-students")
            elif sort == 'hot':
                all_courses = all_courses.order_by('-click_nums')
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_courses, 4, request=request)

        courses = p.page(page)
        return render(request,'course-list.html',{
            'all_courses':courses,
            'sort':sort,
            'hot_courses':hot_courses,
        })


class CourseDetailView(View):
    '''
    课程详情页
    '''
    def get(self,request,course_id):
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()
        has_fav_course = False
        has_fav_org = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user,fav_id = course.id,fav_type=1):
                has_fav_course =True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=2):
                has_fav_org =True

        get_tag = course.tag
        if get_tag:
            relate_courses = Course.objects.filter(tag=get_tag)[:1]
        else:
            relate_courses = []
        return render(request,'course-detail.html',{
            'course':course,
            'relate_courses':relate_courses,
            'has_fav_course':has_fav_course,
            'has_fav_org':has_fav_org,
        })