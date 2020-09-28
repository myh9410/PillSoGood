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
    </div>

    <div class="buttons">
      <!-- @click="onList" -->
      <v-btn class="pillList" large color="#BCAAA4">제품 보기</v-btn>
      <v-btn class="recommend" large color="#BCAAA4">영양제 추천</v-btn>
    </div>

    <div class="products">
      <vueper-slides fade :touchable="false" autoplay arrows-outside>
        <vueper-slide v-for="(sampletonic, i) in sampletonics" :key="i" :title="sampletonic.name" :image="sampletonic.src" />
      </vueper-slides>
    </div>
  </div>
</template>

<script>
import 'vueperslides/dist/vueperslides.css'
import '../assets/css/home.scss'
import { VueperSlides, VueperSlide } from 'vueperslides'
import simage1 from "../assets/images/sample1.png";
import simage2 from "../assets/images/sample2.jpg";
// import http from  "@/util/http-common"
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
    VueperSlides,
    VueperSlide
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
