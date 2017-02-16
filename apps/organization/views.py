#_*_encoding:utf-8_*_
from django.shortcuts import render
from django.views.generic.base import View
from models import CourseOrg,CityDict,Teacher
from django.shortcuts import render_to_response
from .forms import UserAskForm
from django.db.models import Q
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from courses.models import Course
import sys
sys.path.append('..')
from operation.models import UserFavorite
# Create your views here.

class OrgView(View):
    #课程机构列表功能
    def get(self,request):
        all_orgs = CourseOrg.objects.all()
        current_nav = 'org'
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_orgs = all_orgs.filter(
                Q(name__icontains=search_keywords) | Q(desc__icontains=search_keywords))
        #热门排序
        hot_orgs = all_orgs.order_by('-click_num')[:3]
        all_citys = CityDict.objects.all()
        #取出筛选城市
        city_id = request.GET.get('city','')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
        #类别筛选
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)
        org_nums = all_orgs.count()
        #排序功能
        sort = request.GET.get('sort','')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by("-students")
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-course_num')
        #分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_orgs,5, request=request)

        orgs = p.page(page)
        return render(request,'org-list.html',{
            'all_orgs':orgs,
            'all_citys':all_citys,
            'org_nums':org_nums,
            'city_id':city_id,
            'category':category,
            'hot_orgs':hot_orgs,
            'sort':sort,
            'current_nav':current_nav,
        })


class AddUserAskView(View):
    """
    yonghutianjiazixiong
    """
    def post(self,request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status":"success"}',content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"添加出错"}',content_type='application/json')


class OrgHomeView(View):
    '''机构首页'''
    def get(self,request,org_id):
        current_page = 'home'
        course_org = CourseOrg.objects.get(id=int(org_id))
        #判断是否收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user,fav_id = int(course_org.id),fav_type=int(2)):
                has_fav = True
        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]
        return render(request,'org-detail-homepage.html',{
            'all_courses':all_courses,
            'all_teachers':all_teachers,
            'course_org':course_org,
            'current_page':current_page,
            'has_fav':has_fav,
        })


class OrgCourseView(View):
    '''机构课程列表页'''
    def get(self,request,org_id):
        current_page = 'course'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=int(course_org.id), fav_type=int(2)):
                has_fav = True
        all_courses = course_org.course_set.all()
        return render(request,'org-detail-course.html',{
            'all_courses':all_courses,
            'course_org':course_org,
            'current_page': current_page,
            'has_fav': has_fav,
        })

class OrgDescView(View):
    '''机构介绍页'''
    def get(self,request,org_id):
        current_page = 'desc'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=int(course_org.id), fav_type=int(2)):
                has_fav = True
        return render(request,'org-detail-desc.html',{
            'course_org':course_org,
            'current_page': current_page,
            'has_fav': has_fav,
        })

class OrgTeacherView(View):
    '''机构讲师页'''
    def get(self,request,org_id):
        current_page = 'teacher'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=int(course_org.id), fav_type=int(2)):
                has_fav = True
        all_teachers = course_org.teacher_set.all()
        return render(request,'org-detail-teachers.html',{
            'course_org':course_org,
            'all_teachers':all_teachers,
            'current_page': current_page,
            'has_fav': has_fav,
        })

class AddFavView(View):
    '''用户收藏，取消收藏'''
    def post(self,request):
        #收藏的课程id和类型由前台ajax传入
        fav_id = request.POST.get('fav_id',0)
        fav_type = request.POST.get('fav_type',0)

        #判断用户是否登录,就算没有登录也会有匿名用户,调用下面方法做判断
        if not request.user.is_authenticated():
            #如果没有登录，返回json
            return HttpResponse('{"status":"fail","msg":"用户未登录"}',content_type='application/json')
        #如果登录，查找已经存在的记录
        exist_records = UserFavorite.objects.filter(user=request.user,fav_id = int(fav_id),fav_type=int(fav_type))
        if exist_records:
            #如果记录已经存在，表示用户取消收藏
            exist_records.delete()
            return HttpResponse('{"status":"success","msg":"收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            if fav_id > 0 and fav_type >0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                return HttpResponse('{"status":"success","msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail","msg":"收藏出错"}', content_type='application/json')

class TeacherListView(View):
    '''
    课程讲师列表页
    '''
    def get(self,request):
        all_teachers = Teacher.objects.all()
        current_nav = 'teacher'
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_teachers = all_teachers.filter(name__icontains=search_keywords)
        #排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'hot':
                all_teachers = all_teachers.order_by("-click_num")
        sorted_teachers = all_teachers.order_by("-click_num")[:3]
        #对讲师分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_teachers,3, request=request)

        teachers = p.page(page)
        return render(request,'teachers-list.html',{
            'all_teachers':teachers,
            'sorted_teachers':sorted_teachers,
            'sort':sort,
            'current_nav':current_nav,
        })


class TeacherDetailView(View):
    def get(self,request,teacher_id):
        teacher = Teacher.objects.get(id=int(teacher_id))
        org_id = teacher.org.id
        #收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=int(org_id), fav_type=int(2)):
                has_fav = True
        #机构相关讲师id
        all_teachers = Teacher.objects.all()
        # 排行榜
        sorted_teachers = all_teachers.order_by("-click_num")[:3]
        return render(request,'teacher-detail.html',{
            'teacher':teacher,
            'sorted_teachers':sorted_teachers,
            'has_fav': has_fav,
        })