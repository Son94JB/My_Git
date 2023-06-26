<template>
  <div>
    <h1>영화 추천</h1>
    <MovieRecommend v-if="!polled"/>
    <showRecommend @childEvent="handleChildEvent"/>
  </div>
</template>

<script>
import MovieRecommend from '@/components/MovieRecommend.vue'
import showRecommend from '@/components/showRecommend.vue'

export default {
  name: 'RecommendView',
  data(){
    return{
      polled: false,
    }
  },
  components: {
    MovieRecommend,
    showRecommend,
  },
  methods: {
    handleChildEvent(){
      this.polled = true
    }
  },
}
</script>

<style>

</style>