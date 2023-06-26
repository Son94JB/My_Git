import requests
import json
import os
import subprocess


keyword = input("검색할 영화 제목을 입력하세요: ")
url = f"https://api.themoviedb.org/3/search/movie?query={keyword}&include_adult=false&language=ko-KR&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNDc5YmFiNjM4NDc5Y2YzOTRmODFkN2Y3NTUzNDljZiIsInN1YiI6IjY0NjMwNjE2ZWY4YjMyMDE1NTU2MGZiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UajmXt4iP952FyFvcmrcMSx_hL-kapU475aJR7V3kWg"
}

response = requests.get(url, headers=headers)
response = response.json()

# response에서 genre_ids, id, overview, title을 추출해야 함

movies_list = []

for movie in response["results"]:
    id = movie["id"]
    title = movie["title"]
    poster_path = movie["poster_path"]
    genre_ids = movie["genre_ids"]
    overview = movie["overview"]
    
    # id를 이용해 새로운 url을 만들어야 함
    url = f"https://api.themoviedb.org/3/movie/{id}/credits?language=ko-KR"
    credit_response = requests.get(url, headers=headers)
    credit_response = credit_response.json()

    # movie_credit 하나에서 진행하는 중
    # credit_response에서 actor, director를 추출해야 함
    actor_list = []
    director_list = []
    for cast in credit_response["cast"]:
        if cast["known_for_department"] == "Acting":
            actor_data = {
                "model": "movies.actor",
                "pk": cast["id"],
                "fields": {
                    "name": cast["name"],
                }
            }
            actor_list.append(actor_data)

    # movies/fixtures/actors.json 파일에 데이터 추가
    file_path = "movies/fixtures/actors.json"
    if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump([], file)

    with open(file_path, "r+", encoding="utf-8") as file:
        actors = json.load(file)
        for actor_data in actor_list:
            if actor_data not in actors:
                actors.append(actor_data)
        file.seek(0)
        json.dump(actors, file, indent=4, ensure_ascii=False)
        file.truncate()

    for crew in credit_response["crew"]:
        if crew["job"] == "Director":
            director_data = {
                "model": "movies.director",
                "pk": crew["id"],
                "fields": {
                    "name": crew["name"],
                }
            }
            director_list.append(director_data)

    # movies/fixtures/directors.json 파일에 데이터 추가
    file_path = "movies/fixtures/directors.json"
    if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump([], file)

    with open(file_path, "r+", encoding="utf-8") as file:
        directors = json.load(file)
        for director_data in director_list:
            if director_data not in directors:
                directors.append(director_data)
        file.seek(0)
        json.dump(directors, file, indent=4, ensure_ascii=False)
        file.truncate()

    # movies.json 데이터 추가
    movie_data = {
        "model": "movies.movie",
        "pk": id,
        "fields": {
            "title": title,
            "overview": overview,
            "poster": poster_path,
            "trailer": "trailer",
            "genre": genre_ids,
            "actor": [actor["pk"] for actor in actor_list],
            "director": [director["pk"] for director in director_list]
        }
    }

    # movies/fixtures/movies.json 파일에서 동일한 pk 값의 데이터 제거
    file_path = "movies/fixtures/movies.json"
    if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump([], file)

    with open(file_path, "r+", encoding="utf-8") as file:
        movies = json.load(file)
        movies = [data for data in movies if data["pk"] != movie_data["pk"]]
        movies.append(movie_data)
        file.seek(0)
        json.dump(movies, file, indent=4, ensure_ascii=False)
        file.truncate()

# movies/fixtures/movies.json 파일에 데이터 추가
file_path = "movies/fixtures/movies.json"
if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump([], file)

with open(file_path, "r+", encoding="utf-8") as file:
    movies = json.load(file)
    for movie_data in movies_list:
        if movie_data not in movies:
            movies.append(movie_data)
    file.seek(0)
    json.dump(movies, file, indent=4, ensure_ascii=False)
    file.truncate()

subprocess.call(["python", "manage.py", "loaddata", "actors.json"])
subprocess.call(["python", "manage.py", "loaddata", "directors.json"])
subprocess.call(["python", "manage.py", "loaddata", "movies.json"])