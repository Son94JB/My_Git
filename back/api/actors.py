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
actor_data = []  # 수정: actor_data 변수를 반복문 밖으로 이동
director_data = []  # 수정: director_data 변수를 반복문 밖으로 이동
for movie in response["results"]:
    movie_id = movie["id"]

    credit_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNDc5YmFiNjM4NDc5Y2YzOTRmODFkN2Y3NTUzNDljZiIsInN1YiI6IjY0NjMwNjE2ZWY4YjMyMDE1NTU2MGZiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UajmXt4iP952FyFvcmrcMSx_hL-kapU475aJR7V3kWg"
    }
    credit_response = requests.get(credit_url, headers=headers)
    credit_response = credit_response.json()
    actor_id = []
    actor_name = []
    director_id = []
    director_name = []
    for cast in credit_response["cast"]:
        if cast["known_for_department"] == "Acting":
            actor_id.append(cast["id"])
            actor_name.append(cast["name"])

    for crew in credit_response["crew"]:
        if  crew["department"] == "Directing":
            director_id.append(cast["id"])
            director_name.append(cast["name"])
   
    for id, name in zip(actor_id, actor_name):
        actor_data.append({
            "model": "movies.actor",
            "pk": id,
            "fields": {
                "name": name,
            }      
        })
    
    for id, name in zip(director_id, director_name):
        director_data.append({
            "model": "movies.director",
            "pk": id,
            "fields": {
                "name": name,
            }      
        })
    
    print(actor_data)
    print(director_data)

# actor_data 저장
with open('movies/fixtures/actors.json', 'w', encoding='utf-8') as f:
    json.dump(actor_data, f, ensure_ascii=False, indent=4)

# director_data 저장
with open('movies/fixtures/directors.json', 'w', encoding='utf-8') as f:
    json.dump(director_data, f, ensure_ascii=False, indent=4)
