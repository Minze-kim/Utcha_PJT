<template>
  <div>
    <h3>Create</h3>
    <div>
      <label for="title">title:</label>
      <input v-model="reviewData.title" type="text" id="title">
    </div>

    <div class="form-group">
      <label for="exampleFormControlSelect1">Example select</label>
      <select v-model="reviewData.rank" class="form-control" id="exampleFormControlSelect1">
        <option>1</option>
        <option>2</option>
        <option>3</option>
        <option>4</option>
        <option>5</option>
      </select>
    </div>
    <div>
      <label for="content">content:</label>
      <textarea v-model="reviewData.content" type="text" id="content"></textarea>
    </div>
    <button @click="createReview">작성</button>
  </div>

</template>

<script>
import axios from 'axios'
const BACKEND_URL='http://127.0.0.1:8000/'
export default {
    name:'CreateReview',
    data(){
      return{
        reviewData:{
          title:null,
          content:null,
          rank:Number,
        }
      }
    },
    props:{
      id:Number,
    },
    methods:{
      createReview(){
        const config ={
          headers:{
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
      axios.post(BACKEND_URL + 'reviews/create/' + this.id + '/', this.reviewData, config)
        .then(()=> {
          this.$router.push({ name: 'ReviewList' })
        })
      }
    }
}
</script>

<style>

</style>