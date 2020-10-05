<template>
  <div class="home">
       <section
      id="Second"
      style="width: 100vw;
            height: 500px;
            background-color: #f5f1da;"
      class="white--text box2"
    >
      <div
 
        style="width:50%; text-align: center; margin-top: auto; margin-bottom:auto; padding:20vh; padding:5vw; float:left "
      >
        <h4 style=" font-size:30px; line-height:150%;">
          나만의 영양제를 한눈에 <br/>
          
        </h4>
        <div class="description2">
        <p>약 <b>3만개</b>의 영양제 중에, <br>내게 맞는 조합을 추천해줘요!</p>
      </div>
        <div class="buttons">
          <a href="/list">제품 보기</a>
          <a href="/recommend">영양제 추천</a>
      </div>
      </div>
      <div style="width:50%; padding-top:0px; padding:10vw; margin-top:0px; float:right;">
        <img style="width:100%; float:right; opacity:0.7" src="../../src/assets/images/main.png"/>
      </div>
    </section>

    <!-- <div class="explanation" style="width: 100vw; top:0;">
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
    </div> -->
    <br>
    <section>
      <div class="catchphrase">
        <div class="s1">
          <h3>Pill So Good은</h3>
        </div>
        <v-row>
          <v-col>
            문구 1
          </v-col>
          <v-col>
            문구 2
          </v-col>
          <v-col>
            문구 3
          </v-col>
        </v-row>
      </div>
    </section>
    <br>
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




