<template>
    <div>
      <div>
        <h2>영화 장르 설문조사</h2>
        <p>좋아하는 장르를 선택해주세요:</p>
        <div>
          <label v-for="genre in genres" :key="genre.id">
            <input type="checkbox" :value="genre.id" v-model="selectedGenres">
            {{ genre.name }}
          </label>
        </div>
        <button @click="submitSurvey">설문조사 제출</button> 
        
      </div>
    </div>
</template>

<script>
    import axios from 'axios';
    // const API_URL = 'http://127.0.0.1:8000'

    export default {
      data() {
        return {
          selectedGenres: [],
        };
      },
      mounted() {
        this.getGenres()
      },
      computed: {
        genres() {
          return this.$store.getters.genres
        },
        token(){
          return this.$store.getters.token
        }
      },
      methods: {
        getGenres() {
          // API를 통해 장르 목록을 가져오는 비동기 함수 호출
          this.$store.dispatch('fetchGenres')
        },
        submitSurvey() {
          // 사용자가 선택한 장르 목록을 백엔드로 전송하는 비동기 함수 호출
          // 예를 들면 axios.post('/api/survey', { genres: this.selectedGenres }) 등
          // this.$store.dispatch('submitSurvey', this.selectedGenres, this.token)
          // console.log(this.token)
          // console.log(this.selectedGenres)
          axios.post('http://127.0.0.1:8000/polls/createpoll/', this.selectedGenres, {
            headers: {
              Authorization: `Token ${this.token}`
            },
          })
          .then(() => {
            alert('설문이 제출되었습니다.')
            
          })
          .catch(error => {
              console.log(error)
          })
        },
        // getRecommend(){
        //   axios
        //   .get(`${API_URL}/polls/recommend/`, {
        //     headers: {
        //       Authorization: `Token ${this.token}`
        //     },
        //   }).then(res => {
        //     console.log(res)
        //   }).catch(err => [
        //     console.log(err)
        //   ])
        // },
      }
    };
</script>
  