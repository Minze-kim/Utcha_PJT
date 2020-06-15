<template>
    <div>
        <h5>{{ movie.title }}</h5>
        <a
        data-toggle="modal"
        v-bind:data-target="dataTarget" >
            <img class="posterimg" 
            v-bind:src="'https://image.tmdb.org/t/p/w342/'+ movie.poster_path "
            alt="posterUrl">
        </a>
        
        <div class="modal fade" 
        :id="movieId" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">{{ movie.title }}</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <img class="img-fluid poster-url" :src="'https://image.tmdb.org/t/p/w185/'+ movie.poster_path " alt="poster-url">
                <hr>
                <!-- <h3 class="badge badge-info">{{ ㅠ}}</h3> -->
                <p v-text="movie.overview"></p>
                <hr>
                <ul v-for="(comment,index) in comments" :key="comment.id">
                    <li v-text="comment.content"></li>
                    <span><button v-if="comment.user == currentUser" @click="deleteComment(comment.id,index)">삭제</button></span>

                </ul>
                <input type="text" v-model="commentData.content" required>
                <span><button @click="createComment" type="button">작성</button></span>
        
            </div>

            <div class="modal-footer">
                <router-link :to="'/moviereview/'+movie.id"
                
                class="btn btn-success"
                data-dismiss="modal"
                :movie="movie ">상세리뷰</router-link>
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <!-- <button v-if="!isLoggedIn" disabled>상세리뷰를 보려면 로그인해주세요</button> -->
            </div>
            </div>
        </div>
        </div>
    </div>
</template>

<script>
const BACKEND_SERVER = 'http://127.0.0.1:8000/'
import axios from 'axios'

export default {
    name: 'MovieListItemModal',
    props: {
        movie: Object,
    },
    data(){
        return {
            commentData: {
                content: null,
                id:Number,
                movie_id:Number,
                user:Number,
            },
            comments: [],
            isLoggedIn: false,
            currentUser: null,
        }
    },
    computed: {
        movieId() {
            return 'movie'+this.movie.id
        },
        dataTarget() {
            return `#movie${this.movie.id}`
        }
    },
    methods: {
        getComment() {
            axios.get(BACKEND_SERVER + 'movies/get_comments/' + this.movie.id +'/')
            .then(response => {
                this.comments = response.data
            }
        )
        },

        createComment() {
            const config={
                headers:{
                    'Authorization' : `Token ${this.$cookies.get('auth-token')}`
                }
            }
            if (this.commentData.content){
                // 빈 댓글 입력안하기
                // 유저 정보 가져와야하는데.. 'serializer로 유저가 안넘어옴!!ㅠㅠ'
                axios.post(BACKEND_SERVER + 'movies/create_comment/' + this.movie.id + '/', this.commentData, config)
                .then(response => {
                    this.comment = response.data
                    this.comments.push(this.comment)
                    // 작성후 없어지게하기
                    this.commentData.content=''
                })
            }
            //this.getComment()
        },

        deleteComment(commentId,index){
            axios.delete(BACKEND_SERVER + 'movies/delete_comment/' + commentId + '/')
            .then(() => {
                alert('댓글이 삭제되었습니다 :)')
            })
            this.comments.splice(index, 1)
        },
        // validateUser() {
        //     const config = {
        //         headers:{
        //             'Authorization' : `Token ${this.$cookies.get('auth-token')}`
        //         }
        //     }
        //     axios.get(BACKEND_SERVER + 'rest-auth/user/', config)
        //     .then(response=>{
        //         if (response.data.username === this.user.username) {
        //             this.userValidation = true
        //         }
        //     })
        //},
        UserValidation() {
            const config = {
                headers:{
                    'Authorization' : `Token ${this.$cookies.get('auth-token')}`
                }
            }
            axios.get(BACKEND_SERVER + 'rest-auth/user/', config)
            .then(response=>{
                this.currentUser = response.data.id
                this.isLoggedIn = true
                }
            )
        }
    },
    mounted(){
        this.getComment()
        // this.validateUser()
        this.UserValidation()
    },
    created(){
        // this.UserValidation()
        // this.getComment()
    },
    // computed:{
    //     comments: function() {
    //         axios.get(BACKEND_SERVER + 'movies/get_comments/' + this.movie.id +'/')
    //         .then(response => {
    //             return this.comments = response.data
    //         }
    //     )
    //     }
    // }
  
}
</script>

<style>
    img.poster-url {
        width: 100%;
    }
</style>