<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return{
      username: '',
      password1: '',
      password2: '',
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      if (!username) {
        alert('아이디를 입력해주세요')
      }else if (!password1) {
        alert('비밀번호를 입력해주세요')
      }else if (!password2) {
        alert('비밀번호를 확인해주세요')
      }

      const payload = {
        username, password1, password2
      }

      this.$store.dispatch('signUp', payload)
      this.$router.push({name:'HomeView'})
    }
  }
}
</script>
