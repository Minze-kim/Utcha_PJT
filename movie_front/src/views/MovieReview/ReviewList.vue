<template>
  <div>
    <div v-if="isLoggedIn">
      <!-- <h3>{{ movie.id }}</h3> -->
      <!-- <div v-if="isLoggedIn"> -->
      <button @click="createReview">리뷰작성</button>
        <table class="table">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Title</th>
              <th scope="col">User</th>
              <th scope="col">상세보기</th>
            </tr>
          </thead>
          
          <ReviewListItem :movieId="movieId" :movie="movie" :reviews="reviews"/>

        </table>
    </div>
      <!-- </div> -->
      <!-- <div v-else> -->
        <!-- <p>로그인이 필요합니다 :)</p> -->
      <!-- </div> -->

  </div>
</template>

<script>
import axios from 'axios'
const BACKEND_URL = 'http://127.0.0.1:8000/'

import ReviewListItem from '../../components/reviews/ReviewListItem.vue'
export default {
    name:'ReviewList',
    components: {
      ReviewListItem,
    },
    props: {
      movie:Object,
      id: Number, //영화id
    },
    data(){
      return{
        // movie:Object,
        reviews:[],
        isLoggedIn:false,
        errorMessage:null,
        movieId:this.id,
      }
    },

    methods:{

      loginCheck() {
        if (this.$cookies.isKey('auth-token')){
          this.isLoggedIn = true
        } else{
          alert('로그인이 필요합니다 :)')
          this.$router.push({name:'Login'})
        }
        
      },

      setCookies(token){
        this.$cookies.set('auth-token',token)
        this.isLoggedIn=true
      },
      getReviews(){
        
        axios.get(BACKEND_URL + 'reviews/get_reviews/' + this.id )
          .then(response =>{
            console.log(response.data)
            this.reviews = response.data
          })
      },
      createReview(){
        this.$router.push({ name: 'CreateReview' ,params: {id:this.id}})
      }
    },
    mounted() {
      this.loginCheck()
      this.getReviews()

    }

}
</script>

<style>

</style>