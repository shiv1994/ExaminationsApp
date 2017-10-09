from django.conf.urls import url

from .views import allExamsFirstExaminerView, allExamsSecondExaminerView, allExamsFirstExaminerPaperDetail,\
    allExamsSecondExaminerPaperDetail, allExamsExternalExaminerPaperDetail, allExamsExternalExaminerView

# We are adding a URL called /home
urlpatterns = [
    url(r'^viewExamsFirst/$', allExamsFirstExaminerView.as_view(), name='exams'),
    url(r'^viewExamsSecond/$', allExamsSecondExaminerView.as_view(), name='exams1'),
    url(r'^viewExamsExternal/$', allExamsExternalExaminerView.as_view(), name='exams2'),
    url(r'^viewExamPaperDetail/(?P<pk>\d+)$', allExamsFirstExaminerPaperDetail,
        name='allExamsFirstExaminerPaperDetail'),
    url(r'^viewExamPaperDetailSecond/(?P<pk>\d+)$', allExamsSecondExaminerPaperDetail,
        name='allExamsSecondExaminerPaperDetail'),
    url(r'^viewExamPaperDetailExternal/(?P<pk>\d+)$', allExamsExternalExaminerPaperDetail,
        name='allExamsExternalExaminerPaperDetail')

]