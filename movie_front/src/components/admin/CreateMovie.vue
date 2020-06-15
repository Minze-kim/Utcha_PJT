<template>
  <div>
    <form v-on:submit.prevent="createMovie">
      <p>새로운 영화 등록</p>
      <div class="form-group">
        <label for="title">영화 제목</label>
        <input type="text" id="title" class="form-control" v-model="movieDetail.title">
      </div>
      <label for="original-title">영화 원제목</label>
      <input type="text" id="original-title" v-model="movieDetail.original_title">
      <label for="release-date">개봉일</label>
      <input type="date" id='release-date' v-model="movieDetail.release_date"><br>
      <label for="genre">장르선택</label><br>
      <span v-for="genre in genres" v-bind:key="genre.id">
        <label v-bind:for="genre.genre_name">{{ genre.genre_name}}</label>
        <input type="checkbox"  
          v-bind:value="genre.id"
          v-model="movieDetail.genres_ids">
      </span><br>
      
      <label for="adult">관람등급</label>
      <select v-model="movieDetail.adult">
        <option disabled value="">관람등급을 선택해주세요.</option>
        <option v-for="option in adultOptions" 
        v-bind:key="option.id" 
        v-bind:value="option.value">
          {{ option.grade }}
        </option>
      </select><br>
      <label for="overview">줄거리</label>
      <textarea id="overview" v-model="movieDetail.overview" placeholder="줄거리를 입력해주세요"></textarea><br>
      <label for="poster-path">포스터 url</label>
      <input type="text" id="poster-path" v-model="movieDetail.poster_path">
      <input type="submit" class="btn btn-primary" value="새로운영화 생성">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const BACKEND_URL = "http://127.0.0.1:8000/"

export default {
    name: 'CreateMovie',
    data() {
      return {
        movieDetail: {
          title: null,
          original_title: null, 
          release_date: null, 
          genres_ids: [], //require array
          adult: null, 
          overview: null, 
          poster_path: null,  
        },

        adultOptions: [
          { grade: '18' , value: true},
          { grade: '15' , value: false},
          { grade: '12' , value: false},
          { grade: '전체관람가' , value: false},
        ],
        
        genres: []
      }
    },
    methods: {
      createMovie() {
        axios.post(BACKEND_URL + 'movies/add_movie/', this.movieDetail)
        .then(response=>{
          console.log(response.data)
          alert(response.data.title + '가 성공적으로 추가되었습니다.')
        })
        
      },
      getGenres() {
        axios.get(BACKEND_URL + 'movies/getgenres/')
        .then(response => {
          this.genres = response.data
          console.log(this.genres)
        })
      }
    },
    created(){
      this.getGenres()
    }
    
}
</script>

<style>
#title {
  width: 100px;
}

form {
  text-align: left;
}
</style>