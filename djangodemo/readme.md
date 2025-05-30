
# 第一个django应用

初始化一个django项目 `django-admin startproject ll_project .`

最后的.表示 将 Django 项目的文件生成在当前目录下，直接把管理文件如 manage.py放到当前目录下，避免出现ll_project/ll_project/ 这样的嵌套结构

初始化后的项目文件功能：

- settings.py指定django如何与系统交互以及如何管理项目
- wsgi.py 全名 web server gateway interface - Web服务器网关接口

创建sqlite数据库 `python manage.py migrate`
使用runserver运行项目 `python manage.py runserver`
创建webapp  `python manage.py startapp learning_logs`

创建名为0001_initial.py的迁移文件 `python manage.py makemigrations learning_logs` 该文件将在数据库中为模型Topic创建一个表

```bash
Migrations for 'learning_logs':
  learning_logs/migrations/0001_initial.py
    + Create model Topic
```

应用数据库修改 `python manage.py migrate`

```bash
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0001_initial... OK
```

创建超级用户 `python manage.py createsuperuser`
ll_admin/123456
访问 http://127.0.0.1:8000/admin/


修改了models.py 添加了模型后需要再次执行makemigrations
此时出现 0002_entry.py

## 通过django shell交互式会话调试

`python manage.py shell`

```bash
>>> from learning_logs.models import Topic
>>> Topic.objects.all()
<QuerySet [<Topic: Chess>, <Topic: Rock Climbling>]>
>>> [item.id for item in Topic.objects.all()]
[1, 2] # 获取到ID

>>> Topic.objects.get(id=1).text
'Chess'

# 获取一个Topic关联的所有Entry，注意这里的entry_set前面的entry是用户定义的类型
>>> Topic.objects.get(id=1).entry_set.all()
<QuerySet [<Entry: the opening is the first part of the game,roughly 。。。>, <Entry: of course,there are just guidelines,it will be imp。。。>]>

```

经过了一系列的topic entry的CRUD功能的实现，现在开始添加账户管理功能

创建一个 accounts webapp `python manage.py startapp accounts`

django提供了user模型定义，无需开发！

