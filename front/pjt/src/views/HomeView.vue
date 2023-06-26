<template>
  <div>
    <h1>MOVIE.gg</h1>
    <SearchBar/>
  </div>
  
</template>

<script>
import SearchBar from '@/components/SearchBar.vue'; // SearchBar 컴포넌트를 불러옴

export default {
  name: 'HomeView',
  components: {
    SearchBar,
  },
  computed: {
    // movieList를 통해 vuex의 state에 getters로 접근
    movieList() {
      return this.$store.getters.Movies;
    }
  },
  
}
</script>

<style>

</style>