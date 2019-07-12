# -*- coding: utf-8 -*-
#!/usr/bin/env python3
__author__ = 'zl'
__date__ = '2019/7/12 9:56'

import xadmin

from .models import EmailVerifyRecord, Banner


class EmailVerifyRecordAdmin(object):
    list_display = ('code', 'email', 'send_type', 'send_time')  # 排序
    search_fields = ('code', 'email', 'send_type')  # 搜索
    list_filter = ('code', 'email', 'send_type', 'send_time')  # 筛选


class BannerAdmin(object):
    list_display = ('title', 'image', 'url', 'add_time')  # 排序
    search_fields = ('title', 'image', 'url', )  # 搜索
    list_filter = ('title', 'image', 'url', 'add_time')  # 筛选


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)