from django.conf.urls import url

from django.contrib.auth import views as auth_views

from .views import allExamsView

# We are adding a URL called /home
urlpatterns = [
    url(r'^viewExams/$', allExamsView.as_view() , name='exams')
]