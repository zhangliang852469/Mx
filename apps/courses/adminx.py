# -*- coding: utf-8 -*-
#!/usr/bin/env python3


__author__ = 'zl'
__date__ = '2019/7/12 10:35'
import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ('name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time')  # 排序
    search_fields = ('name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums')  # 搜索
    list_filter = ('name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums')   # 筛选


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']  # 排序
    search_fields = ('course', 'name')  # 搜索
    list_filter = ('course', 'name')   # 筛选


class VideoAdmin(object):
    list_display = ('lesson', 'name', 'add_time')  # 排序
    search_fields = ('lesson', 'name')  # 搜索
    list_filter = ('lesson', 'name')   # 筛选


class CourseResourceAdmin(object):
    list_display = ('course', 'name', 'download', 'add_time')  # 排序
    search_fields = ('course', 'name')  # 搜索
    list_filter = ('course', 'name')   # 筛选


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)