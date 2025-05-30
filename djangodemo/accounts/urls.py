from django.urls import path, include
from . import views

# 命名空间，让django能够将这些URL与其他应用程序的URL区分开
app_name='accounts'
urlpatterns = [
    # 包含django定义的默认身份验证URL
    # 默认的URL有 login logout
    path('', include('django.contrib.auth.urls')),
    # 注册页面
    path('register/', views.register, name='register'),
]
