<template>
  <div>
    <h4>{{ article.id }}</h4>
    <p>{{ article.title }}</p>
    <p>작성자 : {{ article.username }}</p>
      <router-link 
        :to="{
          name: 'ArticleDetailView',
          params: {id: article.id },
          }" 
          >
          [DETAIL]
        </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem', // 각 게시물을 나타낼 vue파일
  props: {
    article: Object
  },
  methods: {

  }
}
</script>

<style>

</style>