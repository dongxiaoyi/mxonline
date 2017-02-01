#_*_coding:utf-8_*_


import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['city', 'name', 'desc', 'address', 'fav_num', 'click_num', 'image', 'add_time']
    search_fields = ['name', 'desc', 'address', 'fav_num', 'click_num', 'image']
    list_filter = ['city__name', 'name', 'desc', 'address', 'fav_num', 'click_num', 'image', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_company', 'work_position', 'work_years', 'points', 'fav_num',
                    'click_num', 'add_time']
    search_fields = ['org', 'name', 'work_company', 'work_position', 'work_years', 'points', 'fav_mun',
                     'click_num']
    list_filter = ['org__name', 'name', 'work_company', 'work_position', 'work_years', 'points', 'fav_num','click_num']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)