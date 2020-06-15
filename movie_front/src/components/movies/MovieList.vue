<template>
  <div>
    <!-- <button v-on:click="getMovieList">클릭!</button> -->
    <div class="container">
        <div  class='row ml-auto mr-auto movieList'>
            <div v-for="movie in movieList" v-bind:key="movie.id" class="row">
                <img class="col" v-bind:src="'https://image.tmdb.org/t/p/w185/'+ movie.poster_path " alt="posterUrl">
            </div>
        </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

const BACKEND_SERVER = 'http://127.0.0.1:8000/'
export default {
    data() {
        return {
            movieList: []
        }
    },
    methods: {
        getMovieList(){
            axios.get(BACKEND_SERVER + 'movies/')
            .then(response => {
                this.movieList = response.data
            })
        }
    },
    created(){
        this.getMovieList()
    }

}
</script>

<style scoped>


</style>