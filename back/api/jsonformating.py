import json

# JSON 파일 열기
with open('movies/fixtures/genres.json', 'r', encoding='utf-8') as f:
    # JSON 데이터 로드
    data = json.load(f)

# JSON 데이터 다시 인코딩
formatted_data = json.dumps(data, indent=4)

# JSON 파일에 쓰기
with open('movies/fixtures/genres.json', 'w', encoding='utf-8') as f:
    f.write(formatted_data)
