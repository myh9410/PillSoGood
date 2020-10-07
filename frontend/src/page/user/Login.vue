<template>
  <div class="user" id="login">
    <img src="../../assets/images/logo-vertical-black.png" id="logo" />
    <p>로그인</p>
    <div class="container" style="margin: auto">
      <div class="input-wrap email-wrap">
        <label for="email">이메일</label>
        <input
          v-model="email"
          v-bind:class="{
            error: error.email,
            complete: !error.email && email.length != 0,
          }"
          @keyup.enter="onLogin"
          id="email"
          placeholder="이메일을 입력해주세요"
          style="height: 50px; background-color: white"
          type="text"
        />
        <div class="error-text" v-if="error.email">{{ error.email }}</div>
      </div>
      <div class="input-wrap password-wrap">
        <label for="password">비밀번호</label>
        <input
          v-model="password"
          id="password"
          :type="passwordType"
          v-bind:class="{
            error: error.password,
            complete: !error.password && password.length != 0,
          }"
          @keyup.enter="onLogin"
          placeholder="최소 8자 이상으로 입력해주세요"
          style="height: 50px; background-color: white"
        />
        <span :class="{ active: passwordType === 'text' }">
          <i class="fas fa-eye"></i>
        </span>
        <div class="error-text" v-if="error.password">{{ error.password }}</div>
      </div>
      <div class="submit">
        <input
          type="submit"
          value="Login"
          v-bind:style="loginButton"
          @click="onLogin"
          :disabled="!isSubmit"
          :class="{ disabled: !isSubmit }"
        />
      </div>
      <div class="snsLogin">
        <img src="../../assets/images/google.png" @click="onGoogle" />
        <img src="../../assets/images/kakao.png" @click="onKakao" />
      </div>
      <br />
      <br />
    </div>
  </div>
</template>

<script>
import swal from "sweetalert";
import "../../assets/css/login.scss";
import PV from "password-validator";
import * as EmailValidator from "email-validator";
import http from "@/util/http-common";
import store from "@/store.js";
// const config = require(`../../util/config.json`);

export default {
  name: "login",
  components: {},
  data: () => {
    return {
      email: "",
      password: "",
      passwordSchema: new PV(),
      passwordType: "password",
      error: {
        email: false,
        password: false,
      },
      isSubmit: false,
      component: this,
      loginButton: {
        backgroundColor: "#4CAF50",
        color: "white",
        opacity: "0.4",
      },
    };
  },
  created() {
    this.component = this;

    this.passwordSchema
      .is()
      .min(8)
      .is()
      .max(100)
      .has()
      .digits()
      .has()
      .letters();
  },
  watch: {
    email: function() {
      this.emailCheckForm();
    },
    password: function() {
      this.pwdCheckForm();
    },
    isSubmit: function() {
      if (this.isSubmit) this.loginButton.opacity = "1.0";
      else this.loginButton.opacity = "0.4";
    },
  },
  methods: {
    setCookie(key) {
      this.$cookies.set("auth-token", key);
    },
    emailCheckForm() {
      if (this.email.length >= 0 && !EmailValidator.validate(this.email))
        this.error.email = "이메일 형식이 아닙니다.";
      else this.error.email = false;
    },
    pwdCheckForm() {
      if (
        this.password.length >= 0 &&
        !this.passwordSchema.validate(this.password)
      )
        this.error.password = "영문, 숫자 포함 8자리 이상이어야 합니다.";
      else this.error.password = false;

      let isSubmit = true;
      Object.values(this.error).map((v) => {
        if (v) {
          isSubmit = false;
        }
      });
      this.isSubmit = isSubmit;
    },
    onLogin() {
      http
        .post("users/login/", {
          email: this.email,
          password: this.password,
        })
        .then((res) => {
          //store에 저장하고 가져다가 씀
          this.setCookie(res.data.key);
          store.dispatch("login", res.data.user);
          swal({
            title: "환영합니다!",
            icon: "success",
          });
          // alert("로그인에 성공하였습니다!");
          this.$router.push("/");
        })
        .catch(() => {
          swal({
            title: "로그인에 실패하였습니다!",
            text: "다시 시도해주세요",
            icon: "error",
          });
          // this.$router.push("/user/login");
          // console.log(err);
        });
    },
    onGoogle() {
      this.$gAuth.signIn().then(GoogleUser => {
        var gProfile = GoogleUser.getBasicProfile();
        var gNickname = gProfile.getName();
        var gEmail = gProfile.getEmail();
        http.post("/accounts/check", {
          email : gEmail,
          nickname : gNickname,
          password : "",
        }).then(data => {
          if(data.data.state=='login'){
            http.post("/users/login/", {
                email: gEmail,
                password: gEmail,
                }).then((res) => {
                  this.setCookie(res.data.key)
                  store.dispatch("login", res.data.user);
                  swal({
                    title: "환영합니다!",
                    icon: "success",
                  });
                  this.$router.push("/");
                })
                .catch(() => {
                  swal({
                    title: "로그인에 실패하였습니다!",
                    text: "다시 시도해주세요",
                    icon: "error",
                  });
                });
          } else{
            http.post('/users/signup/',{
                  username: gNickname,
                  email: gEmail,
                  password1: gEmail,
                  password2: gEmail,

                  birth: '2010-10-20',
                  gender: true,
            }).then(res => 
              { 
                this.setCookie(res.data.key);
                store.dispatch("login", {
                    username : gNickname,
                    email : gEmail,
                });
                this.$router.push("/user/favorites");
                swal({
                  title: "회원가입이 완료되었습니다.",
                  icon: "success",
                });
            })
          }
        })
      })
    },
    onKakao() {
      window.Kakao.Auth.login({
        scope : 'account_email, profile',
        success: this.GetMe,
      });
    },
    GetMe(){
      window.Kakao.API.request({
        url: '/v2/user/me',
        success : res => {
          const kakao_account = res.kakao_account;
          const userInfo = {
            nickname : kakao_account.profile.nickname,
            email : kakao_account.email
          }
          http.post('/accounts/check',{
            email : userInfo.email,
            nickname : userInfo.nickname
          }).then(data => {
            if(data.data.state=='login'){
              http.post("/users/login/", {
                email: userInfo.email,
                password: userInfo.email,
              }).then((res) => {
                this.setCookie(res.data.key)
                store.dispatch("login", res.data.user);
                swal({
                    title: "환영합니다!",
                    icon: "success",
                });
                this.$router.push("/");
              }).catch(() => {
                swal({
                  title: "로그인에 실패하였습니다!",
                  text: "다시 시도해주세요",
                  icon: "error",
                });
              });
            } else{
              http.post('/users/signup/',{
                username: userInfo.nickname,
                email: userInfo.email,
                password1: userInfo.email,
                password2: userInfo.email,
                birth: '2010-10-20',
                gender: true,
              }).then(res => { 
                this.setCookie(res.data.key);
                store.dispatch("login", {
                    username : userInfo.nickname,
                    email : userInfo.email,
                });
                this.$router.push("/user/favorites");
                swal({
                  title: "회원가입이 완료되었습니다.",
                  icon: "success",
                });
              }).catch((e) => {
                console.log(e.response);
                  swal({
                    title: "회원가입에 실패하였습니다! 이미 가입하셨는지 확인해주세요!",
                    text: "다시 시도해주세요",
                    icon: "error",
                  });
              });
            }
          })
        }
      })
    },
  },
};
</script>
