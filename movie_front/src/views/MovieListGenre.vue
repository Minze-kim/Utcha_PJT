<template>
    <div>
        <h1>{{genre}}</h1>
        <!-- <MovieList/> -->
        <p v-if="movies.length === 0">영화가 없습니다.</p>
        <div class="container">
            <div class="row">
                    <MovieListItem :movie="movie" v-for="movie in movies" :key="movie.id" />
                        <!-- <div v-for="movie in movies" :key="movie.id"> -->
                            <!-- <img class="col" v-bind:src="'https://image.tmdb.org/t/p/w185/'+ movie.poster_path " alt="posterUrl"> -->
                        <!-- </div> -->
            </div>
        </div>
    </div>
</template>

<script>

const BACKEND_URL = 'http://127.0.0.1:8000/movies/'

import axios from 'axios'
import MovieListItem from '../components/movies/MovieListItem.vue'

export default {
    name:'MovieListGenre',
    components:{
        MovieListItem,
    },

    data(){
        return{
            movies:[],
        }
    },
    props: {
        id: Number,
        genre: String
    },
    methods:{
        getMovies(){
            axios.get(BACKEND_URL + this.id + "/")
                .then(response => {
                    this.movies = response.data
                })
                .catch(err => console.log(err.response.data))
        },
    },
    mounted() {
        this.getMovies()
    },
    watch: {
        id: function() {
            axios.get(BACKEND_URL + this.id + "/")
                .then(response => {
                    this.movies = response.data
                })
        }
    }
}

</script>

<style>

</style>