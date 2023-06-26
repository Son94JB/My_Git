from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('<str:search_term>/', views.MovieListView.as_view(), name='movie-list'),
    path('detail/<int:movie_id>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('actor/<int:actor_id>/', views.ActorDetailView.as_view(), name='actor-detail'),
    path('director/<int:director_id>/', views.DirectorDetailView.as_view(), name='director-detail'),
    path('review/<int:movie_id>/<int:review_id>/', views.MovieReviewView.as_view(), name='movie-review'),
    path('review/create/', views.MovieReviewCreateView.as_view(), name='movie-review-create'),
    path('review/<int:review_id>/delete/', views.MovieReviewDeleteView.as_view(), name='movie-review-delete'),
    path('review/<int:review_id>/update/', views.MovieReviewUpdateView.as_view(), name='movie-review-update'),
    # path('genre/', views.GenresList.as_view(), name='genre-list'),
]
