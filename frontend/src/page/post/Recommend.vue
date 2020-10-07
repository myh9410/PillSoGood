<template>
  <div style="padding-top: 10vh">
    <h1 style="text-align: center">
      {{ this.$store.state.userInfo.username }}님을 위한 추천리스트
    </h1>
    <br />

    <br />
    <br />

    <div
      v-for="(sample, j) in functional"
      :key="j"
      style="width: 700px; height: 200px; margin: auto; margin-top: 10px"
    >
      <h3>
        <b>{{ j }}</b
        >을 위한 영양제
      </h3>
      <div style="border: solid 1px #dadada; height: 160px; margin-top: 10px">
        <VueSlickCarousel
          class="carouselContainer"
          v-bind="carouselSettings"
          style="
            width: 400px;
            height: 100px;
            margin: 20px auto;
            color: #black;
            text-align: center;
          "
        >
          <div v-for="(tonic, i) in sample" :key="i" style="height: 80px">
            <div
              style="
                width: 45px;
                height: 60px;
                margin: auto;
                text-align: center;
              "
            >
              <v-img
                :src="
                  'https://firebasestorage.googleapis.com/v0/b/pillsogood-764c8.appspot.com/o/images%2F' +
                  tonic.name +
                  '_1.jpg?alt=media'
                "
                @error="imgUrlAlt()"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                @click="goDetail(tonic)"
              ></v-img>
            </div>
            <hr />
            <h6 style="text-align: center">{{ tonic.name }}</h6>
          </div>
        </VueSlickCarousel>
      </div>
    </div>

    <h3 style="margin-top: 10px">
      {{ this.$store.state.userInfo.username }}님과 유사한 사용자들이 찾는
      영양제
    </h3>
    <div
      v-for="l in relist"
      :key="l"
      style="
        width: 700px;
        height: 160px;
        margin: auto;
        border: solid 1px #dadada;
        margin-top: 10px;
      "
    >
      <VueSlickCarousel
        class="carouselContainer"
        v-bind="carouselSettings"
        style="width: 400px; height: 100px; margin: 20px auto; color: #black"
      >
        <div v-for="(rtonic, k) in l" :key="k" style="height: 50px">
          <div style="width: 45px; height: 60px; margin: auto">
            <v-img
              :src="
                'https://firebasestorage.googleapis.com/v0/b/pillsogood-764c8.appspot.com/o/images%2F' +
                rtonic.name +
                '_1.jpg?alt=media'
              "
              @error="imgUrlAlt()"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              @click="goDetail(rtonic)"
            ></v-img>
          </div>
          <hr />
          <h6 style="text-align: center">{{ rtonic.name }}</h6>
        </div>
      </VueSlickCarousel>
    </div>
    <br /><br /><br />
  </div>
</template>
<script>
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";
import "../../assets/css/recommend.scss";
import http from "@/util/http-common";
import simage1 from "../../assets/images/noimage.gif";

export default {
  name: "Recommend",
  components: { VueSlickCarousel },
  created() {
    this.recommends();
    this.recommendsf();
  },
  data: () => ({
    checkList: [],
    relist: [],
    fkey: [],
    functional: [],
    slickOptions: {
      //  dots: true,

      touchMove: true,
      dotsClass: "slick-dots",
      autoplay: true,
      autoplaySpeed: 3000,
    },
    carouselSettings: {
      // "dots": true,
      infinite: true,
      initialSlide: 2,
      speed: 500,
      slidesToShow: 4,
      slidesToScroll: 1,
      swipeToSlide: true,
    },
  }),
  methods: {
    goDetail(sampletonic) {
      this.$router.push(`/list/${sampletonic.id}/`);
    },
    imgUrlAlt() {
      event.target.src = simage1;
    },
    recommends() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      http
        .get("/recommends/", config)
        .then((res) => {
          this.relist.push(res.data);
        })
        .catch((err) => {
          console.error(err);
        });
    },

    recommendsf() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      http
        .get("/recommends/functional/", config)
        .then((res) => {
          this.functional = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>
<style>
.slick-prev:before {
  color: black;
}

.slick-next:before {
  color: black;
}
</style>
<style scoped>
.v-responsive__content {
  height: 100px;
  padding-bottom: 0px;
}
.v-responsive__sizer {
  padding-bottom: 0px;
}
.v-image.v-responsive.theme--light {
  height: 100px;
  padding-bottom: 0px;
}
.v-image__image {
  width: 100px;
  height: 100px;
}
.v-image__image.v-image__image--cover {
  width: 100px;
  height: 100px;
}
.v-image__image--cover {
  width: 100px;
  height: 100px;
}
.v-image__placeholder {
  width: 100px;
  height: 100px;
}
</style>