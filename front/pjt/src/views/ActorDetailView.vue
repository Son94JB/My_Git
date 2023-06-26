<template>
  <div>
    <h1>{{actorDetail.name}}</h1>
    <img v-if="actorDetail.profile_path" :src="`https://image.tmdb.org/t/p/w500/${actorDetail.profile_path}`" alt="actor profiel" />
    <!-- 출연작 리스트 -->
    <div>
      <h2>출연작</h2>
      <div v-for="movie in actorDetail.movies" :key=movie.title>
        <img @click="toMovieDetail(movie)" v-if="movie.poster" :src="`https://image.tmdb.org/t/p/w500/${movie.poster}`" alt="movie poster" />
        <p>{{ movie.title }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'ActorDetailView',
    created() {
        this.$store.dispatch('fetchActorDetail', this.$route.params.id);
    },
    computed: {
        actorDetail() {
            return this.$store.getters.actorDetail;
        },
    },
    methods: {
      toMovieDetail(movie){
        this.$router.push(`/detail/${movie.id}`);
        this.$store.dispatch('fetchMovieDetail', movie.id);
      }
    }
}
</script>

<style>

</style>