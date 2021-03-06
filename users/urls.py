from django.conf.urls import url
from . import views

app_name='users'
urlpatterns=[
        url(r'^user/register/$', views.register, name='register_url'),
        url(r'^user/login/$',views.login,name='login_url'),
        url(r'^user/logout/$',views.logout,name='logout_url'),
        url(r'^user/information_change/$',views.information_change,name='information_url'),
        url(r'^user/changepassword/$',views.change_password,name='changpassword_url'),
]