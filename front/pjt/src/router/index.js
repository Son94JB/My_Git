import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ArticleView from '@/views/ArticleView.vue'
import SearchView from '@/views/SearchView.vue'
import ArticleCreate from '@/views/ArticleCreate.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import DetailView from '@/views/DetailView.vue'
import store from '@/store'
// import store from  '@/store/index.js'
import ActorDetailView from '@/views/ActorDetailView.vue'
import DirectorDetailView from '@/views/DirectorDetailView.vue'
import MovieReviewDetailView from '@/views/MovieReviewDetailView.vue'
import RecommendView from '@/views/RecommendView.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView,
  },

  {
    path: '/article',
    name: 'ArticleView',
    component: ArticleView,
  },
  
  {
    path: '/movies/:id',
    name: 'SearchView',
    component: SearchView
  },

  {
    path: '/create',
    name: 'ArticleCreate',
    component: ArticleCreate
  },
  {
    path: '/update/:id',
    name: 'ArticleUpdate',
    component: () => import("@/views/ArticleUpdate"),
  },
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView,
    beforeEnter(to, from, next){
      if (store.getters.isLogin === true) {
        alert('이미 로그인 되어있습니다. \n먼저 로그아웃을 해주세요.')
        next(from)
      }else{
        next()
      }
    }
  },

  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView,
    beforeEnter(to, from, next){
      if (store.getters.isLogin === true) {
        alert('이미 로그인 되어있습니다. \n먼저 로그아웃을 해주세요.')
        next(from)
      }else{
        next()
      }
    }
  },

  {
    path: '/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView,
    beforeEnter(to, from, next){
      if (store.getters.isLogin != true) {
        alert('게시글을 보려면 로그인을 해주세요')
        next(false)
      }else{
        next()
      }
    },
  },

  {
    path: '/detail/:id',
    name: 'DetailView',
    component: DetailView
  },

  {
    path: '/actor/:id',
    name: 'ActorDetailView',
    component: ActorDetailView
  },

  {
    path: '/director/:id',
    name: 'DirectorDetailView',
    component: DirectorDetailView
  },

  {
    path: '/moviereivew/:id',
    name: 'MovieReviewDetailView',
    component: MovieReviewDetailView
  },

  {
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  duplicateNavigationPolicy: 'ignore', // 중복 네비게이션 경고 비활성화

})

// router.beforeEach((to, from, next) => {
//   // 검색 정보 초기화
//   store.dispatch('resetSearchTerm');
//   next();
// })



export default router
