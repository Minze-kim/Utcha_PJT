<template>
  <div>
        <p v-if="!movieToDelete">삭제를 원하는 영화를 선택해주세요</p>
        <select v-model="movieToDelete">
            <option v-for="movie in movies" :key="movie.id" :value="movie">
                {{ movie.title }}
            </option>
        </select>
        <button v-if="movieToDelete" v-on:click="deleteMovie">삭제</button>
  </div>
</template>

<script>
import axios from 'axios'

const BACKEND_URL = "http://127.0.0.1:8000/"

export default {
    name: 'DeleteMovie',
    data() {
        return {
            movies: [],
            movieToDelete: null,
        }
    },
    methods: {
        getMovieList() {
            axios.get(BACKEND_URL + 'movies/')
            .then(response=>{
                this.movies = response.data
            })
        },
        deleteMovie() {
            const confimation = confirm(`${this.movieToDelete.title} 을 삭제하시겠습니까?`)
            if (confimation === true) {
                axios.delete(BACKEND_URL + `movies/delete_movie/${this.movieToDelete.id}/`)
                .then(response=>{
                    alert(`${response.data.title} 가 삭제되었습니다.`)
                })
                this.getMovieList()
            }
        }
    },
    created() {
        this.getMovieList()
    }
}
</script>

<style>

</style>