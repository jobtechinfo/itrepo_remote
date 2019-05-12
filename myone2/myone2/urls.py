"""myone2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from testapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jobs/', views.jobs_info_view),
    url(r'^index/', views.jobs_list_view),
    url(r'^update/', views.jobs_update_info),
    url(r'^hydjobs/', views.hyd_jobs_view),
    url(r'^update1/', views.hyd_jobs_update),
    url(r'^delete/(?P<id>\d+)/$', views.delete_jobs_view),
    url(r'^hyddelete/(?P<id>\d+)/$', views.hyd_delete_view),
    url(r'^bngljobs/', views.bngl_jobs_view),
    url(r'^update2/', views.bngl_jobs_update),
    url(r'^bngldelete/(?P<id>\d+)/$', views.bngl_delete_view),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/', views.logout_view),
    url(r'^signup/', views.signup_view),


]
