# -*- coding: utf-8 -*-
#!/usr/bin/env python3
__author__ = 'zl'
__date__ = '2019/7/12 10:51'

import xadmin

from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    list_display = ('name', 'mobile', 'course_name', 'add_time')  # 排序
    search_fields = ('name', 'mobile', 'course_name')  # 搜索
    list_filter = ('name', 'mobile', 'course_name')   # 筛选


class CourseCommentsAdmin(object):
    list_display = ('user', 'course', 'comments', 'add_time')  # 排序
    search_fields = ('user', 'course')  # 搜索
    list_filter = ('user', 'course', 'comments')   # 筛选


class UserFavoriteAdmin(object):
    list_display = ('user', 'fav_id', 'fav_type', 'add_time')  # 排序
    search_fields = ('user', 'fav_id', 'fav_type')  # 搜索
    list_filter = ('user', 'fav_id', 'fav_type')   # 筛选


class UserMessageAdmin(object):
    list_display = ('user', 'message', 'has_read', 'send_time')  # 排序
    search_fields = ('user', 'message', 'has_read')  # 搜索
    list_filter = ('user', 'message', 'has_read')   # 筛选


class UserCourseAdmin(object):
    list_display = ('user', 'course', 'add_time')  # 排序
    search_fields = ('user', 'course')  # 搜索
    list_filter = ('user', 'course')   # 筛选


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)

