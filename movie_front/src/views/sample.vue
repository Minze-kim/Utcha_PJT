<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">읏챠 플레이</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
      <router-link class="nav-link" to="/">Home</router-link> |
      </li>
    <li class="nav-item">
        <span v-if="!isLoggedIn">
          <router-link class="nav-link" :to="{ name:'Signup' }">Signup</router-link> |
          <router-link class="nav-link" :to="{ name:'Login' }">Login</router-link>
        </span>
    </li>
    <li class="nav-item">
        <span v-if="isLoggedIn">
          <router-link to="/accounts/logout" @click.native="logout">로그아웃</router-link>
        </span>
    </li>
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
        </div>
        
    </ul>
    <form class="form-inline my-2 my-lg-0">
        <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
    </div>
    </nav>
</template>

<script>
export default {

}
</script>

<style>

</style>