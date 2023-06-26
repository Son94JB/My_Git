<template>
  <div>
    <ArticleContent :article="article"
    @delete-success="toUpdatedList"
    /><hr>
    <CommentList :article="article"/><hr>
    <router-link :to="{ name: 'ArticleView' }">목록으로</router-link>
    <ArticleList/>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

import ArticleContent from '@/components/ArticleContent.vue'
import ArticleList from '@/components/ArticleList.vue'
import CommentList from '@/components/CommentList.vue'

export default {
  name: 'ArticleDetailView',
  components:{
    // 3개 필요. 게시글 내용이랑 댓글이랑 다른 게시글 목록
    ArticleContent,
    ArticleList,
    CommentList,
  },
  created() {
    const articleId = this.$route.params.id
    this.fetchArticle(articleId)

  },
  data() {
    return {
      article: {
        id: null,
        title: '',
        content: '',
      }
    }
  },
  // computed : {
  //   loadedArticle(){
  //     return this.article
  //   }
  // },
  methods: {
    fetchArticle(id){
      axios.get(`${API_URL}/api/v1/articles/${id}/`)
      .then(res => {
        this.article = res.data
      }).catch(err => {
        console.log(err)
      })
    },
    toUpdatedList(){
      this.$router.push({name: 'ArticleView '})
    },
    testMethod(){
      axios.get(`${API_URL}/api/v1/test/`, {
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      }).then(res => {
        console.log(res)
      }).catch(err => {
        console.log(err)
      })
    },
  },
  beforeRouteUpdate(to, from, next){
    this.fetchArticle(to.params.id)
    next()
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth'
      })
  },
}
</script>

<style>

</style>