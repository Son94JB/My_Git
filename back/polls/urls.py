from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('genre/', views.GenresList.as_view(), name='genre-list'),
    path('createpoll/', views.CreatePoll.as_view(), name='create-poll'),
    path('recommend/', views.recommend, name='recommend'),

]
