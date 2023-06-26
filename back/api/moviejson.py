import requests
import json

url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNDc5YmFiNjM4NDc5Y2YzOTRmODFkN2Y3NTUzNDljZiIsInN1YiI6IjY0NjMwNjE2ZWY4YjMyMDE1NTU2MGZiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UajmXt4iP952FyFvcmrcMSx_hL-kapU475aJR7V3kWg"
}

response = requests.get(url, headers=headers)
response = response.json()
movie_list = []
print(len(response["results"]))
for movie in response["results"]:
    movie_id = movie["id"]
    movie_title = movie["title"]
    movie_poster_path = movie["poster_path"]
    movie_genre_ids = movie["genre_ids"]

    credit_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNDc5YmFiNjM4NDc5Y2YzOTRmODFkN2Y3NTUzNDljZiIsInN1YiI6IjY0NjMwNjE2ZWY4YjMyMDE1NTU2MGZiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UajmXt4iP952FyFvcmrcMSx_hL-kapU475aJR7V3kWg"
    }
    credit_response = requests.get(credit_url, headers=headers)
    credit_response = credit_response.json()
    actor_list = []
    director_list = []
    for cast in credit_response["cast"]:
        if cast["known_for_department"] == "Acting":
            actor_list.append(cast["id"])
    
    for crew in credit_response["crew"]:
        if crew["department"] == "Directing":
            director_list.append(crew["id"])

    movie_data = {
        "model": "movies.movie",
        "pk": movie_id,
        "fields": {
            "title": movie_title,
            "poster": movie_poster_path,
            "trailer": "trailerpath",
            "genre": movie_genre_ids,
            "actor": actor_list,
            "director": director_list
        }
    }
    movie_list.append(movie_data)
    # print(len(movie_list))

# movies.json 예쁘게 포맷팅하여 저장
with open('movies/fixtures/movies.json', 'w', encoding='utf-8') as f:
    json.dump(movie_list, f, indent=4, ensure_ascii=False)

print("movies.json 파일이 예쁘게 포맷팅되어 저장되었습니다.")
