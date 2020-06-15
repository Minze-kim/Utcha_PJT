<template>
    <div class="modalitems">
        
        <a 
        data-toggle="modal"
        v-bind:data-target="dataTarget" >

            <div class="scale"><img class="posterimg" 
            v-bind:src="'https://image.tmdb.org/t/p/w342/'+ movie.poster_path "
            alt="posterUrl">
            <h5 id=" header" class="postertitle postercard-body">{{ movie.title }}</h5>

            </div>
            
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
                <h5 class="text-left text-bold">줄거리</h5>
                <p class="text-left" v-text="movie.overview"></p>
                <hr>
                <h5 class="text-left text-bold">유저 평점</h5>
                <ul v-for="(comment,index) in comments" :key="comment.id">
                    <li v-text="comment.content"></li>
                    <span><button v-if="comment.user == currentUser" @click="deleteComment(comment.id,index)">삭제</button></span>
                </ul>
                <hr>
                <div class="form-row">
                    <div class="col-8">
                        <input class="form-control" type="text" v-model="commentData.content" required>
                    </div>
                    <div class="col-4">
                        <button @click="createComment" class="btn btn-primary">댓글등록</button>
                    </div>
                </div>
        
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

<style scoped>
.modalitems{
    /* position:fixed; */
    /* top:100px; */
}

.scale {
  transform: scale(1);
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transition: all 0.5s ease-in-out;   /* 부드러운 모션을 위해 추가*/
}

.scale:hover .postertitle{
    opacity: 1;
    text-align: center;
    color:#ffff;

}
.posterimg:hover{
    opacity: 0.4;
}


.postertitle{
    position: relative;
    bottom: 200px;
    font-size: 27px;
    opacity:0;
}
.scale:hover {
  transform: scale(1.2);
  -webkit-transform: scale(1.2);
  -moz-transform: scale(1.2);
  -ms-transform: scale(1.2);
  -o-transform: scale(1.2);
  /* opacity: ; */
}
/* .scale:hover:after {
    opacity: 0;
} */
</style>