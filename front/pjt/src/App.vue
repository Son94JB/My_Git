<template>
  <div id="app">
    <nav>
      <p v-if="username">안녕하세요 {{ username }}님!</p>
      <router-link :to="{ name: 'HomeView' }">Home</router-link> | 
      <router-link :to="{ name: 'SearchView', params: { id: serachTerm } }">Search</router-link> |
      <router-link :to="{ name: 'ArticleView' }">Article</router-link> |  
      <router-link :to="{ name: 'LogInView' }">LogIn</router-link> |
      <router-link :to="{ name: 'SignUpView' }">SignUp</router-link> |
      <router-link :to="{ name: 'RecommendView' }">Recommend</router-link> |
    <button v-if="this.$store.state.token" @click="logOut">LogOut</button>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

<script>
import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'App',
  computed: {
    serachTerm(){
      return this.$store.state.searchTerm
    },
  },
  data(){
    return {
      username: null,
    }
  },
  created(){
    this.getUserName()
  },
  watch:{
    '$route'() {
      if (this.$store.state.token) {
        this.getUserName();
      } else {
        this.username = null;
      }
    }
  },
  methods:{
    logOut(){
      this.$store.dispatch('deleteToken')
      this.username = null
      alert('로그아웃')
      this.$router.push({name: 'LogInView'})
    },
    async getUserName(){
      axios.get(`${API_URL}/accounts/user/`, {
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      }).then(res => {
        this.username = res.data.username
      }).catch(err => {
        console.log(err)
      })
    },
  }
}
</script>
