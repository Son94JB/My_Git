from django.shortcuts import render
from movies.models import Genre
from .models import Poll
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GenreSerializer, PollSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from dj_rest_auth.models import TokenModel
from rest_framework.decorators import api_view
# from django.http import HttpResponseForbidden
from rest_framework import status
from movies.models import Movie

# Create your views here.


class GenresList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)


class CreatePoll(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        poll = Poll.objects.create(user=request.user)
        print(request.data)
        poll.genre.set(request.data)
        poll.save()
        serializer = PollSerializer(poll)
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = PollSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.genre.set(request.data['genre'])
    #         serializer.save(user=request.user)
    #         return Response(serializer.data)
    #     return Response(serializer.errors)


# 영화 추천 로직
# 1. 토큰을 받아온다. 받아온 토큰으로 유저 아이디를 가져온다.
# 2. 가져온 유저 아이디와 폴의 유저 아이디 중 일치하는 것을 찾는다
# 3, 일치하는 폴 아이디로 장르 아이디들을 추출한다.
# 4, 장르 아이디들로 영화들 중 같은 장르 아이디를 가진 영화들을 추출
# 5, 추출한 영화 모음을 뷰로 보내준다
@api_view(['GET'])
def recommend(request):
    # 1. 토큰을 받아온다. 받아온 토큰으로 유저 아이디를 가져온다.
    user_token = request.headers.get('Authorization').split(' ')[1]
    token_model = TokenModel.objects.filter(key=user_token).first()

    if token_model:
        user_id = token_model.user_id
        # 2. 가져온 유저 아이디와 폴의 유저 아이디 중 일치하는 것을 찾는다
        # 3, 일치하는 폴 아이디로 장르 아이디들을 추출한다.
        genre_ids = Poll.objects.filter(
            user_id=user_id).values_list('genre', flat=True)
        # 4, 장르 아이디들로 영화들 중 같은 장르 아이디를 가진 영화들을 추출
        movies = Movie.objects.filter(
            genre__in=genre_ids)
        movie_list = []
        for movie in movies:
            movie_title = movie.title
            movie_poster = movie.poster
            movie_data = {
                'title': movie_title,
                'poster': movie_poster
            }
            movie_list.append(movie_data)
            print(movie_list)
        # 5, 추출한 영화 모음을 뷰로 보내준다
        return Response(movie_list, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
