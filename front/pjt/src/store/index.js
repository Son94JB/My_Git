import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'
Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],
  state: {
    articles:[],
    token: '',
    movies: [],
    movieDetail: null,
    searchTerm: '',  // 검색어
    actorDetail: null,
    directorDetail: null,
    genres: [],
    poll: null,
    // movieReviewDetail: null,
    // userDetail: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
    Movies(state) {
      return state.movies
    },
    movieDetail(state) {
      return state.movieDetail
    },
    actorDetail(state) {
      return state.actorDetail
    },
    directorDetail(state) {
      return state.directorDetail
    },
    genres(state) {
      return state.genres
    },
    poll(state) {
      return state.poll
    },
    token(state) {
      return state.token
    },
    // movieReviewDetail(state) {
    //   return state.movieReviewDetail
    // },
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    // signup & login 같이 이걸로
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'ArticleView'}) // store/index.js $router 접근 불가 -> import를 해야함
    },
    // SIGN_UP(state, token){
    //   state.token = token
    // },
    DELETE_TOKEN(state){
      state.token = ''
    },
    SET_MOVIES(state, movies) {
      state.movies = movies
      console.log(state.movies)
    },
    // detail은 fetchMovieDetail에서 받아온 response.data
    setMoviedetails(state, detail) {
      state.movieDetail = detail
      console.log(state.movieDetail)
    },
    RESET_SEARCH_DATA(state) {
      state.searchTerm = ''
      state.movies = []
      state.movieDetail = null
      console.log(state.searchTerm)
    },
    setActorDetails(state, detail) {
      state.actorDetail = detail
    },
    setDirectorDetails(state, detail) {
      state.directorDetail = detail
    },
    SET_USER_DETAIL(state, userDetail) {
      state.userDetail = userDetail;
    },
    SET_SEARCH_TERM(state, searchTerm) {
      state.searchTerm = searchTerm
    },
    setGenres(state, genres) {
      state.genres = genres
    },
    setPoll(state, poll) {
      state.poll = poll
    },
    // setMovieReviewDetails(state, detail) {
    //   state.movieReviewDetail = detail
    //   console.log(state.movieReviewDetail)
    // },
    // DELETE_ARTICLE(state) {
    //   state.articles = 
    // },
  },
  // ====================================================================================
  // ====================================================================================
  actions: {

    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
      })
        .then(res => {
          context.commit('GET_ARTICLES', res.data)
        })
        .catch(err => {
        console.log(err)
      })
    },
    // ====================================================================================
    deleteToken(context){
      // axios({
      //   method: 'post',
      //   url: `${API_URL}/accounts/logout/`,
      //   headers: {
      //     Authorization: `Token ${context.state.token}`,
      //   }
      // }).then(res =>
        context.commit('DELETE_TOKEN')
      // ).catch(err => console.log(err))
    },
    // ====================================================================================
    searchMovies(context, searchTerm){
      console.log(searchTerm)
      context.commit('SET_SEARCH_TERM', searchTerm)
      axios.get(`http://127.0.0.1:8000/movies/${searchTerm}/`)
      .then(response => {
        context.commit('SET_MOVIES', response.data)
      })
      .catch(error => {
          console.log(error)
      })
    },
    // ====================================================================================
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username : username, 
          password1 : password1, 
          password2 : password2,
        }
      })
        .then((res) => {
          // console.log(res)
          // context.commit('SIGN_UP', res.data.key)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    // ====================================================================================
    logIn(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        })
      .catch((err) => {
        console.log(err)
        alert('아이디 혹은 비밀번호를 확인해주세요!')
      })
    },
    // ====================================================================================
    fetchMovieDetail(context, movieId) {
      axios.get(`http://127.0.0.1:8000/movies/detail/${movieId}/`)
      .then(response => {
        context.commit('setMoviedetails', response.data)
      })
      .catch(error => {
        console.log(error)
      })
    },
    fetchGenres(context) {
      axios.get('http://127.0.0.1:8000/polls/genre/')
      .then(response => {
        context.commit('setGenres', response.data)
      })
      .catch(error => {
        console.log(error)
      })
    },
    submitSurvey(context, payload, token) {
      axios.post('http://127.0.0.1:8000/polls/createpoll/', payload, {
        headers: {
          Authorization: `Token ${token}`
        },
      })
      .then(response => {
        context.commit('setPoll', response.data)
      })
      .catch(error => {
        console.log(error)
      })
    },

    // ====================================================================================
    resetSearchTerm(context) {
      context.commit('RESET_SEARCH_DATA', '');
    },
    // ====================================================================================
    fetchActorDetail(context, actorId) {
      axios.get(`http://127.0.0.1:8000/movies/actor/${actorId}/`)
      .then(response => {
        context.commit('setActorDetails', response.data)
      })
      .catch(error => {
        console.log(error)
      })
    },
    // ====================================================================================
    fetchDirectorDetail(context, directorId) {
      axios.get(`http://127.0.0.1:8000/movies/director/${directorId}/`)
      .then(response => {
        context.commit('setDirectorDetails', response.data)
      })
      .catch(error => {
        console.log(error)
      })
    },
    fetchUserInfo({commit, state}){
      return axios.get(`${API_URL}/accounts/user/`, {
        headers: {
          Authorization: `Token ${state.token}`
        }
      }).then(res => {
        const userInfo = res.data
        commit('SET_USER_INFO', userInfo)
        return userInfo
      }).catch(err => {
        console.lof(err)
      })
    },
    // fetchMovieReviewDetail(context, reviewId) {
    //   axios.get(`${API_URL}/movies/review/${reviewId}/`)
    //   .then(response => {
    //     context.commit('setMovieReviewDetails', response.data)
    //   })
    //   .catch(error => {
    //     console.log(error)
    //   })
    // },
    // ====================================================================================
    getUserName(context){
      // 해당 유저의 정보(토큰)도 같이 받아와서 그거에 맞는 userDetail을 가져와야 됨.
      const token = context.state.token

      axios.get(`${API_URL}/accounts/user/`, {
        headers: {
          Authorization: `Token ${token}`,
        }
      }).then(res => {
        const userDetail = res.data
        context.commit('SET_USER_DETAIL', userDetail)
      }).catch(err => {
        console.log(err)
      })
    },
    // ====================================================================================
  },
  
  modules: {
  },
})
