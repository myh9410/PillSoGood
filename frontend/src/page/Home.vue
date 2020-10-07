<template>
  <div class="home">
    <!-- <div class="explanation">
      <img src="../../src/assets/images/main.png" />
      <div class="description1">
        <p>나만의 영양제를<br />한눈에</p>
      </div>
      <div class="description2">
        <p>약 <b>3만개</b>의 영양제 중에, <br />내게 맞는 조합을 추천해줘요!</p>
      </div>
      <div class="buttons">
        <a href="/list">제품 보기</a>

        <a
          v-if="!this.$store.state.isLogged"
          style="
            border: 1px solid #eebb4d;
            margin: 1%;
            margin-top: 3%;
            line-height: 49px;
            text-align: center;
            width: 144px;
            height: 49px;
            text-decoration: none;
            color: black;
            display: inline-block;
            cursor:pointer;
          "
          @click="needLogin()"
          >영양제 추천</a
        >

        <a v-if="this.$store.state.isLogged" href="/recommend">영양제 추천</a>
      </div>
    </div> -->

    <!-- <v-card>
      <v-img
        src="../../src/assets/images/main.jpg"
        class="white--text align-end"
        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
        height="200px"
      >
        <v-card-title>나아아아아ㅏ</v-card-title>
      </v-img>
    </v-card> -->

    <!-- <div style="background-image: url('../../src/assets/images/main.jpg')"> -->
    <!-- <img style="width: 100%" src="../../src/assets/images/main.jpg" alt="" /> -->

    <!-- <div
      style="
        position: relative;
        width: 100%;
        margin: 10px auto;
        background-color: #fbe9b9;
      "
    >
      <img
        style="
          top: 0px;
          opacity: 80%;
          width: 100%;
          height: 400px;
          line-height: 400px;
        "
        src="../../src/assets/images/main.jpg"
        alt=""
      />
      <div style="position: absolute; top: 10px">
        <div class="description1">
          <p>나만의 영양제를<br />한눈에</p>
        </div>
        <div class="description2">
          <p>
            약 <b>3만개</b>의 영양제 중에, <br />내게 맞는 조합을 추천해줘요!
          </p>
        </div>
        <div class="buttons">
          <a href="/list">제품 보기</a>

          <a
            v-if="!this.$store.state.isLogged"
            style="
              border: 1px solid #eebb4d;
              margin: 1%;
              margin-top: 3%;
              line-height: 30px;
              text-align: center;
              width: 144px;
              height: 30px;
              text-decoration: none;
              color: black;
              display: inline-block;
              cursor: pointer;
            "
            @click="needLogin()"
            >영양제 추천</a
          >

          <a v-if="this.$store.state.isLogged" href="/recommend">영양제 추천</a>
        </div>
      </div>
    </div> -->

    <section style="margin-top: 20px" id="" class="mainBanner">
      <div class="mainBWrap container">
        <h1>나만의 영양제를<br />한눈에</h1>
        <p>약 <b>3만개</b>의 영양제 중에, <br />내게 맞는 조합을 추천해줘요!</p>
        <br />
        <div>
          <v-btn
            style="margin: 0px 10px; width: 150px; height: 50px"
            color="#E6B553"
            ><a
              style="
                text-decoration: none;
                color: white;
                font-weight: 100;
                font-size: 16px;
              "
              href="/list"
              >제품 보기</a
            ></v-btn
          >
          <v-btn
            style="margin: 0px 10px; width: 150px; height: 50px"
            color="#E6B553"
          >
            <a
              v-if="!this.$store.state.isLogged"
              style="
                text-decoration: none;
                color: white;
                font-weight: 100;
                font-size: 16px;
              "
              @click="needLogin()"
              >영양제 추천</a
            >
            <a
              style="
                text-decoration: none;
                color: white;
                font-weight: 100;
                font-size: 16px;
              "
              v-if="this.$store.state.isLogged"
              href="/recommend"
              >영양제 추천</a
            >
          </v-btn>
        </div>
      </div>
    </section>

    <br />
    <section>
      <div style="padding: 50px" class="catchphrase">
        <div class="s1">
          <h2>
            <span style="font-size: 24px">Pill So Good</span>
            은
          </h2>
        </div>
        <br />
        <v-row>
          <v-col>
            <img
              src="../assets/images/algorithm.png"
              style="width: 100px; height: 100px; margin-bottom: 10px"
            /><br />
            <br />
            <h4 style="color: #535353">
              관심항목 기반의<br />
              추천 알고리즘!
            </h4>
          </v-col>
          <v-col>
            <img
              src="../assets/images/supplement.png"
              style="width: 100px; height: 100px; margin-bottom: 10px"
            /><br />
            <br />
            <h4 style="color: #535353">
              내게 맞는<br />
              나를 위한 영양제!
            </h4>
          </v-col>
          <v-col>
            <img
              src="../assets/images/nutrient.png"
              style="width: 100px; height: 100px; margin-bottom: 10px"
            /><br />
            <br />
            <h4 style="color: #535353">
              영양제의 성분까지<br />
              한눈에!
            </h4>
          </v-col>
        </v-row>
      </div>
    </section>
    <br />
    <div class="products-login" v-if="this.$store.state.isLogged">
      <br />
      <h1>추천 영양제</h1>
      <br />
      <vueper-slides
        fade
        :touchable="false"
        autoplay
        arrows-outside
        fractions
        progress
        color="#ADC779"
        height="22rem"
        :parallax="parallax"
        :parallax-fixed-content="parallaxFixedContent"
      >
        <vueper-slide
          v-for="recommend in recommends"
          :key="recommend.id"
          :title="recommend.name"
          :image="recommend.src"
          style="margin: auto; width: 30%; height: 50%"
        />
      </vueper-slides>
    </div>
    <div class="products-logout" v-else>
      로그인을 통해 <br />
      나를 위한 비타민들을 <br />
      확인해보세요!<br /><br /><br />
      <v-btn style="background-color: #eec15a" x-large @click="toLogin"
        >로그인</v-btn
      >
    </div>
    <div class="reviews" v-if="reviews.length != 0">
      <h1>최신 리뷰들</h1>
      <br />
      <vueper-slides
        fade
        :touchable="false"
        autoplay
        arrows-outside
        fractions
        progress
      >
        <vueper-slide
          v-for="review in reviews"
          :key="review.id"
          :title="review.user.username"
          :content="review.content"
        />
      </vueper-slides>
    </div>
  </div>
</template>

<script>
import "vueperslides/dist/vueperslides.css";
import "../assets/css/home.scss";
import { VueperSlides, VueperSlide } from "vueperslides";
import http from "@/util/http-common";
import swal from "sweetalert";
// @ is an alias to /src

export default {
  name: "Home",
  components: {
    VueperSlides,
    VueperSlide,
  },
  mounted() {
    if (this.$store.state.isLogged) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      http.get("recommends/", config).then((res) => {
        if (res.data.length > 10) {
          this.recommends = res.data.splice(0, 10);
        } else {
          this.recommends = res.data;
        }
        for (let i = 0; i < this.recommends.length; i++) {
          this.recommends[i].src =
            "https://firebasestorage.googleapis.com/v0/b/pillsogood-764c8.appspot.com/o/images%2F" +
            this.recommends[i].name +
            "_1.jpg?alt=media";
        }
      });
    }
    http.get("reviews/").then((res) => {
      if (res.data.length > 10) {
        this.reviews = res.data.splice(0, 10);
      } else {
        this.reviews = res.data;
      }
    });
  },
  data: () => ({
    recommends: [],
    reviews: [],
    parallax: 1,
    parallaxFixedContent: false,
  }),
  methods: {
    toLogin() {
      this.$router.push("/user/login");
    },
    needLogin() {
      swal({
        title: "로그인이 필요한 서비스입니다!",
        icon: "error",
      });
    },
  },
};
</script>
<style scoped>
.vueperslides__parallax-wrapper {
  height: 22rem;
}
.vueperslides__progress {
  color: #ff7777b8;
}
/*main banner button*/
.mainBanner {
  height: 20em;

  background-position: center;
  -moz-align-items: center;
  -webkit-align-items: center;
  -ms-align-items: center;
  display: -moz-flex;
  display: -webkit-flex;
  display: -ms-flex;
  display: flex;
  align-items: center;
  padding: 0;
  position: relative;
}
.mainBanner .mainBWrap {
  padding-left: 5em;
  padding-top: 4em;
  height: 100%;
  position: relative;
  text-align: right;
  margin-right: 50px;
}
.mainBanner .mainBWrap h1 {
  font-weight: 600;
  font-size: 2.6em;
  line-height: 1.4em;
  color: #444;
}

.mainBanner p {
  bottom: 1.5em;
  font-size: 1.1em;
  color: #847a6e;
  font-weight: 600;
  font-family: "NanumGothic";
}
.mainBanner p em {
  font-size: 1.4em;
  color: #a1917d;
  font-weight: 500;
  padding: 0 0.5em;
  font-family: "arial";
  background: #fff;
  border-radius: 10em;
}

.mainBtnWrap {
  margin: 3em 0;
  padding: 0;
}
.mainBtnWrap div h2 {
  text-align: center;
  margin-bottom: 1em;
}
.mainBtn {
  margin: 0;
}
.mainBtn a {
  position: relative;
  display: inline-block;
  width: 50%;
  height: 10em;
  border-radius: 0.5em;
  border: 2px solid #fe8900;
  overflow: hidden;
  background: #fe8900;
  color: #fff !important;
  padding: 1em;
  text-decoration: none;
  position: relative;
  align-items: center;
}
.mainBtn a:hover {
  background: #fff;
  color: #333 !important;
}
.mainBtn a:active {
  background: #fff;
  color: #333 !important;
}
.mainBtn a:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  height: 10em;
  width: 10em;
}
.mainBtn a.goIconPro {
  margin-right: 1em;
}
.mainBtn a.goIconCheck {
  margin-left: 1em;
}
.mainBtn a.goIconPro:before {
  background: url("/inc/img/goIcon1w.png") no-repeat 100%;
  background-size: 60%;
  background-position: 70%;
}
.mainBtn a.goIconCheck:before {
  background: url("/inc/img/goIcon2w.png") no-repeat 100%;
  background-size: 60%;
  background-position: 60%;
}
.mainBtn a .mainBtnCon {
  padding-left: 9em;
}
.mainBtn a .mainBtnCon span {
  font-size: 1.7em;
}
.mainBtn a .mainBtnCon p {
  font-size: 1.1em;
  margin-top: 0.4em;
}
.mainBtn a i {
  position: absolute;
  right: 1em;
  font-size: 2em;
}

.majorTitArrow {
  display: none;
}
.majorTitArrowO {
  position: absolute;
  right: 0.5em;
  top: 35%;
  font-size: 3em;
}
.btnShadow {
  -webkit-box-shadow: 0 5px 4px 0 rgba(0, 0, 0, 0.15);
  box-shadow: 0 5px 4px 0 rgba(0, 0, 0, 0.15);
}

@media (max-width: 1024px) {
  .mainBanner {
    background-size: 150%;
    background-position: center;
  }
  .mainBtn a {
    height: 9em;
  }
  .mainBtn a:before {
    height: 9em;
    width: 6em;
  }
  .mainBtn a .mainBtnCon {
    padding-left: 5.5em;
  }
  .majorTitArrow {
    display: inline-block;
    padding-left: 1.5em;
    font-size: 0.9em !important;
    position: relative !important;
  }
  .majorTitArrowB {
    display: none;
  }
}
@media (max-width: 767px) {
  .mainBanner {
    height: 13em;
  }
  .mainBanner .mainBWrap {
    padding-left: 3em;
    padding-top: 3em;
  }
  .mainBanner .mainBWrap h1 {
    font-size: 2em;
  }
  .mainBtnWrap {
    margin: 1.5em 0;
  }
  .mainBtnCon {
    font-size: 0.8em;
  }
  .mainBtn a {
    align-items: flex-start;
  }
  .mainBtn a:before {
    height: 5em;
    top: 50%;
    left: 70%;
  }
  .mainBtn a.goIconPro {
    margin-right: 0.5em;
  }
  .mainBtn a.goIconCheck {
    margin-left: 0.5em;
  }
  .mainBtn a .mainBtnCon {
    padding-left: 0.5em;
  }
  .mainBtn a .mainBtnCon p {
    margin-top: 0;
    line-height: 1.3em;
  }
}
@media (max-width: 575px) {
  .mainBanner .mainBWrap {
    padding-left: 2em;
  }
  .mainBanner {
    background-position: 50% 0%;
    background-size: 200%;
  }
  .mainBanner p {
    bottom: 1em;
    font-size: 1em;
  }
  .mainBtnWrap div h2 {
    line-height: 1.2em;
  }
  .mainBtnWrap div h2 span {
    display: block;
    font-size: 0.8em;
  }
  .mainBtn a {
    height: 8em;
  }
  .mainBtn a:before {
    height: 4em;
    width: 4em;
  }
  .mainBanner .mainBWrap div span {
    font-size: 1em;
  }
  .mainBanner .mainBWrap div em {
    font-size: 1.2em;
  }
  .mainBtn a .mainBtnCon {
    padding-left: 0;
  }
}
</style>