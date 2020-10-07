<template>
  <div class="home">
    <div class="explanation">
      <img src="../../src/assets/images/main.png"/>
      <div class="description1">
        <p>나만의 영양제를<br>한눈에</p>
      </div>
      <div class="description2">
        <p>약 <b>3만개</b>의 영양제 중에, <br>내게 맞는 조합을 추천해줘요!</p>
      </div>
      <div class="buttons">
          <a href="/list">제품 보기</a>
          <a href="/recommend">영양제 추천</a>
      </div>
    </div>
    <br>
    <section>
      <div class="catchphrase">
        <div class="s1">
          <h2>Pill So Good은</h2>
        </div>
        <v-row>
          <v-col>
            <img src="../assets/images/algorithm.png" style="width : 100px; height : 100px; margin-bottom : 10px" /><br>
            <h3>
            관심항목 기반의<br>
            추천 알고리즘!
            </h3>
          </v-col>
          <v-col>
            <img src="../assets/images/supplement.png" style="width : 100px; height : 100px; margin-bottom : 10px" /><br>
            <h3>
            내게 맞는<br>
            나를 위한 영양제!
            </h3>
          </v-col>
          <v-col>
            <img src="../assets/images/nutrient.png" style="width : 100px; height : 100px; margin-bottom : 10px" /><br>
            <h3>
            영양제의 성분까지<br>
            한눈에!
            </h3>
          </v-col>
        </v-row>
      </div>
    </section>
    <br>
    <div class="products-login" v-if="this.$store.state.isLogged">
      <vueper-slides fade :touchable="false" autoplay arrows-outside fractions progress :parallax="parallax" :parallax-fixed-content="parallaxFixedContent">
        <vueper-slide v-for="recommend in recommends" :key="recommend.id" :title="recommend.name" :image="recommend.src" style="margin : auto; width : 30%; height : 50%"/>
      </vueper-slides>
    </div>
    <div class="products-logout" v-else>
      로그인을 통해 <br>
      나를 위한 비타민들을 <br>
      확인해보세요!<br><br><br>
       <v-btn rounded x-large @click="toLogin">로그인</v-btn>
    </div>
    <div class="reviews" v-if="reviews.length != 0">
      <h1>최신 리뷰들</h1>
      <br>
      <vueper-slides fade :touchable="false" autoplay arrows-outside fractions progress>
        <vueper-slide v-for="review in reviews" :key="review.id" :title="review.user.username" :content="review.content" />
      </vueper-slides>
    </div>
  </div>
</template>

<script>
import 'vueperslides/dist/vueperslides.css'
import '../assets/css/home.scss'
import { VueperSlides, VueperSlide } from 'vueperslides'
import http from  "@/util/http-common"
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
    VueperSlides,
    VueperSlide
  },
  mounted() {
    if (this.$store.state.isLogged){
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      http.get('recommends/', config)
      .then(res => {
        if (res.data.length > 10) {
          this.recommends = res.data.splice(0,10);
        } else {
            this.recommends = res.data;
        }
        for (let i = 0; i < this.recommends.length; i++){
          this.recommends[i].src = "https://firebasestorage.googleapis.com/v0/b/pillsogood-764c8.appspot.com/o/images%2F" + this.recommends[i].name +"_1.jpg?alt=media";
        }
      });
    }
    http.get('reviews/')
    .then(res => {
      if (res.data.length > 10) {
        this.reviews = res.data.splice(0,10);
      } else {
        this.reviews = res.data;
      }
    });
  },
  data: ()=> ({
    recommends : [],
    reviews : [],
    parallax: 1,
    parallaxFixedContent : false
  }),
  methods : {
    toLogin() {
      this.$router.push("/user/login")
    }
  }
}
</script>