<template>
  <!-- 클릭하면 showDetail메서드 작동 -->  
  <div v-if="movie" @click="showDetail(movie.id)" class="search-list-item">
    <img v-if="movie.poster" class="movie-poster" :src="`https://image.tmdb.org/t/p/w500/${movie.poster}`" alt="movie poster" />
    <div class="movie-details">
      <h1 class="movie-title">{{ movie.title }}</h1>
      <p class="movie-overview">{{ movie.overview }}</p>
    </div>
  </div>
</template>
  
  <script>
  export default {
    name: 'SearchListItem',
    props: {
      movie: {
        type: Object,
        default: () => {},
      },
    },
    methods: {
      showDetail(movieId) {
        // movieId를 통해 영화 상세 정보 페이지로 이동
        this.$router.push(`/detail/${movieId}`);
        this.$store.dispatch('fetchMovieDetail', movieId);
      }
    },
  }
  </script>
  
  <style scoped>
  .search-list-item {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
  }
  
  .movie-poster {
    width: 150px;
    height: auto;
    margin-right: 20px;
  }
  
  .movie-details {
    flex: 1;
  }
  
  .movie-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .movie-overview {
    font-size: 16px;
  }
  </style>
  