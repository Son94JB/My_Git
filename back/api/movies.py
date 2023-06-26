import requests
import json
import subprocess

input_keyword = input("검색어를 입력하세요: ")
url = f"https://api.themoviedb.org/3/search/movie?query={input_keyword}&include_adult=false&language=ko-KR&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNDc5YmFiNjM4NDc5Y2YzOTRmODFkN2Y3NTUzNDljZiIsInN1YiI6IjY0NjMwNjE2ZWY4YjMyMDE1NTU2MGZiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UajmXt4iP952FyFvcmrcMSx_hL-kapU475aJR7V3kWg"
}

response = requests.get(url, headers=headers)
response = response.json()

movie_list = []
for movie in response["results"]:
    movie_list.append({
        "model": "movies.movie",
        "fields": {
            "id": movie["id"],
            "title": movie["title"],
        }
    })

# 만약 movie_list에 존재하는 영화가 movies/fixtures/movies.json 파일에 없으면 추가
with open("movies/fixtures/movies.json", "r", encoding="utf-8") as f:
    movies = json.load(f)
    for movie in movie_list:
        if movie['fields'] not in [m['fields'] for m in movies]:
            movies.append(movie)
        print(movies)

# movies를 파일에 저장
with open("movies/fixtures/movies.json", "w", encoding="utf-8") as f:
    json.dump(movies, f, ensure_ascii=False, indent=4)

subprocess.call(["python", "manage.py", "loaddata", "movies/fixtures/movies.json"])

print("영화가 추가되었습니다.")
