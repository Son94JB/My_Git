<template>
  <div class="article-list">
    <p>여기는 ArticleList입니다.</p>
    <ArticleListItem v-for="article in articles"
    :key="article.id"
    :article="article"
    />
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem.vue'

export default {
  name: 'ArticleList',  // 게시글 목록

  created() {
    this.getArticles()
  },

  methods: {
    getArticles() {
        this.$store.dispatch('getArticles')
    },
  },
  components: {
    ArticleListItem,
  },
  computed: {
    articles(){
      return this.$store.state.articles
    }
  },
}
</script>

<style>
.article-list {
  text-align: start;
}
</style>

