<template>
  <div>
      <h1>Signup</h1>
            <div>
                <label for="username">아이디</label>
                <input v-model="signupData.username" type="text" id="username">
            </div>
            <!-- <div>
                <label for="email">이메일</label>
                <input v-model="signupData.email" type="email" id="email">
            </div> -->
            <div>
                <label for="password1">비밀번호</label>
                <input v-model="signupData.password1" type="password" id="password1">
            </div>
            <div>
                <label for="password2">비밀번호</label>
                <input v-model="signupData.password2" type="password" id="password2">
            </div>
            <button @click="signup">확인</button>

  </div>
</template>

<script>
export default {
    name:'Signup',
    data() {
        return {
            signupData: {
                username: null,
                //email:null,
                password1: null,
                password2: null,
            }
        }
    },
    methods: {
       signup() {
        this.$emit('save-signup-data', this.signupData)
       }
    },
}
</script>

<style>

</style>