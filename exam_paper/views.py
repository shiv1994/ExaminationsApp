# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django_tables2 import RequestConfig

from django.views import generic

from .models import ExamPaper, MembershipExamUser

from .tables import MembershipExamUserTable


# Create your views here.

def allExamsFirstExaminerPaperDetail(request, pk):
    template_name = 'exam_paper/view_exam_paper_detail.html'
    paperObj = ExamPaper.objects.get(pk=pk)
    return render(request, template_name, {"paperObj": paperObj})

# @login_required(login_url="login/")
class allExamsFirstExaminerView(generic.ListView):
    model = ExamPaper

    context_object_name = 'exam_list'

    ordering = ['id']

    template_name = 'exam_paper/view_exam_papers_first_examiner.html'

    def get_context_data(self, **kwargs):
        context = super(allExamsFirstExaminerView, self).get_context_data(**kwargs)
        table = MembershipExamUserTable(MembershipExamUser.objects.filter(firstExaminer__id=self.request.user.id).order_by('-pk'))
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context
