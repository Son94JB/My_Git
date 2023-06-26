{
        "model": "movies.genre",
        "pk": 1,
        "fields": {
            "name": "genre1"
        }
    },

{
        "model": "movies.director",
        "pk": 1,
        "fields": {
            "name": "direc1"
        }
    },

{
        "model": "movies.actor",
        "pk": 1,
        "fields": {
            "name": "actor1"
        }
    },

{
        "model": "movies.movie",
        "pk": 3,
        "fields": {
            "title": "movie3",
            "poster": "posterpath",
            "trailer": "trailerpath",
            "genre": [
                2,
                5
            ],
            "actor": [
                1,
                2,
                3
            ],
            "director": [
                4
            ]
        }
    }