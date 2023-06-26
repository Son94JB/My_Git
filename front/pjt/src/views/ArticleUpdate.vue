<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="updateArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model="article.title"><br>
      <label for="content">내용 : </label>
      <textarea 
        id="content" cols="30" rows="10"
        v-model="article.content"
        >
      </textarea><br>
      <input type="submit" id="submit">
    </form>
    <button @click="goBack">뒤로가기</button>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleUpdate',
  data(){
    return{
      article:{}
    }
  },
  created(){
    const articleId = this.$route.params.id
    axios
    .get(`${API_URL}/api/v1/articles/${articleId}/`, {
      headers: {
        Authorization: `Token ${this.$store.state.token}`,
      }})
      .then((res) => {
        this.article = res.data
      }).catch((err) => {
        console.log(err);
      });
    },
  methods:{
    initArticle(){
      this.article = this.$route.params.article;
    }
    ,
    updateArticle(){
      
      const { title, content } = this.article

      if (!title || !content){
        alert('제목과 내용을 둘 다 입력해주세요!!!!!!!!!!!!!!!!!!!!!')
        return;
      }

      axios
      .put(`${API_URL}/api/v1/articles/${this.article.id}/`, this.article, {
        headers:{
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        // console.log(res)
        alert('게시글 수정 완료!')
        this.$router.push(`/${this.$route.params.id}`)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goBack(){
      this.$router.push(`/${this.$route.params.id}`)
    }
  }
}
</script>

<style>

</style>