#_*_encoding:utf-8_*_
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import  ModelBackend
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Course,CourseResource
from django.shortcuts import render_to_response
from operation.models import UserFavorite,CourseComments
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


class CourseInfoView(View):
    #课程章节信息
    def get(self,request,course_id):
        course = Course.objects.get(id=int(course_id))
        all_resourses = CourseResource.objects.filter(course=course)
        get_tag = course.tag
        if get_tag:
            relate_courses = Course.objects.filter(tag=get_tag)[:5]
        else:
            relate_courses = []
        return render(request,'course-video.html',{
            'course':course,
            'all_resourses':all_resourses,
            'relate_courses':relate_courses,
        })


class CommentsView(View):
    #课程评论
    def get(self,request,course_id):
        course = Course.objects.get(id=int(course_id))
        all_resourses = CourseResource.objects.filter(course=course)
        all_comments = CourseComments.objects.filter(course=course)
        get_tag = course.tag
        if get_tag:
            relate_courses = Course.objects.filter(tag=get_tag)[:5]
        else:
            relate_courses = []
        return render(request,'course-comment.html',{
            'course':course,
            'all_resourses':all_resourses,
            'relate_courses':relate_courses,
            'all_comments':all_comments,
        })


class AddCommentsView(View):
    # 用户添加评论
    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type='application/json')

        course_id = request.POST.get('course_id', 0)
        comments = request.POST.get('comments', '')
        if course_id > 0 and comments:
            course_comment = CourseComments()
            course = Course.objects.get(id=(course_id))
            course_comment.course = course
            course_comment.comments = comments
            course_comment.user = request.user
            course_comment.save()
            return HttpResponse('{"status":"success","msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"添加失败"}', content_type='application/json')



