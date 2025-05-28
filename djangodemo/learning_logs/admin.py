from django.contrib import admin

# Register your models here.
# .models 表示在当前文件所属目录下查找 models.py文件
from .models import Topic
from .models import Entry

admin.site.register(Topic)
admin.site.register(Entry)
