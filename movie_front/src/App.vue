<template>
  <div id="app">
    <div>
        <nav class="navbar navbar-expand-lg navbar-dark">
            <a class="logo navbar-brand" href="#">읏챠 플레이</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                    <span class="nav-item active">
                        <router-link class="homebtn nav-link" to="/">Home</router-link> 
                    </span>

                <div class='nav-item dropdown'>
                    <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    장르별 탐색
                    </button>
                    <div class="dropdown-menu">
                        <router-link v-for="genre in genres"
                        v-bind:key="genre.id"
                        v-bind:genre="genre.name"
                        :to="{ name: 'MovieListGenre', params: {id: `${genre.id}` } }">{{genre.name}}<br></router-link>
                    </div>
                </div>
                <span class="nav-item active">
                    <span class="nav-link" v-if="!isLoggedIn">
                        <router-link class="btn btn-light navitem" :to="{ name:'Signup' }">Signup</router-link> 
                        <router-link class="btn btn-light navitem" :to="{ name:'Login' }">Login</router-link>
                    </span>
                </span>
                <span class="nav-item active">
                    <span class="nav-link" v-if="isLoggedIn">
                        <router-link  class="btn btn-light" to="/accounts/logout" @click.native="logout">로그아웃</router-link>
                    </span>
                </span>
      </ul>
    </div>
    <router-link class="btn btn-light" v-if="isAdmin" to="/adminpage/" >관리자 페이지</router-link>  
  </nav>
  </div>
      <router-view @save-signup-data="signup" @save-login-data="login" />

      <!-- <router-link to="/">Home</router-link> |
        <span v-if="!isLoggedIn">
          <router-link :to="{ name:'Signup' }">Signup</router-link> |
          <router-link :to="{ name:'Login' }">Login</router-link>
        </span>
        
        <span v-if="isLoggedIn">
          <router-link to="/accounts/logout" @click.native="logout">로그아웃</router-link>
        </span>
        <div class='dropdown'>
          <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          장르별 탐색
          </button>
          <div class="dropdown-menu">
            <router-link v-for="genre in genres"
            v-bind:key="genre.id"
            v-bind:genre="genre.name"
            :to="{ name: 'MovieListGenre', params: {id: `${genre.id}` } }">{{genre.name}}<br></router-link>
          </div>
        </div> -->
    <!-- </div>
    <router-view @save-signup-data="signup" @save-login-data="login" /> -->
</div>
    

</template>
<script>
import axios from 'axios'
const BACKEND_URL = "http://127.0.0.1:8000/"

export default {
  
  data() {
    return {
      genres: [
        {
          "id": 28,
          "name": "액션"
        },
        {
          "id": 12,
          "name": "모험"
        },
        {
          "id": 16,
          "name": "애니메이션"
        },
        {
          "id": 35,
          "name": "코미디"
        },
        {
          "id": 80,
          "name": "범죄"
        },
        {
          "id": 99,
          "name": "다큐멘터리"
        },
        {
          "id": 18,
          "name": "드라마"
        },
        {
          "id": 10751,
          "name": "가족"
        },
        {
          "id": 14,
          "name": "판타지"
        },
        {
          "id": 36,
          "name": "역사"
        },
        {
          "id": 27,
          "name": "공포"
        },
        {
          "id": 10402,
          "name": "음악"
        },
        {
          "id": 9648,
          "name": "미스터리"
        },
        {
          "id": 10749,
          "name": "로맨스"
        },
        {
          "id": 878,
          "name": "SF"
        },
        {
          "id": 10770,
          "name": "TV 영화"
        },
        {
          "id": 53,
          "name": "스릴러"
        },
        {
          "id": 10752,
          "name": "전쟁"
        },
        {
          "id": 37,
          "name": "서부"
        }
      ],
      isLoggedIn: false,
      isAdmin: false,
      loginData: null,
  
    }
  },
  methods:{
    setCookies(token) {
      this.$cookies.set('auth-token', token)
      this.isLoggedIn = true
    },

    signup(signupData) {
      console.log(signupData)
      axios.post(BACKEND_URL + 'rest-auth/signup/', signupData)
      .then(response => {
        console.log(response.data.key)
        this.setCookies(response.data.key)
        this.$router.push({ name: 'Home'})
      
      })
      .catch(() => {
        // console.log(err.data.key)
        console.log('ERROR')
      })
    },
    login(loginData) {
      axios.post(BACKEND_URL + 'rest-auth/login/', loginData)
      .then(response => {
        this.setCookies(response.data.key)
        this.$router.push({ name: 'Home'})
      })
      .catch(() => {
        console.log('ERROR')
      })
    },
    
    logout() {
      const config = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(BACKEND_URL + 'rest-auth/logout/', null, config)
      .then(() => {
        this.$cookies.remove('auth-token')
        this.isLoggedIn = false
        this.isAdmin = false

        this.$router.push({ name: 'Home' })
      })
      .catch(() => {
        console.log('ERROR')
      })
    }
  },
  mounted() {
    this.isLoggedIn = this.$cookies.isKey('auth-token')
  },

  watch: {
    isLoggedIn: function() {
      if (this.isLoggedIn === true) {
        const config = {
          headers: {
            'Authorization': `Token ${this.$cookies.get('auth-token')}`
          }
        }
        axios.get(BACKEND_URL + "rest-auth/user/", config)
        .then(response => {
          this.isAdmin = response.data.is_staff
        })
      }
    }
  }
}
</script>






<style>
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  font-family: 'Jua', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.logo{
    font-weight: 900;
    font-size: 27px;
}
.dropdown-menu>a{
    color:white;
}
nav{
    height: 100px;
}
.homebtn{
    color:white;
    font-weight: 900;
    /* font-size:40; */
}
.homebtn{
    font-size:40;
}
nav>ul{
    display: flex;
    /* align-items:; */
    justify-content: space-around;
}
nav.navitem{
    text-decoration: none;
    color:white;
    margin:0px 10px;
}
.nav-link>.btn{
    margin:0px 5px;

}
.navbar{
    background-color: #000000;
}
.dropdown{
    text-align: right;
}
.dropdown-menu{
    background-color:rgb(20, 21, 23);
}
.dropdown-toggle{
    background-color:#2B2B2B;
    text-align: right;
    border:none;
    height:45px;
    /* padding */
    width: 230px;
}
.dropdown-menu{
    background-color:rgb(20, 21, 23);
    width: 230px;
    padding: 10px 15px;
    color:white;
}
</style>
