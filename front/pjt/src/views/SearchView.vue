<template>
  <div>
    <SearchBar/>
    <!-- SearchList 컴포넌트에 movie-list라는 이름으로 전달 -->
    <!-- SearchList는 props로 받을 때 movieList로 받는 거임 -->
    <SearchList :movie-list="movieList"/> 
    <SearchListItem/>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue'; // SearchBar 컴포넌트를 불러옴
import SearchList from '@/components/SearchList.vue'; // SearchList 컴포넌트를 불러옴
import SearchListItem from '@/components/SearchListItem.vue'; // SearchListItem 컴포넌트를 불러옴

export default {
    name: 'SearchView',
    components: {
      SearchBar,
      SearchList,
      SearchListItem,
    },
    computed: {
      // movieList를 통해 vuex의 state에 getters로 접근
      movieList() {
          return this.$store.getters.Movies
      },
    },
}
</script>

<style>

</style>