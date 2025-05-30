'''定义learning_logs的URL pattern'''
from django.urls import path
from . import views

# 定义app_name,让django能够将此urls.py文件与其他应用程序中的urls.py文件区分开
app_name='learning_logs'
urlpatterns = [
    # 主页 path函数的一个入参是url，第二个入参指定调用views.py中的哪个函数；第三个参数是这个url别名，方便引用
    path('index', views.index, name='index'),
    # 显示所有topic的页面
    path('topics', views.topics, name='topics'),
    # 特定Topic下d所有entry查询页面
    path('topics/<int:topic_id>', views.topic, name='topic'),
    # 用于添加新主题的网页
    path('new_topic', views.new_topic, name='new_topic'),
]
