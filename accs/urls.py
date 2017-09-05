from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'accs/login.html'}),
    url(r'^logout/$', auth_views.logout, {'template_name': 'accs/logout.html'})
]