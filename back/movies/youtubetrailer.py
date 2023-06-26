import requests

def get_movie_trailer(movie_title, api_key):
    base_url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'q': f'{movie_title} 공식 예고편',
        'type': 'video',
        'key': api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'items' in data and len(data['items']) > 0:
        trailer = data['items'][0]
        video_id = trailer['id']['videoId']
        video_title = trailer['snippet']['title']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        return video_title, video_url, video_id

    return None, None, None