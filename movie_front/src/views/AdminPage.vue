<template>
  <div>
      <router-link v-bind:to="{ name: 'CreateMovie'}">영화 생성</router-link><br>
      <router-link v-bind:to="{ name: 'ModifyMovie'}">영화 수정</router-link><br>
      <router-link v-bind:to="{ name: 'DeleteMovie'}">영화 삭제</router-link>
      <router-view/>
  </div>
</template>

<script>

export default {
    name: 'AdminPage',

}
</script>

<style>

</style>