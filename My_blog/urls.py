"""My_blog URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
# from blog.views import index, ac_data_ana
from blog import views
app_name = 'blog'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    # url(r'^add/', views.add, name='add'),   #add/?a=3&b=4 7
    # url(r'^add2/(\d+)/(\d+)', views.add2, name='add2'), #add2/3/4 7
    url(r'^acData/', views.ac_data_ana, name='ac_data_ana'),
    url(r'^statistics/', views.statistics, name='statistics'),
    url(r'^post/(?P<pk>[0-9]+)', views.detail, name='detail'),
    url(r'^(?P<cate_name>[\w]+)/', views.category, name='category'),
    url(r'^(?P<tag_name>[\w]+)', views.tag, name='tag'),

]
