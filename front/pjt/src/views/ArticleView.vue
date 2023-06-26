<template>
  <div>
    <h1>Article List</h1>
    <router-link :to="{ name: 'ArticleCreate' }">글쓰기</router-link>
    <hr>
    <!-- <BestArticleList/> -->
    <ArticleList/>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'
// import BestArticleList from '@/components/BestArticleList.vue'

export default {
  name: 'ArticleView',
  components: {
    // BestArticleList,
    ArticleList,
  },
}
</script>

<style>

</style>
