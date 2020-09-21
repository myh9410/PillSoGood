<template>
  <div class="user" id="login" style="background-color:#f2f2f2">
    <div style="margin:auto; width:50%">
      <div class="input-wrap email-wrap">
        <label for="email">이메일</label>
        <input
          v-model="email"
          v-bind:class="{error : error.email, complete: !error.email&&email.length!=0}"
          @keyup.enter="onLogin"
          id="email"
          placeholder="이메일을 입력해주세요"
          style="height:50px; background-color:white;"
          type="text"
        />
        <div class="error-text" v-if="error.email">{{error.email}}</div>
      </div>
      <div class="input-wrap password-wrap">
        <label for="password">비밀번호</label>
        <input
          v-model="password"
          id="password"
          :type="passwordType"
          v-bind:class="{error : error.password, complete: !error.password&&password.length!=0}"
          @keyup.enter="onLogin"
          placeholder="최소 8자 이상으로 입력해주세요"
          style="height:50px; background-color:white;"
        />
        <span :class="{active : passwordType==='text'}">
          <i class="fas fa-eye"></i>
        </span>
        <div class="error-text" v-if="error.password">{{error.password}}</div>
      </div>

      <GoogleLogin :component="component" />

      <div class="submit">
        <v-btn large color="#BCAAA4" @click="onLogin" :disabled="!isSubmit" :class="{disabled : !isSubmit}">로그인</v-btn>
      </div>
    </div>
  </div>
</template>

<script>
import '../../assets/css/login.scss'
import PV from "password-validator";
import * as EmailValidator from "email-validator";
import http from  "@/util/http-common"
import GoogleLogin from "../../components/accounts/Google.vue";

export default {
  name: "join",
  components: {
    GoogleLogin
  },
  data: () => {
    return {
      email:'',
      password: '',
      passwordSchema : new PV(),
      passwordType: "password",
      error : {
        email : false,
        password : false
      },
      isSubmit: false,
      component: this
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
    .letters()

  },
  watch: {
    email: function() {
      this.emailCheckForm()
    },
    password: function() {
      this.pwdCheckForm();
    },
  },
  methods: {
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
      Object.values(this.error).map(v => {
        if (v) isSubmit = false;
      });
      this.isSubmit = isSubmit;
    },
    onLogin() {
      http.post('users/login/',
        {
          email : this.email,
          password : this.password
        })
      .then( res => {
        //store에 저장하고 가져다가 씀
        console.log(res.data.user);
        alert("로그인에 성공하였습니다!");
        this.$router.push("/");
      }). catch( err => {
        console.log(err);
      })
    }
  },

};
</script>
