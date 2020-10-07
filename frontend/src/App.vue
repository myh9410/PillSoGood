<template>
  <div data-app id="app">
    <v-app-bar color="#fbcb64" dense dark>
      <v-toolbar-title
        ><img
          class="logo"
          style="padding: 20px"
          src="../src/assets/images/logo-black.png"
          @click="toHome"
      /></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        to="/list"
        style="font-weight: 600; font-size: 16px"
        color="#fbcb64"
        elevation="0"
      >
        영양제
      </v-btn>
      <div v-if="!this.$store.state.isLogged">
        <v-btn
          @click="needLogin()"
          style="font-weight: 600; font-size: 16px"
          color="#fbcb64"
          elevation="0"
        >
          추천
        </v-btn>
      </div>
      <div v-else>
        <v-btn
          to="/recommend"
          style="font-weight: 600; font-size: 16px"
          color="#fbcb64"
          elevation="0"
        >
          추천
        </v-btn>
      </div>
      <div v-if="!this.$store.state.isLogged">
        <v-btn
          to="/user/login"
          style="font-weight: 600; font-size: 16px"
          color="#fbcb64"
          elevation="0"
        >
          로그인
        </v-btn>
      </div>
      <div v-if="!this.$store.state.isLogged">
        <v-btn
          to="/user/join"
          style="font-weight: 600; font-size: 16px"
          color="#fbcb64"
          elevation="0"
        >
          회원가입
        </v-btn>
      </div>
      <div v-else>
        <v-menu bottom offset-y>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              v-bind="attrs"
              v-on="on"
              style="font-weight: 600; font-size: 16px"
              color="#fbcb64"
              elevation="0"
            >
              {{ nname }}
            </v-btn>
          </template>
          <v-list>
            <v-list-item>
              <router-link to="/user/favorites" style="text-decoration: none"
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
          <!-- <v-contatiner> -->
          <ul style="display: flex" class="comp-link">
            <v-row>
              <li><a href="/">홈으로</a></li>
            </v-row>
            <v-row>
              <li><a href="/user/join">회원가입</a></li>
            </v-row>
            <v-row>
              <li>
                <a v-if="this.$store.state.isLogged" href="/recommend">추천</a>
                <a
                  v-if="!this.$store.state.isLogged"
                  style="cursor: pointer"
                  @click="needLogin()"
                  >추천</a
                >
              </li>
            </v-row>

            <v-row>
              <li><a href="/list">영양제</a></li>
            </v-row>
          </ul>
          <!-- </v-contatiner> -->
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
import swal from "sweetalert";
export default {
  name: "app",

  components: {},
  data: () => ({
    isFooter: true,
    items: [{ name: "관심사 변경" }, {}],
  }),
  methods: {
    toHome() {
      this.$router.push("/");
    },
    onLogout() {
      // http.post('users/logout/');
      store.dispatch("logout");
      this.$cookies.remove('auth-token')
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
    needLogin() {
      swal({
        title: "로그인이 필요한 서비스입니다!",
        icon: "error",
      });
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
    // this.nname = this.$store.state.userInfo.username;
  },
  computed: {
    nname() {
      return this.$store.state.userInfo.username;
    },
  },
};
</script>
<style scoped>
p.logout:hover {
  cursor: pointer;
}
@font-face {
  font-family: "BBTreeGR";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_nine_@1.1/BBTreeGR.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
* {
  font-family: "BBTreeGR";
}
</style>
