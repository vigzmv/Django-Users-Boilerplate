from django.conf.urls import url
from . import views
from django.contrib.auth import views as authViews
from .forms import LoginForm
from django.conf import settings

# Template Names
login_template  = settings.DJANGO_USERS_BOILERPLATE_TEMPLATES_NAMES['login']
logout_next_page_template  = settings.DJANGO_USERS_BOILERPLATE_TEMPLATES_NAMES['logout_next_page']

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', authViews.login, {'template_name': login_template,'authentication_form': LoginForm}),
    url(r'^logout/$', authViews.logout, {'next_page': logout_next_page_template}),
    url(r'^register/$', views.register, name="register"),
    url(r'^password/$', views.change_password, name='change_password'),
]
