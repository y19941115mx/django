"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from mysite.views import LoginView, IndexView, RegisterView, OrderView, LogoutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 登录
    url(r'^login/$', LoginView.as_view(), name='login'),
    # 首页
    url(r'^$', IndexView.as_view(), name='index'),
    # 注册
    url(r'^register/$', RegisterView.as_view(), name='register'),
    # 订房
    url(r'^order/$', OrderView.as_view(), name='order'),
    # 退出登录
    url(r'^logout/$', LogoutView.as_view(), name='logout')
]
