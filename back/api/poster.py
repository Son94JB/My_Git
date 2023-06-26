import requests

input_keyword = input("검색어를 입력하세요: ")
url = f"https://api.themoviedb.org/3/search/movie?query={input_keyword}&include_adult=false&language=ko-KR&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNDc5YmFiNjM4NDc5Y2YzOTRmODFkN2Y3NTUzNDljZiIsInN1YiI6IjY0NjMwNjE2ZWY4YjMyMDE1NTU2MGZiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UajmXt4iP952FyFvcmrcMSx_hL-kapU475aJR7V3kWg"
}

response = requests.get(url, headers=headers)
# response에서 poster_path를 가져와서 출력
response = response.json()
for movie in response["results"]:
    poster_path = f'https://image.tmdb.org/t/p/w500/{ movie["poster_path"]}'
    print(poster_path)

