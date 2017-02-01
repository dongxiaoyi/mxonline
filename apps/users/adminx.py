#_*_coding:utf-8_*_
import xadmin
from xadmin import views

from models import EmaliVerifyRecord,Banner

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSetrtings(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"
    menu_style = "accordion"

class EmaliVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time',]
    #搜索框
    search_fields = ['code','email','send_type']
    #过滤器
    list_filter = ['code','email','send_type','send_time',]

xadmin.site.register(EmaliVerifyRecord,EmaliVerifyRecordAdmin)


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time' ]
    # 搜索框
    search_fields = ['title', 'image', 'url', 'index',]
    # 过滤器
    list_filter = ['title', 'image', 'url', 'index','add_time'  ]

xadmin.site.register(Banner,BannerAdmin)

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetrtings)