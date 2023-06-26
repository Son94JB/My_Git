<template>
  <div>
    <h2>{{ movieReview.user }}</h2>
    <form @submit.prevent="updatePost">
      <label for="content">내용</label>
      <input type="text" id="content" v-model.trim="content" />
      <label for="score">평점</label>
      <input type="number" id="score" v-model="score" />
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'MovieReviewDetailView',
  data() {
    return {
      content: '',
      score: 0,
    };
  },
  computed: {
    reviewId() {
      return this.$route.params.id; // Vue Router를 통해 reviewId를 받아옴
    },
    movieReview() {
      return this.$store.getters.movieDetail.reviews.find(review => review.id === parseInt(this.reviewId))
    },
    movieDetail() {
      return this.$store.getters.movieDetail
    }
  },
  methods: {
    updatePost() {
      const content = this.content;
      const score = parseInt(this.score);
      const movie = parseInt(this.movieDetail.id);
      console.log('movie 확인해')
      console.log(content, score, movie)
      axios.put(`http://127.0.0.1:8000/movies/review/${this.reviewId}/update/`, {
          content: content,
          score: score,
          movie: movie
          //이렇게 무비 정보 직접 시리얼라이저에 전달해도 됨.. ㅇㅇ
        }, {
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
        .then(response => {
          console.log(response)
          this.$store.dispatch('fetchMovieDetail', movie)
        })
        .catch(error => {
          console.error(error);
        });
        this.$router.replace({name: 'DetailView', params: {id: movie}})
    },
  }
};
</script>

<style>
/* 필요한 스타일링을 추가 */
</style>
