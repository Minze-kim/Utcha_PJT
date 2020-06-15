<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
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
            :to="{ name: 'MovieListGenre', params: {id: `${genre.id}` } }">{{genre.name}}<br></router-link>
          </div>
        </div>
        <router-link v-if="isAdmin" v-bind:to="{name:'AdminPage' }">관리자 페이지</router-link>  
    </div>
    <router-view @save-signup-data="signup" @save-login-data="login" />


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
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
