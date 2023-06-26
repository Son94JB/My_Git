# class MovieDetailView(APIView):
#     # async 키워드로 정의된 비동기 함수 작성.
#     # async 키워드로 정의된 함수들이 병렬적으로 실행됨
#     # 즉 fetch_actor_profile, fetch_director_profile 함수들이 병렬적으로 실행됨
#     # 하지만 가장 먼저 get 메서드가 실행되어 이벤트 루프를 생성함
    
#     async def fetch_actor_profile(self, actor):
#         # 배우의 프로필 사진을 가져오는 비동기 함수
#         url = f"https://api.themoviedb.org/3/search/person?query={actor.name}&include_adult=false&language=ko-KR&page=1"
#         headers = {
#             "accept": "application/json",
#             "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNDc5YmFiNjM4NDc5Y2YzOTRmODFkN2Y3NTUzNDljZiIsInN1YiI6IjY0NjMwNjE2ZWY4YjMyMDE1NTU2MGZiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UajmXt4iP952FyFvcmrcMSx_hL-kapU475aJR7V3kWg"
#         }

#         # await는 
#         response = await asgiref.sync.async_to_sync(None, requests.get, url, headers)  # 비동기 HTTP 요청
#         response = response.json()

#         # response에서 프로필 사진 경로를 가져옴
#         if "results" in response and len(response["results"]) > 0 and "profile_path" in response["results"][0]:
#             profile_path = response["results"][0]["profile_path"]
#         else:
#             profile_path = None

#         # 배우의 이름과 프로필 사진을 반환
#         return {
#             "name": actor.name,
#             "profile_path": profile_path,
#         }

#     async def fetch_director_profile(self, director):
#         # 감독의 프로필 사진을 가져오는 비동기 함수
#         url = f"https://api.themoviedb.org/3/search/person?query={director.name}&include_adult=false&language=ko-KR&page=1"
#         headers = {
#             "accept": "application/json",
#             "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNDc5YmFiNjM4NDc5Y2YzOTRmODFkN2Y3NTUzNDljZiIsInN1YiI6IjY0NjMwNjE2ZWY4YjMyMDE1NTU2MGZiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UajmXt4iP952FyFvcmrcMSx_hL-kapU475aJR7V3kWg"
#         }

#         response = await self.loop.run_in_executor(None, requests.get, url, headers)  # 비동기 HTTP 요청
#         response = response.json()

#         # response에서 프로필 사진 경로를 가져옴
#         if "results" in response and len(response["results"]) > 0 and "profile_path" in response["results"][0]:
#             profile_path = response["results"][0]["profile_path"]
#         else:
#             profile_path = None

#         # 감독의 이름과 프로필 사진을 반환
#         return {
#             "name": director.name,
#             "profile_path": profile_path,
#         }

#     async def get(self, request, movie_id):
#         # 이벤트 루프 생성
#         self.loop = asyncio.get_event_loop()

#         # 주어진 movie_id에 해당하는 영화 객체를 가져옴
#         movie = Movie.objects.get(pk=movie_id)
#         overview = movie.overview
#         poster = movie.poster
#         actors = movie.actor.all()
#         directors = movie.director.all()
#         genres = movie.genre.all()
#         title = movie.title
#         trailer = movie.trailer

#         # 배우들의 프로필을 비동기적으로 가져오는 작업들을 리스트에 추가
#         # 위에서 선언한 fetch_actor_profile함수는 actors 리스트의 actor를 인자로 받고 있음
#         # 그래서 각 actor 마다 fetch_actor_profile 함수를 실행하게 되는데 이때 비동기적으로 실행되는 것. 즉 모든 배우에 대해 fetch_actor_profile 함수가 동시에 실행됨
#         # 아래의 감독도 마찬가지
#         # 그런데 아직 실행한 것은 아님 아래의 await asyncio.gather(*actor_tasks)에서 비로소 실행됨
#         actor_tasks = [self.fetch_actor_profile(actor) for actor in actors]
#         director_tasks = [self.fetch_director_profile(director) for director in directors]

#         # 비동기 작업들을 병렬로 실행하고 결과를 가져옴
#         # * 언패킹 연산자를 이용해 리스트 내의 작업들을 개별 인자로 전달
#         # 아래 코드는 배우 프로필을 가져오는 연산들을 비동기적으로 처리하고 모든 작업이 완료되면 결과를 actor_profiles에 저장
#         actor_profiles = await asyncio.gather(*actor_tasks)
#         director_profiles = await asyncio.gather(*director_tasks)

#         self.json_response(actor_profiles, director_profiles)
    
#         genre_list = [genre.name for genre in genres]

#         # 가져온 필드들을 하나의 딕셔너리로 만듦
#         movie_detail = {
#             "title": title,
#             "overview": overview,
#             "poster": poster,
#             "genre": genre_list,
#             "actor_profiles": actor_profiles,
#             "director_profiles": director_profiles,
#             "trailer": trailer,
#         }
#         return await JsonResponse(movie_detail)