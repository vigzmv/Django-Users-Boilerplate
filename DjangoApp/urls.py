from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from App.forms import LoginForm
from App import views as App_v

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('App.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
    url(r'^register/$', App_v.register, name="register"),
    url(r'^password/$', App_v.change_password, name='change_password'),
]