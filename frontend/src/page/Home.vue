<template>
  <div class="home">
    <div class="explanation">
      <img src="../../src/assets/images/main_640.png"/>
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
      제품보기, 설명
    </div>
  </div>
</template>

<script>
import '../assets/css/home.scss'
// import http from  "@/util/http-common"
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
    
  }
}
</script>
