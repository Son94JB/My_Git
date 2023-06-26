<template>
  <div>
    <input v-model="searchTerm" type="text" placeholder="영화 검색" />
    <button @click="searchMovies">검색</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchTerm: '', // 검색어를 저장할 데이터
    };
  },
  methods: {
    searchMovies() {
    // 현재 URL과 검색할 URL이 동일한지 확인
    if (this.$route.name === 'SearchView' && this.$route.params.id === this.searchTerm) {
    // 동일한 URL로의 네비게이션을 피하기 위해 return 문을 사용하여 함수 종료
      return;
    }

    // Vuex 액션 호출하여 검색 요청 보내기
    this.$router.replace({ name: 'SearchView', params: { id: this.searchTerm } });
    this.$store.dispatch('searchMovies', this.searchTerm);
    },
  },
};
</script>
