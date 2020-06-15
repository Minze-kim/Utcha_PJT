<template>
  <div>
    <p v-if="!movieToModify">수정을 원하는 영화를 선택해주세요</p>
    <select v-model="movieToModify">
        <option v-for="movie in movies" :key="movie.id" :value="movie">
            {{ movie.title }}
        </option>
    </select>
    <div v-if="movieToModify">
        <p>수정중인 영화: {{ movieToModify.title }}</p>
        <form v-on:submit.prevent="modifyMovie">
            <label for="title">영화 제목</label>
            <input type="text" id="title" v-model="dataToModify.title">
            <label for="original-title">영화 원제목</label>
            <input type="text" id="original-title" v-model="dataToModify.original_title">
            <label for="release-date">개봉일</label>
            <input type="date" id='release-date' v-model="dataToModify.release_date"><br>
            <label for="genre">장르선택</label><br>
            <span v-for="genre in genres" v-bind:key="genre.id">
                <label v-bind:for="genre.genre_name">{{ genre.genre_name}}</label>
                <input type="checkbox"  
                v-bind:value="genre.id"
                v-model="dataToModify.genres_ids">
            </span><br>
            
            <label for="adult">관람등급</label>
            <select v-model="dataToModify.adult">
                <option disabled value="">관람등급을 선택해주세요.</option>
                <option v-for="option in adultOptions" 
                v-bind:key="option.id" 
                v-bind:value="option.value">
                {{ option.grade }}
                </option>
            </select><br>
            <label for="overview">줄거리</label>
            <textarea id="overview" v-model="dataToModify.overview"></textarea><br>
            <label for="poster-path">포스터 url</label>
            <input type="text" id="poster-path" v-model="dataToModify.poster_path">
            <input type="submit" value="수정하기"><br>
    </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const BACKEND_URL = "http://127.0.0.1:8000/"

export default {
    name: 'ModifyMovie',
    data() {
        return {
            movies: [],
            movieToModify: null,
            dataToModify: null,
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
        getMovieList() {
            axios.get(BACKEND_URL + 'movies/')
            .then(response=>{
                this.movies = response.data
            })
        },
        modifyMovie() {
            axios.put(BACKEND_URL + 'movies/modify_movie/' + `${this.movieToModify.id}/`, this.dataToModify)
            .then(response=>{
                alert(`${response.data.title} 의 정보가 성공적으로 수정되었습니다.`)
            })
            this.getMovieList()
        },
        getGenres() {
            axios.get(BACKEND_URL + 'movies/getgenres/')
            .then(response => {
            this.genres = response.data
            console.log(this.genres)
            })
            
        },
    },
    created() {
        this.getMovieList()
        this.getGenres()
    },
    watch:{
        movieToModify: function() {
            const originalData = {
                title: this.movieToModify.title,
                original_title: this.movieToModify.original_title, 
                release_date: this.movieToModify.release_date, 
                genres_ids: this.movieToModify.genres_ids, //require array
                adult: this.movieToModify.adult, 
                overview: this.movieToModify.overview, 
                poster_path: this.movieToModify.poster_path,  
            }
            this.dataToModify = originalData
        }
    }

}
</script>

<style>

</style>