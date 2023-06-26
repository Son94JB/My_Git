<template>
  <div>
    <!-- 검색결과가 있다면 검색결과 출력 그렇지 않다면 검색결과가 없습니다 출력 -->
    <p v-if="movieList.length > 0" class="search-result">검색결과</p>
    <p v-else class="no-results">검색결과가 없습니다.</p>
    <SearchListItem 
    v-for="movie in movieList" :key="movie.id" :movie="movie"
    />
  </div>
</template>

<script>
import SearchListItem from '@/components/SearchListItem.vue'
export default {
    name: 'SearchList', // 검색 결과 목록
    components: {
        SearchListItem,
    },
    props: {
      movieList: {
      type: Array,
      default: () => ([]),
  },
},

}
</script>

<style>

</style>