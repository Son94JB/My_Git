from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.views import UserDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    # path('accounts/user/', UserDetailsView.as_view(), name='user_details'),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    path('movies/', include('movies.urls')),
    path('polls/', include('polls.urls')),
]
