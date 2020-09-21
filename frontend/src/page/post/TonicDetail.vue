<template>
  <div>
    
    <section
      style="width: 100vw;
            height: 100vh;
            padding: 10px;
            margin:0px;
            "
      class="white--text d-flex"
    >
      <div
        class="d-flex"
        style="width:40%; text-align: center; margin-top: auto; margin-bottom:auto; padding:20vh; padding:5vw "
      >
        <v-img
        class="d-flex"
          :src="sample.src"
          style="text-align: center; margin-top: auto; margin-bottom:auto; padding:20vh; padding:5vw "
          gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
        ></v-img>
      </div>
      <div class="d-flex" style="width:40%; text-align: center; margin-top: auto; margin-bottom:auto; padding:20vh; padding:5vw " >
    <h1>상품 정보</h1>
    <dl class="product-table">
      <dt>상품 이름</dt>
      <dd>{{ sample.name }}</dd>
      <dt>효능</dt>
      <dd>{{ sample.effect }}</dd>
      
    </dl>
  </div>
      <!-- <div
        class="d-flex"
        style="width:40%; padding:20vh; padding:10vw; margin:0px; "
      >
        {{sample.name}}
        {{ $route.sampletonic_pk }}
      </div> -->
    </section>
    
  </div>
</template>

<script>
import simage1 from "../../assets/images/sample1.png";
export default {
  data: () => ({
    sample: { name: "아이키커", effect:"뼈 발달에 좋다" ,src: simage1 },
  }),
};
</script>

<style>
</style>