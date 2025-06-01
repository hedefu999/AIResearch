"""
URL configuration for ll_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.conf.urls import handler500
from learning_logs import views

# handler404要放在ll_project目录下才能生效，learning_logs里不可以
handler404 = views.custom_404_view
handler500 = views.custom_500_view

# 默认的urls.py位于 ll_project 文件夹中
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('learning_logs.urls')),
    # 匹配所有以accounts开头的URL
    path('accounts/',include('accounts.urls')),
]
