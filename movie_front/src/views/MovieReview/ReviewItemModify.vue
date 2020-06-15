<template>
  <div>
    <h3>Update</h3>
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
    <button @click="modifyReview">수정완료</button>
  </div>

</template>

<script>
import axios from 'axios'
const BACKEND_URL='http://127.0.0.1:8000/'

export default {
    name:"ReviewItemModify",
    props:{
        // review:Object,
        id:Number,
    },
    data(){
        return{
            reviewData: {
                "title":null,
                "content":null,
                "rank":Number,

                // "id":this.id
                // user:{

                // }
            },
            // modifyData:{
            //     "title":null,
            //     "content":null
            //     // id:Number
            //     // user:{
            //     // }
            // }
        
        }
    },


    methods:{
        getReview(){
        axios.get(BACKEND_URL+'reviews/get_review/'+ this.id + '/')
            .then(response => {            
            this.reviewData = response.data
            })
        },
        modifyReview(){
            const config ={
                headers:{
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
            }
            }
            axios.put(BACKEND_URL + 'reviews/modify/' + this.id + '/', this.reviewData, config)
                .then(() => {
                    alert('수정이 완료되었습니다 :)')
                    this.$router.go(-1)
                    // this.$router.push({ name: 'ReviewList' })
            })
        }

    },
    mounted(){
      this.getReview()
    }
    
}
</script>


<style>

</style>