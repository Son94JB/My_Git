import requests
import json

url = "https://api.themoviedb.org/3/genre/movie/list?language=ko"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNDc5YmFiNjM4NDc5Y2YzOTRmODFkN2Y3NTUzNDljZiIsInN1YiI6IjY0NjMwNjE2ZWY4YjMyMDE1NTU2MGZiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UajmXt4iP952FyFvcmrcMSx_hL-kapU475aJR7V3kWg"
}

response = requests.get(url, headers=headers)
response = response.json()
genre_list = []
for genre in response["genres"]:
    genre_list.append({
        "model": "movies.genre",
        "pk": genre["id"],
        "fields": {
            "name": genre["name"],
        }
    })

# genres.json 예쁘게 포맷팅하여 저장
with open('movies/fixtures/genres.json', 'w', encoding='utf-8') as f:
    json.dump(genre_list, f, indent=4, ensure_ascii=False)

print("genres.json 파일이 예쁘게 포맷팅되어 저장되었습니다.")
