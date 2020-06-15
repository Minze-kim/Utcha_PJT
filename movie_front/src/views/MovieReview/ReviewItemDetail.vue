<template>
  <div>
      <div class="jumbotron">
        <h5 class="badge badge-pill badge-light user_name">{{ review.user.username }}님의 리뷰</h5>
        <span class="badge badge-info">{{ review.rank }}</span>

        <h1 class="display-4">{{ review.title }}</h1>
        <p class="lead">{{ review.content }}</p>
        
        <div v-if="review.user.id == currentUser">
            <span><button class="btn btn-outline-info my-2 my-sm-0" @click="modifyReview(review)" type="button">글수정</button></span>
            <span><button class="btn btn-outline-info my-2 my-sm-0" @click="deleteReview(movieId)" type="button">글삭제</button></span>
        </div>
        <hr class="my-4">
        <!-- 댓글기능 -->
          <div>
            <h5 class="text-left">댓글</h5>
            <hr>
            <ul v-for="(comment,index) in comments" :key="comment.id">
                <li v-text="comment.content">
                </li>
                <span><button v-if="comment.user == currentUser" @click="deleteComment(comment.id,index)">삭제</button></span>
                
            </ul>
          </div>
        <hr class="my-4">
            <input v-model="commentData.content" class="form-control mr-sm-2" type="text" placeholder="댓글을 작성하세요:)">
            <span><button class="btn btn-outline-info my-2 my-sm-0" @click="createComment" type="button">작성</button></span>
            

      </div>
  </div>
</template>

<script>
import axios from 'axios'
const BACKEND_URL='http://127.0.0.1:8000/'

export default {
    name: "ReviewItemDetail",
    props:{
        id:Number,
        movieId:Number,
    },
    data(){
        return{
          review:{
              "title":null,
              "cotent":null,
              "id":Number,
              "rank":Number,
              "user":{
                  "id":Number,
                  "username":null,
              }
          },
          commentData: {
                content: null,
                id:Number,
                movie_id:Number,
                user:Number,
          },
          comments: [],

          userValidation: false,
          currentUser: null,

        }
    },

    methods:{
        getReview(){
        axios.get(BACKEND_URL+'reviews/get_review/'+ this.id + '/')
            .then(response => {            
            this.review = response.data
            })
        },
        createComment() {

        const config={
            headers:{
                'Authorization' : `Token ${this.$cookies.get('auth-token')}`
            }
        }
        if (this.commentData.content){
            axios.post(BACKEND_URL + 'reviews/create_comment/' + this.id+ '/', this.commentData, config)
                
                .then(response => {
                console.log(response.data)
                this.comment = response.data
                this.comments.push(this.comment)
                this.commentData.content=''
                })
            }

        },
        modifyReview(data) {
            this.$router.push({ name:'ReviewItemModify', params:{ review:data}})
        },
        deleteReview() {
            axios.post(BACKEND_URL + 'reviews/delete/' + this.id+ '/')
                .then(() => {
                    alert('게시물 삭제가 완료되었습니다 :)')
                    this.$router.go(-1)
                    // this.$router.push({ name: 'ReviewList'})
                })
      },
      getComment() {
    
        axios.get(BACKEND_URL + 'reviews/get_comments/' + this.id +'/')
            .then(response => {
                this.comments = response.data
            })
      },
      validateUser() {
          const config = {
            headers:{
                'Authorization' : `Token ${this.$cookies.get('auth-token')}`
            }
        }
          axios.get(BACKEND_URL + 'rest-auth/user/', config)
          .then(response=>{
              if (response.data.username === this.review.user.username) {
                  this.userValidation = true
              }
          })
        },
        deleteComment(commentId,index){
                    console.log(this.commentData.id)
        axios.delete(BACKEND_URL + 'reviews/delete_comment/' + commentId + '/')
            .then(() => {
                alert('댓글이 삭제되었습니다 :)')

            })
        this.comments.splice(index, 1)
        },
        commentUserValidation() {
            const config = {
                headers:{
                    'Authorization' : `Token ${this.$cookies.get('auth-token')}`
                }
            }
            axios.get(BACKEND_URL + 'rest-auth/user/', config)
            .then(response=>{
                this.currentUser = response.data.id
                }
            )
        }
    },


    mounted(){
      this.getReview()
      this.getComment()
      this.validateUser()
      this.commentUserValidation()
    },
    created() {
        // this.validateUser()
        // this.commentUserValidation()
    }
}
</script>

<style>
.user_name{
  font-size: 20px;
  margin: 0 0 50px 0;
}

</style>