# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import ExamPaper, MembershipExamUser, Course

# Register your models here.

admin.site.register(MembershipExamUser)

admin.site.register(ExamPaper)

admin.site.register(Course)