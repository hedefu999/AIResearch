from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 用户将存储的主题
class Topic(models.Model):
    """用户学习的主题"""
    # CharField 由字符组成的数据
    text = models.CharField(max_length=200)
    # 用户创建新主题时，django自动设置为当前的日期和时间
    date_added = models.DateTimeField(auto_now_add=True)
    # 该主题的创建人
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              default=1  # 默认关联 User.id = 1
                              )

    def __str__(self):
        return self.text + ';'

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回一个表示条目的简单字符串"""
        return f"{self.text[:50]}。。。"
