import httpx, requests
from .models import Actor, Director, Movie
from rest_framework.response import Response
import asyncio




class MovieDetail():
    def __init__(self, id, title):
        self.id = id
        self.movie_title = title

    async def get_movie_detail(self, id, title):
        actor_list, director_list, (video_url, video_id) = await asyncio.gather(self.fetch_actor_profile(id), self.fetch_director_profile(id), self.fetch_youtube_trailer(title))
        return actor_list, director_list, video_url, video_id

    async def fetch_actor_profile(self, id):
        url = f"https://api.themoviedb.org/3/movie/{id}/credits?language=en-US"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNDc5YmFiNjM4NDc5Y2YzOTRmODFkN2Y3NTUzNDljZiIsInN1YiI6IjY0NjMwNjE2ZWY4YjMyMDE1NTU2MGZiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UajmXt4iP952FyFvcmrcMSx_hL-kapU475aJR7V3kWg"
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            
        credit_response = response.json()
        
        # 배우 프로필을 담을 리스트
        actor_list = []

        # 배우정보 가져옴
        for cast in credit_response["cast"]:
            if cast["known_for_department"] == "Acting":
                # actor_data = {
                #     "fields": {
                #         "id": cast["id"],
                #         "name": cast["name"],
                #         "profile_path": cast["profile_path"],
                #     }
                # }
                # actor = Actor(**actor_data["fields"])
                # actor.save()
                # actor_list.append(actor)
                actor_data = {
                    "id": cast["id"],
                    "name": cast["name"],
                    "profile_path": cast["profile_path"],
                }
                actor_list.append(actor_data)
        
        return actor_list

    async def fetch_director_profile(self, id):
        url = f"https://api.themoviedb.org/3/movie/{id}/credits?language=en-US"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNDc5YmFiNjM4NDc5Y2YzOTRmODFkN2Y3NTUzNDljZiIsInN1YiI6IjY0NjMwNjE2ZWY4YjMyMDE1NTU2MGZiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UajmXt4iP952FyFvcmrcMSx_hL-kapU475aJR7V3kWg"
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)

        credit_response = response.json()
        
        # 감독 프로필을 담을 리스트
        director_list = []

        # 감독정보 가져옴
        for crew in credit_response["crew"]:
            if crew["job"] == "Director":
                # director_data = {
                #     "fields": {
                #         "id": crew["id"],
                #         "name": crew["name"],
                #         "profile_path": crew["profile_path"],
                #     }
                # }
                # director = Director(**director_data["fields"])
                # director.save()
                # director_list.append(director)
                director_data = {
                    "id": crew["id"],
                    "name": crew["name"],
                    "profile_path": crew["profile_path"],
                }
                director_list.append(director_data) 
        
        return director_list
        

    async def fetch_youtube_trailer(self, title):
        base_url = 'https://www.googleapis.com/youtube/v3/search'
        params = {
            'part': 'snippet',
            'q': f'{title} 공식 예고편',
            'type': 'video',
            'key': 'AIzaSyDqO27_XD1C7soWNsobVyzyaO0LUvidpFA'
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(base_url, params=params)

        data = response.json()

        if 'items' in data and len(data['items']) > 0:
            trailer = data['items'][0]
            video_id = trailer['id']['videoId']
            video_title = trailer['snippet']['title']
            video_url = f'https://www.youtube.com/watch?v={video_id}'
            return video_url, video_id

        return None, None