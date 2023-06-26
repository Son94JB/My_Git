from django.db import models
from django.conf import settings

# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # article_like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='article_like')

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#     comment_like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='comment_like')

# class CommentLike(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

# class ArticleLike(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
