<template>
  <div data-app>
    <div style="width: 700px; margin: 0 auto">
      <div style="width: 100%; padding-top: 10px; margin: auto">
        <!--         
            <div style="margin-top:50px"> -->

        <img
          src="../../assets/images/logo-vertical-black.png"
          style="width: 40%"
          id="logo"
        />
        <h1 style="text-align:center">회원가입</h1>
        <br /><br />
        <p style="text-align: left; margin-bottom: 4px">이메일</p>

        <input
          v-model="email"
          v-bind:class="{
            error: error.email,
            complete: !error.email && email.length != 0,
          }"
          id="email"
          placeholder="이메일을 입력해주세요"
          style="
            border: solid 1px #dadada;
            height: 50px;
            width: 100%;
            background-color: white;
          "
          type="text"
        />
        <div class="error-text" v-if="error.email">{{ error.email }}</div>
      </div>
      <br />
      <div class>
        <p style="text-align: left; margin-bottom: 4px">이름</p>
        <input
          v-model="username"
          id="username"
          style="
            border: solid 1px #dadada;
            height: 50px;
            width: 100%;
            background-color: white;
          "
          placeholder="이름을 입력해주세요"
          type="text"
        />
      </div>
      <br />

      <div class="password-wrap">
        <p style="text-align: left; margin-bottom: 4px">비밀번호</p>
        <input
          v-model="password1"
          id="password1"
          :type="password1Type"
          placeholder="최소 8자 이상으로 입력해주세요"
          v-bind:class="{
            error: error.password1,
            complete: !error.password1 && password1.length != 0,
          }"
          style="
            border: solid 1px #dadada;
            height: 50px;
            width: 100%;
            background-color: white;
          "
        />
        <span>
          <i class="fas fa-eye"></i>
        </span>
        <div class="error-text" v-if="error.password1">
          {{ error.password1 }}
        </div>
      </div>

      <br />
      <div class="password-wrap">
        <p style="text-align: left; margin-bottom: 4px">비밀번호 확인</p>
        <input
          v-model="password2"
          id="password2"
          style="
            border: solid 1px #dadada;
            height: 50px;
            width: 100%;
            background-color: white;
          "
          :type="password2Type"
          v-bind:class="{
            error: error.password2,
            complete: !error.password2 && password2.length != 0,
          }"
          placeholder="비밀번호를 다시 한 번 입력해주세요"
        />
        <div class="error-text" v-if="error.password2">
          {{ error.password2 }}
        </div>
      </div>
      <div style="flex-direction: row">
        <p style="text-align: left; margin-bottom: 4px">성별</p>
        <v-container style="padding: 0">
          <v-radio-group v-model="gender">
            <v-row style="margin-left: 0px">
              <v-radio
                style="width: 20%; float: right"
                label="남성"
                value="true"
              ></v-radio>
              <v-radio
                style="width: 20%; flex-direction: row"
                label="여성"
                value="false"
              ></v-radio>
            </v-row>
          </v-radio-group>
        </v-container>
      </div>

      <div style="color: rgb(0, 0, 0)">
        <p style="text-align: left; margin-bottom: 4px">생년월일</p>
        <input
          type="date"
          style="
            border: solid 1px #dadada;
            height: 50px;
            width: 100%;
            background-color: white;
          "
          v-model="date"
        />
      </div>
      <br />
      <br />
      <div class="mb-6" style="height: 30px; width: 100%; margin: auto">
        <v-dialog width="600px" style="text-align: center">
          <template v-slot:activator="{ on, attrs }" style="text-align: center">
            <div
              class="row justify-content-between flex"
              style="width: 300px; margin: 0px"
            >
              <v-checkbox style="margin: 0px; float: left" v-model="isTerm" />
              <p v-bind="attrs" style="text-decoration: underline" v-on="on">
                개인정보처리방침
              </p>
              <div style="margin-right: 5px">에 동의</div>
            </div>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">개인정보처리방침</span>
            </v-card-title>
            <v-card-text>
              '(주)필소굿'은 (이하 '회사'는) 고객님의 개인정보를 중요시하며,
              "정보통신망 이용촉진 및 정보보호"에 관한 법률을 준수하고 있습니다.
              회사는 개인정보취급방침을 통하여 고객님께서 제공하시는 개인정보가
              어떠한 용도와 방식으로 이용되고 있으며, 개인정보보호를 위해 어떠한
              조치가 취해지고 있는지 알려드립니다.
              <br />
              <br />■ 수집하는 개인정보 항목 <br />수집항목 : 이름, 생년월일,
              성별, 비밀번호, 이메일, 서비스 이용기록, 접속 로그, 접속 IP 정보
            </v-card-text>
          </v-card>
        </v-dialog>
      </div>

      <button
        style="
          margin-top: 20px;
          background-color: #96bb7c;
          width: 100%;
          height: 50px;
          border: solid 0px;
        "
        @click="Signup"
        class="btn"
      >
        <span>확인</span>
      </button>
    </div>
  </div>
  <!-- </div> -->
</template>

<script>
import http from "@/util/http-common";
import swal from "sweetalert";

import store from "@/store.js";

export default {
  components: {},
  data: () => {
    return {
      username: "",
      password1: "",
      password2: "",
      gender: null,
      birthday: "",
      email: "",
      error: {
        email: false,
        password1: false,
        password2: false,
      },
      password1Type: "password",
      password2Type: "password",
      isTerm: false,
      date: null,
      menu: false,
    };
  },
  computed: {},

  watch: {
    email: function() {
      this.emailCheck();
    },
    password1: function() {
      this.password1Check();
    },
    password2: function() {
      this.password2Check();
    },
  },
  created() {
    this.component = this;
  },
  methods: {
    setCookie(key) {
      this.$cookies.set("auth-token", key);
    },
    Signup() {
      // const API_SIGNUP_URL = API_BASE_URL + "/users/signup/";
      const signupInfo = {
        username: this.username,
        email: this.email,
        password1: this.password1,
        password2: this.password2,

        birth: this.date,
        gender: this.gender,
      };

      var exptext = /^[A-Za-z0-9_,-]+@[A-Za-z0-9,-]+\.[A-Za-z0-9,-]+/;
      var passwordExp = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d$@$!%*#?&]{8,}$/;
      if (signupInfo.email === "") {
        swal("이메일을 입력해주세요");
      } else if (exptext.test(signupInfo.email) === false) {
        //이메일 형식이 알파벳+숫자@알파벳+숫자.알파벳+숫자 형식이 아닐경우
        swal("이메일형식이 올바르지 않습니다.");
      } else if (signupInfo.username === "") {
        swal("이름을 입력해주세요");
      } else if (signupInfo.password1 === "") {
        swal("비밀번호를 입력해주세요");
      } else if (passwordExp.test(signupInfo.password1) === false) {
        swal("비밀번호 형식이 잘못되었습니다.");
      } else if (signupInfo.password1 !== signupInfo.password2) {
        swal("비밀번호가 동일하지않습니다. 다시 입력해주세요.");
      } else if (signupInfo.gender === null) {
        swal("성별을 체크해주세요");
      } else if (signupInfo.birth === null) {
        swal("생일을 입력해주세요");
      } else if (!this.isTerm) {
        swal("약관을 읽어보시고, 동의란에 체크해주세요.");
      } else {
        http.post("/users/signup/", signupInfo)
        .then((res) => {
          this.setCookie(res.data.key);
          store.dispatch("login", {
            username: this.username,
            email: this.email,
            birth: this.date,
            gender: this.gender,
          });
          this.$router.push("/user/favorites");
          swal({
            title: "회원가입이 완료되었습니다.",
            icon: "success",
          });
        })
        .catch((err) => {
          if (err.response.data.username) {
            swal("아이디 : " + err.response.data.username);
          } else if (err.response.data.password) {
            swal("비밀번호 : " + err.response.data.password);
          } else if (err.response.data.password1) {
            swal("비밀번호 : " + err.response.data.password1);
          } else if (err.response.data.password2) {
            swal("비밀번호 확인 : " + err.response.data.password2);
          } else if (err.response.data.non_field_errors) {
            swal("" + err.response.data.non_field_errors);
          }
        })
      }
    },
    emailCheck() {
      var exptext = /^[A-Za-z0-9_,-]+@[A-Za-z0-9,-]+\.[A-Za-z0-9,-]+/;
      if (this.email.length >= 0 && !exptext.test(this.email)) {
        this.error.email = "이메일 형식이 아닙니다.";
      } else {
        this.error.email = false;
      }
    },

    password1Check() {
      var passwordExp = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d$@$!%*#?&]{8,}$/;
      if (this.password1.length >= 0 && !passwordExp.test(this.password1)) {
        this.error.password1 = "영문, 숫자 포함 8자리 이상이어야 합니다.";
      } else {
        this.error.password1 = false;
      }
    },
    password2Check() {
      if (this.password2.length >= 0 && this.password1 != this.password2) {
        this.error.password2 = "비밀번호를 똑같이 적어주세요";
      } else {
        this.error.password2 = false;
      }
    },
  },
};
</script>
<style>
.for-input {
  width: 300px;
}
</style>
