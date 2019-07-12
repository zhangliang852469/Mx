# -*- coding: utf-8 -*-
#!/usr/bin/env python3

__author__ = 'zl'
__date__ = '2019/7/12 11:00'

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ('name', 'desc', 'add_time')  # 排序
    search_fields = ('name', 'desc')  # 搜索
    list_filter = ('name', 'desc')  # 筛选


class CourseOrgAdmin(object):
    list_display = ('name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time')  # 排序
    search_fields = ('name', 'desc', 'click_nums', 'fav_nums', 'address', 'city')  # 搜索
    list_filter = ('name', 'desc', 'click_nums', 'fav_nums', 'address', 'city')  # 筛选


class TeacherAdmin(object):
    list_display = ('name', 'org', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                    'add_time')  # 排序
    search_fields = ('name', 'org', 'work_years')  # 搜索
    list_filter = ('name', 'org', 'work_years', 'work_company', 'work_position', 'points', 'click_nums',
                   'fav_nums')  # 筛选


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)

