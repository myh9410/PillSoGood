<template>
  <div id="app">
    <v-app-bar
      color="deep-purple accent-4"
      dense
      dark
    >
      <v-toolbar-title><img class="logo" src="../src/assets/images/logo.png" @click="toHome"></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn to="/list">
        영양제
      </v-btn>
      <v-btn to="/recommend">
        추천
      </v-btn>
      <div v-if="!this.$store.state.isLogged">
        <v-btn to="/user/login">
          로그인
        </v-btn>
      </div>
      <div v-else>
        <v-btn @click="onLogout">
          로그아웃
        </v-btn>
      </div>
      <v-btn to="/user/join">
        회원가입
      </v-btn>
    </v-app-bar>
    
    <router-view />

  </div>
</template>

<script>
// import constants from "./lib/constants";
import '../src/assets/css/home.scss';
import store from '@/store.js'
// import http from '@/util/http-common'

export default {
  name: 'app',

  components: {
    
  },
  beforeMount() {
    console.log(store.state.isLogged);
  },
  mounted() {

  },
  data: () => ({
    
  }),
  methods : {
    toHome() {
      this.$router.push('/');
    },
    onLogout(){
      // http.post('users/logout/');
      store.dispatch('logout');
      if (window.location.pathname == '/') this.$router.go(0);
      else this.$router.push({ name: 'Home'});
    }
  }
};
</script>
