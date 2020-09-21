<template>
  <div id="app">
    <v-app-bar
      color="deep-purple accent-4"
      dense
      dark
    >
      <v-toolbar-title><img class="logo" src="../src/assets/images/logo.png"/></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn to="/list">
        영양제
      </v-btn>
      <v-btn text>
        추천
      </v-btn>
      <v-btn to="/user/login">
        로그인
      </v-btn>
      <v-btn to="/user/join">
        회원가입
      </v-btn>
    </v-app-bar>
    <router-view />

  </div>
</template>

<script>
// import constants from "./lib/constants";
export default {
  name: 'app',

  components: {
    
  },

  data: () => ({
    
  }),
};
</script>
