<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="logIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="로그인">
    </form>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return{
      username: '',
      password: '',
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      if (!username) {
        alert('아이디를 입력해주세요')
      }else if (!password) {
        alert('비밀번호를 입력해주세요')
      }

      const payload = {
        username, password
      }
      this.$store.dispatch('logIn', payload)
    },
  },
}
</script>