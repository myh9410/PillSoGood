<template>
  <div data-app id="app">
    <v-app-bar color="#eebb4d" dense dark>
      <v-toolbar-title
        ><img
          class="logo"
          src="../src/assets/images/logo-black.png"
          @click="toHome"
      /></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn to="/list" color="#eebb4d" elevation="0"> 영양제 </v-btn>
      <v-btn to="/recommend" color="#eebb4d" elevation="0"> 추천 </v-btn>
      <div v-if="!this.$store.state.isLogged">
        <v-btn to="/user/login" color="#eebb4d" elevation="0"> 로그인 </v-btn>
      </div>
      <div v-if="!this.$store.state.isLogged">
        <v-btn to="/user/join" color="#eebb4d" elevation="0"> 회원가입 </v-btn>
      </div>
      <div v-else>
        <v-menu bottom offset-y>
          <template v-slot:activator="{ on, attrs }">
            <v-btn v-bind="attrs" v-on="on" style="" color="#eebb4d">
              {{ nname }}
            </v-btn>
          </template>
          <v-list>
            <v-list-item>
              <router-link to="/user/favorites" style="text-decoration:none"
                >관심사 변경</router-link
              >
            </v-list-item>
            <v-list-item>
              <p class="logout" @click="onLogout">로그아웃</p>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>
    </v-app-bar>

    <router-view />

    <footer v-if="isFooter">
      <div class="footer-container">
        <div class="col1">
          <img src="../src/assets/images/logo-vertical-black.png" />
        </div>
        <div class="right">
          <ul class="comp-link">
            <li><a href="/">홈으로</a></li>
            <li><a href="/user/join">회원가입</a></li>
            <li><a href="/recommend">추천</a></li>
            <li><a href="/list">영양제</a></li>
          </ul>
          <div class="col2">
            SSAFY 506 Pill So Good 팀 <br />
            류승민, 김민재, 문용호, 배민규, 이규진 <br />
            Copyright ⓒ 2020. Pill So Good. All rights reserved.
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
// import constants from "./lib/constants";
import "../src/assets/css/home.scss";
import store from "@/store.js";
// import http from '@/util/http-common'

export default {
  name: "app",

  components: {},

  // beforeMount() {
  //   console.log(store.state.isLogged);
  // },
  mounted() {},
  data: () => ({
    isFooter: true,
    items: [{ name: "관심사 변경" }, {}],
    nname: "",
  }),
  methods: {
    toHome() {
      this.$router.push("/");
    },
    onLogout() {
      // http.post('users/logout/');
      store.dispatch("logout");
      if (window.location.pathname == "/") this.$router.go(0);
      else this.$router.push({ name: "Home" });
    },
    fetchuser() {
      store.dispatch("state");
      // console.log(store.state.userData.username);
    },
    checkFooter(url) {
      let array = ["TonicDetail"];
      // console.log(url);

      let isFooter = true;
      array.map((path) => {
        if (url === path) {
          isFooter = false;
        }
      });
      this.isFooter = isFooter;
    },
  },
  watch: {
    $route(to) {
      this.checkFooter(to.name);
    },
  },
  created() {
    let url = this.$route.name;
    // console.log(url);
    this.checkFooter(url);
    this.nname = this.$store.state.userInfo.username;
  },
};
</script>
<style scoped>
p.logout:hover {
  cursor: pointer;
}
</style>
