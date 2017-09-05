# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.decorators import login_required

import django_tables2 as tables

from django.views import generic

from .models import ExamPaper, MembershipExamUser


# Create your views here.

# @login_required(login_url="login/")
class allExamsView(generic.ListView):
    model = ExamPaper
    context_object_name = 'exam_list'

    def get_queryset(self):
        return MembershipExamUser.objects.filter(firstExaminer__id=self.request.user.id)

    template_name = 'exam_paper/view_exam_papers.html'
