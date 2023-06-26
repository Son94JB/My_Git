<template>
  <div>
    <h2>Comments</h2>
        <ul v-if="comments.length > 0">
          <li v-for="comment in comments" :key="comment.id">
            <div>

              <template v-if="selectedComment !== comment.id">
                {{ comment.content }}
                <div> <button @click="editComment(comment)">수정</button> | 
                <button @click="deleteComment(comment.id)">삭제</button> </div>
              </template>

              <template v-else>
                <textarea cols="100" rows="2" v-model="editedComment" type="text"></textarea>
                <div>
                  <button @click="updateComment(comment.id)">저장</button> |
                  <button @click="cancelEdit">취소</button>  
                  <!-- cancel하면 content는 원래 있던 content로 돌리고 selectedComment를 null로 바꾸면 될 듯 -->
                </div>
              </template>
            </div>
          </li>
        </ul>
        
        <p v-else>댓글이 없습니다.</p>
        <form @submit.prevent="createComment">
          <label for="content">content : </label>
          <textarea id="content" cols="100" rows="10" v-model="content"></textarea><br>
          <input type="submit" value="작성">
        </form>



  </div>
</template>

<script>
import axios from 'axios'
import { mapActions, mapState } from 'vuex';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentList',
  props: {
    article: {
      type: Object,
      required: true
    },
  },
  data() {
    return {
      content: '',
      comments: [],
      editedComment: '',
      selectedComment: null,
      edting: false,
    }
  },
  computed:{
    ...mapState(['userDetail']),
  },
  created() {
    const articleId = this.article.id
    this.fetchComments(articleId);
    this.getUserName()
  },
  watch: {
    article: {
      immediate: true,
      handler(article){
        if(article){
          const articleId = article.id
          this.fetchComments(articleId)
        }
    }
  },
  },
  methods: {
    ...mapActions(['getUserName']),
    fetchComments() {
      // 해당 게시글의 댓글을 가져오는 API 호출
      axios.get(`${API_URL}/api/v1/comments/${this.$route.params.id}/`)
      .then(response => {
        this.comments = response.data;
      })
      .catch(error => {
        if(error.response && error.response.status === 404){
        this.comments = []
        }
        else{
          console.error(error)
        }
      })
    },

    createComment(){
      if(this.editing){
        alert('수정작업을 먼저 완료해주세요')
      }else{
      this.getUserName()
      const content = this.content
      const userId = parseInt(this.userDetail.pk)

      axios.post(`${API_URL}/api/v1/comments/${this.$route.params.id}/`, {
        user: userId,
        content: content,
      }, {
      headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then(res => {
        const newComment = res.data
        this.comments.push(newComment)
        this.content = ''
      })
      .catch(err => {
        console.log(err)
      })
      }
    },


    deleteComment(comment_id){
      axios
      .delete(`${API_URL}/api/v1/comments/change/${comment_id}/`,{
      headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then(() => {
        this.comments = this.comments.filter(comment => comment.id !== comment_id)
        alert('댓글이 삭제되었습니다')
      })
      .catch(err => {
        alert('자신의 댓글만 삭제 가능합니다!')
        console.log(err)
      })
    },

    editComment(comment) {
      this.editing = true
      this.getUserName()
      if (comment.user === this.userDetail.pk){
        this.selectedComment = comment.id;
        this.editedComment = comment.content;
      }else{
        alert('자신의 댓글만 수정이 가능합니다.')
      }
    },

    updateComment(comment_id){
      this.getUserName()
      const content = this.editedComment
      const userId = parseInt(this.userDetail.pk)

      axios
      .put(`${API_URL}/api/v1/comments/change/${comment_id}/`, {
        user: userId,
        content: content
      }, {
      headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      }).then(() => {
          const updatedComment = this.comments.find(comment => comment.id === comment_id);
          if (updatedComment) {
            updatedComment.content = content;
          }
          this.cancelEdit();
        })
        .catch(err => {
          console.log(err);
        });
    },

    cancelEdit() {
      this.selectedComment = null;
      this.editedComment = '';
    },

  },
}
</script>
  