<template>
  <div data-app>
    <div style="width: 300px; margin:0 auto;">
      <div style="width:90%; padding-top:20px; margin:auto">
        <div class="for-input">
          <p style="text-align:left; margin-bottom:4px">이메일</p>
          <input
            v-model="email"
            placeholder="이메일을 입력해주세요"
            style="border:solid 1px #dadada;height:50px; width:279px;  background-color:white;"
            type="text"
            @change="emailCheck"
          />
        </div>
<br/>
        <div class>
          <p style="text-align: left; margin-bottom:4px">이름</p>
          <input
            v-model="username"
            id="username"
            style=" border:solid 1px #dadada;height:50px;width:279px;  background-color:white;"
            placeholder="이름을 입력해주세요"
            type="text"
          />
        </div>
<br/>
        <div>
          <p style="text-align: left; margin-bottom:4px">성별</p>
          <v-container fluid style="padding:0">
            <v-radio-group class="d-flex" v-model="gender" :mandatory="false">
              <v-radio style="width:30%" label="남성" value="true"></v-radio>
              <v-radio style="width:30%" label="여성" value="false"></v-radio>
            </v-radio-group>
          </v-container>
        </div>



        <div style="color:rgb(0,0,0);">
          <p style="text-align: left; margin-bottom:4px">생년월일</p>
          <v-row justify="center" style="margin-left:3px">
            <v-menu
              ref="menu"
              v-model="menu"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field v-model="date" readonly v-bind="attrs" v-on="on"></v-text-field>
              </template>
              <v-date-picker
                ref="picker"
                v-model="date"
                :max="new Date().toISOString().substr(0, 10)"
                min="1950-01-01"
                @change="save"
              ></v-date-picker>
            </v-menu>
          </v-row>
        </div>

        <div class="password-wrap">
          <p style="text-align: left; margin-bottom:4px">비밀번호</p>
          <input
            v-model="password1"
            id="password1"
            :type="password1Type"
            placeholder="최소 8자 이상으로 입력해주세요"
            style="border:solid 1px #dadada;height:50px; width:279px;  background-color:white;"
          />
          <span>
            <i class="fas fa-eye"></i>
          </span>
        </div>
<br/>
        <div class="password-wrap">
          <p style="text-align: left; margin-bottom:4px">비밀번호 확인</p>
          <input
            v-model="password2"
            id="password2"
            style="border:solid 1px #dadada;height:50px; width:279px; background-color:white;"
            :type="password2Type"
            placeholder="비밀번호를 다시 한 번 입력해주세요"
          />
        </div>
<br/>
        <div class="mb-6" style="height:30px; width:279px; margin:auto">
          <v-dialog width="600px" style="text-align:center">
            <template v-slot:activator="{ on, attrs }" style="text-align:center">
              <div class="row justify-content-between flex" style="width:300px; margin:0px">
                <v-checkbox style="margin:0px; float:left" v-model="isTerm" />
                <p
                
                  v-bind="attrs"
                  style="text-decoration:underline;"
                  v-on="on"
                >개인정보처리방침</p>
                <div style="margin-right:5px">에 동의</div>
              </div>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">개인정보처리방침</span>
              </v-card-title>
              <v-card-text>
                '(주)필소굿'은 (이하 '회사'는) 고객님의 개인정보를 중요시하며, "정보통신망 이용촉진 및 정보보호"에 관한 법률을 준수하고 있습니다. 회사는 개인정보취급방침을 통하여 고객님께서 제공하시는 개인정보가 어떠한 용도와 방식으로 이용되고 있으며, 개인정보보호를 위해 어떠한 조치가 취해지고 있는지 알려드립니다.
                <br />
                <br />■ 수집하는 개인정보 항목
                <br />수집항목 : 이름, 생년월일, 성별, 비밀번호, 이메일, 서비스 이용기록, 접속 로그, 접속 IP 정보
              </v-card-text>
            </v-card>
          </v-dialog>
        </div>

        <button
          style="margin-top:20px; background-color:rgb(128,128,128); width:100%; height:50px; border:solid 0px;"
          @click="Signup"
          class="btn"
        >
          <span>확인</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_BASE_URL = "http://localhost:8000";

export default {
  data: () => {
    return {
      username: "",
      password1: "",
      password2: "",
      gender: true,
      birthday: "",
      email: "",
      password1Type: "password",
      password2Type: "password",
      isTerm: false,
      date: null,
      menu: false,
    };
  },
  computed: {},

  watch: {
    menu(val) {
      val && setTimeout(() => (this.$refs.picker.activePicker = "YEAR"));
    },
  },

  methods: {
    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      return `${month}/${day}/${year}`;
    },
    parseDate(date) {
      if (!date) return null;

      const [month, day, year] = date.split("/");
      return `${year}-${month.padStart(2, "0")}-${day.padStart(2, "0")}`;
    },
    save(date) {
      this.$refs.menu.save(date);
    },
    Signup() {
      const API_SIGNUP_URL = API_BASE_URL + "/users/signup/";
      const signupInfo = {
        username: this.username,
        email: this.email,
        password1: this.password1,
        password2: this.password2,

        birth: this.date,
        gender: this.gender,
      };
      console.log(typeof signupInfo.birth);
      console.log(signupInfo);
      var exptext = /^[A-Za-z0-9_,-]+@[A-Za-z0-9,-]+\.[A-Za-z0-9,-]+/;

      var passwordExp = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d$@$!%*#?&]{8,}$/;
      if (exptext.test(signupInfo.email) == false) {
        //이메일 형식이 알파벳+숫자@알파벳+숫자.알파벳+숫자 형식이 아닐경우
        alert("이메일형식이 올바르지 않습니다.");
      } else if (signupInfo.username.value == "") {
        alert("이름을 입력해주세요");
      } else if (signupInfo.gender == "") {
        alert("성별을 체크해주세요");
      } else if (signupInfo.birth == null) {
        alert("생일을 입력해주세요");
      } else if (signupInfo.password1 == "") {
        alert("비밀번호를 입력해주세요");
      } else if (passwordExp.test(signupInfo.password1) == false) {
        alert("비밀번호 형식이 잘못되었습니다.");
      } else if (signupInfo.password1 != signupInfo.password2) {
        alert("비밀번호가 동일하지않습니다. 다시 입력해주세요.");
      } else if (!this.isTerm) {
        alert("약관을 읽어보시고, 동의란에 체크해주세요.");
      } else {
        axios.post(API_SIGNUP_URL, signupInfo)
        .then(res =>{
          console.log(res);
        })
        this.$router.push("/user/joincomplete");
        alert("회원가입이 완료되었습니다.");
      }
    },
    emailCheck() {
      var exptext = /^[A-Za-z0-9_,-]+@[A-Za-z0-9,-]+\.[A-Za-z0-9,-]+/;
      if (this.email.length >= 0 && !exptext.test(this.email))
      this.error.email = "이메일 형식이 아닙니다.";
      else this.error.email = false;
    },


    //     const API_SIGNUP_URL = API_BASE_URL + '/rest-auth/registration/'
    // },
  },
  // methods: {
  // },
};
</script>
<style scoped>
.for-input {
  width: 300px;
}
/* .user .input-wrap {
  width: 100%;
  float: left;
  margin-bottom: 10px;
  position: relative;
}

.user .input-wrap input {
  width: 100%;
}

.user .wrap {
  float: left;
  margin: 0 auto;
} */
</style>