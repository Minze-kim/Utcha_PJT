<template>
  <div>
      <h1>Login</h1>
          <div>
            <label for="username">아이디</label>
            <input v-model="loginData.username" type="text" id="username" >
          </div>
          <div>
            <label for="password">비밀번호</label>
            <input v-model="loginData.password" type="password" id="password" >
          </div>
          <button @click="login">확인</button>
  </div>

</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            loginData: {
                username: null,
                password: null,
            }
        }
    },
    methods: {
        login() {
            this.$emit('save-login-data', this.loginData)
        }
    }

}
</script>

<style scoped>
.form{
  text-align: left;
  margin: 20px auto;
  width:50%;
}

</style>