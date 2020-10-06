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
      <vueper-slides fade :touchable="false" autoplay arrows-outside>
        <vueper-slide v-for="(sampletonic, i) in sampletonics" :key="i" :title="sampletonic.name" :image="sampletonic.src" />
      </vueper-slides>
    </div>
    <div class="products-logout" v-else>
      로그인을 통해 <br>
      나를 위한 비타민들을 <br>
      확인해보세요!
    </div>
  </div>
</template>

<script>
import 'vueperslides/dist/vueperslides.css'
import '../assets/css/home.scss'
import { VueperSlides, VueperSlide } from 'vueperslides'
import simage1 from "../assets/images/sample1.png";
import simage2 from "../assets/images/sample2.jpg";
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
        console.log(res);
      })
    }
  },
  data: ()=> ({
    sampletonics: [
      {
        id: 1,
        name: "아이키커",
        src: simage1,
      },
      {
        id: 2,
        name: "솔가 비타민 B",
        src: simage2,
      },
      {
        id: 3,
        name: "솔가 비타민 C",
        src: simage2,
      },
      {
        id: 4,
        name: "솔가 비타민 D",
        src: simage2,
      },
      {
        id: 5,
        name: "솔가 비타민 E",
        src: simage2,
      },
    ]
  })
}
</script>