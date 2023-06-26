from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/<int:article_pk>/', views.comment_basic),
    path('comments/change/<int:comment_id>/', views.comment_change),
]
