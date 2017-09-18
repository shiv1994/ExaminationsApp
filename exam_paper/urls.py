from django.conf.urls import url

from django.contrib.auth import views as auth_views

from .views import allExamsFirstExaminerView, allExamsFirstExaminerPaperDetail

# We are adding a URL called /home
urlpatterns = [
    url(r'^viewExamsFirst/$', allExamsFirstExaminerView.as_view(), name='exams'),
    url(r'^viewExamPaperDetail//(?P<pk>\d+)$', allExamsFirstExaminerPaperDetail, name='allExamsFirstExaminerPaperDetail')
]