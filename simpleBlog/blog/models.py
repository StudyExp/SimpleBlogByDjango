from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tag(models.Model):

    """标签"""
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Category(models.Model):

    """分类目录"""
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Post(models.Model):

    """文章"""

    # 作者
    author = models.ForeignKey(User)
    # 标题
    title = models.CharField(max_length=200)
    # 正文
    text = models.TextField()
    # 标签
    tags = models.ManyToManyField(Tag)
    # 点击量
    click = models.IntegerField(default=0)
    # 创建时间
    created_date = models.DateTimeField(default=timezone.now)
    # 发布时间
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
