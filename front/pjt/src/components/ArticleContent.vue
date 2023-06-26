<template>
  <div>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성자 : {{ article?.username }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    <button @click="onClickDelete">DELETE</button>
    <button @click="onClickUpdate">UPDATE</button>
    <!-- <router-link class="temp" :to="{name:'ArticleUpdate', params:{id:this.article.id} }" @click="onClickUpdate">수정하기</router-link> -->
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions, mapState } from 'vuex'
const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'ArticleContent',  // 게시글 내용
  props:{
    article: Object,
  },
  created(){
    this.getArticles()
    this.getUserName()
  },
  computed:{
    ...mapState(['userDetail']),
  },

  methods:{
    ...mapActions(['getUserName']),

    getArticles() {
        this.$store.dispatch('getArticles')
    },
    onClickDelete(){
      // console.log(this.$store.state.articles)
      axios.delete(`${API_URL}/api/v1/articles/${this.article.id}/`, {
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then((res) => {
        this.$emit('delete-success'),
        alert('삭제 완료되었습니다!!', res)
        this.$router.push({ name: 'ArticleView'});
      })
      .catch((err) => {
        alert('자신의 게시물만 삭제 가능합니다!');
        console.log(err);
      })
    },
    onClickUpdate(event) {
      event.preventDefault();
      if (this.article.username !== this.userDetail.username){
        alert('작성자만 수정할 수 있습니다!');
      }else{
        this.$router.push({ name: 'ArticleUpdate', params: { id: this.article.id } });
      }
    },
  },
}

</script>

<style scoped>
.temp{
  text-decoration-line:none;
}
.temp:hover{
  color: aqua;
}
.temp:visited{
  color: violet;
}
</style>