<template>
  <div style="text-align: center; padding-top: 10vh">
    <div style="width: 100vw; height: 100vh; padding: 10px; margin: 0 auto">
      <div class="row" style="margin: auto; width: 60%">
        <div
          class="col-md-5"
          style="
            text-align: center;
            margin-top: auto;
            margin-bottom: auto;

            width: 50%;
          "
        >
          <div class="center">
            <div v-if="!isImg">
              <v-carousel
                :continuous="false"
                cycle
                :show-arrows="false"
                hide-delimiter-background
                delimiter-icon="mdi-minus"
                height="300"
              >
                <v-carousel-item v-for="(slide, i) in items" :key="i">
                  <img
                    :src="slide.src"
                    @error="imgUrlAlt(slide)"
                    style="
                      border-radius: 5px;
                      text-align: center;
                      margin-top: auto;
                      margin-bottom: auto;
                      padding: 0px;
                      width: 100%;
                      height: 100%;
                    "
                  />
                </v-carousel-item>
              </v-carousel>
            </div>
          </div>
        </div>
        <div
          class="col-md-5"
          style="width: 50%; text-align: center; margin-top: 0; margin: auto"
        >
          <h1>{{ tonic.name }}</h1>
          <!-- <p>{{tonic}}</p> -->

          <table style="margin-top: 10px; text-align: left">
            <tr style="height: 50px">
              <th style="width: 100px">제조사</th>
              <td>{{ tonic.manufacturer }}</td>
            </tr>
            <tr style="height: 50px">
              <th>타입</th>
              <td>{{ tonic.product_form }}</td>
            </tr>
            <tr style="height: 50px">
              <th>복용법</th>
              <td>{{ tonic.dosage }}</td>
            </tr>
            <tr style="height: 50px">
              <th>포함된 영양소</th>
              <td>
                <v-row style="margin-left: 0px">
                  <div v-for="(nutrient, i) in tonic.nutrients" :key="i">
                    <p v-if="i == 0">{{ nutrient.name }}</p>
                    <p v-if="i != 0">, {{ nutrient.name }}</p>
                  </div>
                </v-row>
              </td>
            </tr>
            <tr style="height: 50px">
              <th>효능</th>
              <td>
                <v-row style="margin-left: 0px">
                  <div v-for="(nutrient, l) in tonic.nutrients" :key="l">
                    <v-row style="margin-left: 0px">
                      <div
                        v-for="(functional, i) in nutrient.functionals"
                        :key="i"
                      >
                        <!-- {{ functional.content }} -->
                        <p v-if="i == 0 && l == 0">{{ functional.content }}</p>
                        <p v-else>, {{ functional.content }}</p>
                      </div>
                    </v-row>
                  </div></v-row
                >
              </td>
            </tr>
            <tr>
              <th style="padding-top: 0px">주의사항</th>
              <td>
                <v-row style="margin-left: 0px">
                  <div v-for="(nutrient, i) in tonic.nutrients" :key="i">
                    <p v-if="i == 0">{{ nutrient.precaution }}</p>
                    <p v-if="i != 0">, {{ nutrient.precaution }}</p>
                  </div>
                </v-row>
              </td>
            </tr>
          </table>
        </div>
      </div>
      <section
        style="width: 100vw; padding: 10px; margin: 0 auto; text-align: center"
      >
        <div style="margin: auto; width: 60%">
          <Review />
          <br />
        </div>
        <br /><br /><br />
        <div style="margin: auto; width: 80%; text-align: left"></div>
      </section>
    </div>
  </div>
</template>

<script>
import simage1 from "../../assets/images/noimage.gif";
import Review from "../../components/post/Review";

// import axios from "axios";
const API_BASE_URL = "http://j3a506.p.ssafy.io:8000";
export default {
  data() {
    return {
      sample: { src: simage1 },
      tonic: [],
      cycle: false,
      params: this.$route.params.tonic_pk,
      tonicsrc1: "",
      tonicsrc2: "",
      tonicsrc3: "",
      tonicsrc4: "",
      isImg: true,
      items: [
        {
          src: "",
        },
        {
          src: "",
        },
        {
          src: "",
        },
        {
          src: "",
        },
      ],
    };
  },
  components: {
    Review,
  },
  created() {
    this.fetchTonic();

    // this.search()
  },
  methods: {
    fetchTonic() {
      const API_TONIC_URL = API_BASE_URL + `/supplements/${this.params}`;
      const config = {};
      this.$axios
        .get(API_TONIC_URL, config)
        .then((res) => {
          console.log(res.data);
          this.tonic = res.data;
          console.log(
            `https://firebasestorage.googleapis.com/v0/b/pillsogood-764c8.appspot.com/o/images%2F${this.tonic.name}_1.jpg?alt=media`
          );

          this.items[0].src = `https://firebasestorage.googleapis.com/v0/b/pillsogood-764c8.appspot.com/o/images%2F${this.tonic.name}_1.jpg?alt=media`;
          this.items[1].src = `https://firebasestorage.googleapis.com/v0/b/pillsogood-764c8.appspot.com/o/images%2F${this.tonic.name}_2.jpg?alt=media`;
          this.items[2].src = `https://firebasestorage.googleapis.com/v0/b/pillsogood-764c8.appspot.com/o/images%2F${this.tonic.name}_3.jpg?alt=media`;
          this.items[3].src = `https://firebasestorage.googleapis.com/v0/b/pillsogood-764c8.appspot.com/o/images%2F${this.tonic.name}_4.jpg?alt=media`;
        })
        .catch((err) => {
          console.error(err);
        });
      const cconfig = {
        apiKey: "AIzaSyB5trzHsemzlHfcwXGHXANsnRzKHSpM8Ag",
        authDomain: "pillsogood-764c8.firebaseapp.com",
        databaseURL: "https://pillsogood-764c8.firebaseio.com",
        storageBucket: "pillsogood-764c8.appspot.com",
      };
      this.$axios
        .get(
          `https://firebasestorage.googleapis.com/v0/b/pillsogood-764c8.appspot.com/o/images%2F${this.tonic.name}_1.jpg?alt=media`,
          cconfig
        )
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.error(err);
          this.isImg = false;
        });
    },
    imgUrlAlt(slide) {
      console.log("후 제발...");
      console.log(slide.src);
      slide.src = simage1;
      // slide.src= "https://firebasestorage.googleapis.com/v0/b/pillsogood-764c8.appspot.com/o/images%2FnoImage.png?alt=media"
      // event.target.src = "../../assets/images/sample1.png"
    },
    // lowprice() {
    //   var client_id = "Mke36SOHbvgzVeWWmJqV";
    //   var client_secret = "697sdPxld3";
    //   var api_url = "https://openapi.naver.com/v1/datalab/shopping/categories";
    //   var request_body = {

    //   };
    //   var options = {
    //     method: "post",
    //     url: api_url,
    //     requestBody: request_body,
    //     headers: {
    //       "X-Naver-Client-Id": client_id,
    //       "X-Naver-Client-Secret": client_secret,
    //       "Access-Control-Allow-Origin": "*",
    //     },
    //     withCredentials: true,
    //   };
    //   axios(options)
    //     .then((response) => {
    //       console.log(response.headers);
    //       // this.response = true
    //     })
    //     .catch((error) => {
    //       // console.log('my error :', error)
    //       if (error.response) {
    //         console.log("error.response.data : ", error.response.data);
    //         // console.log('error.response.status : ', error.response.status);
    //         // console.log('error.reponse.headers : ', error.response.headers);
    //       } else if (error.request) {
    //         console.log("request error: ", error.request);
    //       } else {
    //         console.log("Error", error.message);
    //       }
    //       console.log(error.config);
    //     });
    // },

    // search() {
    //   var express = require("express");
    //   var app = express();
    //   var client_id = "Mke36SOHbvgzVeWWmJqV";
    //   var client_secret = "697sdPxld3";
    //   app.get("/search/shop", function (req, res) {
    //     var api_url =
    //       "https://openapi.naver.com/v1/search/shop?query=" +
    //       encodeURI(this.tonic.name); // json 결과
    //     //   var api_url = 'https://openapi.naver.com/v1/search/blog.xml?query=' + encodeURI(req.query.query); // xml 결과
    //     var request = require("request");
    //     var options = {
    //       url: api_url,
    //       headers: {
    //         "X-Naver-Client-Id": client_id,
    //         "X-Naver-Client-Secret": client_secret,
    //       },
    //     };
    //     request.get(options, function (error, response, body) {
    //       if (!error && response.statusCode == 200) {
    //         res.writeHead(200, { "Content-Type": "text/json;charset=utf-8" });
    //         res.end(body);
    //         console.log("hi")
    //       } else {
    //         res.status(response.statusCode).end();
    //         console.log("error = " + response.statusCode);
    //       }
    //     });
    //   });
    //   app.listen(3000, function () {
    //     console.log(
    //       "http://127.0.0.1:3000/search/blog?query=검색어 app listening on port 3000!"
    //     );
    //   });
    // },
  },
};
</script>

<style>
</style>