# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django_tables2 import RequestConfig

from django.views import generic

from .models import ExamPaper, MembershipExamUser

from .tables import MembershipExamUserTable, MembershipExamUserTableSecond, MembershipExamUserTableExternal

# Create your views here.

def allExamsFirstExaminerPaperDetail(request, pk):
    template_name = 'exam_paper/view_exam_paper_detail.html'
    paperObj = ExamPaper.objects.get(pk=pk)
    return render(request, template_name, {"paperObj": paperObj, 'canUploadExam': True, 'canUploadReport': True,
                                           'canUploadSolution': False})


def allExamsSecondExaminerPaperDetail(request, pk):
    template_name = 'exam_paper/view_exam_paper_detail.html'
    paperObj = ExamPaper.objects.get(pk=pk)
    return render(request, template_name, {"paperObj": paperObj, 'canUploadExam': False, 'canUploadReport': True,
                                           'canUploadSolution': False})


def allExamsExternalExaminerPaperDetail(request, pk):
    template_name = 'exam_paper/view_exam_paper_detail.html'
    paperObj = ExamPaper.objects.get(pk=pk)
    return render(request, template_name, {"paperObj": paperObj, 'canUploadExam': False, 'canUploadReport': True,
                                           'canUploadSolution': False})


class allExamsFirstExaminerView(generic.ListView):
    model = ExamPaper

    context_object_name = 'exam_list'

    ordering = ['id']

    template_name = 'exam_paper/view_exam_papers_first_examiner.html'

    def get_context_data(self, **kwargs):
        context = super(allExamsFirstExaminerView, self).get_context_data(**kwargs)
        table = MembershipExamUserTable(MembershipExamUser.objects.filter(firstExaminer__id=self.request.user.id)
                                        .order_by('-pk'))
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class allExamsSecondExaminerView(generic.ListView):
    model = ExamPaper

    context_object_name = 'exam_list'

    ordering = ['id']

    template_name = 'exam_paper/view_exam_papers_second_examiner.html'

    def get_context_data(self, **kwargs):
        context = super(allExamsSecondExaminerView, self).get_context_data(**kwargs)
        table = MembershipExamUserTableSecond(MembershipExamUser.objects.filter(secondExaminer__id=self.request.user.id)
                                              .order_by('-pk'))
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class allExamsExternalExaminerView(generic.ListView):
    model = ExamPaper

    context_object_name = 'exam_list'

    ordering = ['id']

    template_name = 'exam_paper/view_exam_papers_external_examiner.html'

    def get_context_data(self, **kwargs):
        context = super(allExamsExternalExaminerView, self).get_context_data(**kwargs)
        table = MembershipExamUserTableExternal(MembershipExamUser.objects.filter(externalExaminer__id=self.request.user.id)
                                              .order_by('-pk'))
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context
