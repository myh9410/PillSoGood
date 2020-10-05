<template>
  <div>
    <div style="width: 100vw; height: 100vh; padding: 10px; margin: 0 auto">
      <div
        class="row justify-content-between flex"
        style="margin: auto; width: 80%"
      >
        <div
          class="col-md-5"
          style="
            text-align: center;
            margin-top: auto;
            margin-bottom: auto;
            padding: 20vh;
            padding: 5vw;
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
                      text-align: center;
                      margin-top: auto;
                      margin-bottom: auto;
                      margin-left: 50px;
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
          style="
            width: 40%;
            text-align: center;
            margin-top: 0;
            margin-bottom: auto;
            padding: 20vh;
            padding: 5vw;
          "
        >
          <h1>{{ tonic.name }}</h1>
          <!-- <p>{{tonic}}</p> -->

          <table style="margin-top: 100px; text-align: left">
            <tr>
              <th>제조사</th>
              <td>{{ tonic.manufacturer }}</td>
            </tr>
            <tr>
              <th>타입</th>
              <td>{{ tonic.product_form }}</td>
            </tr>
            <tr>
              <th>복용법</th>
              <td>{{ tonic.dosage }}</td>
            </tr>
          </table>
        </div>
      </div>
      <section
        style="width: 100vw; padding: 10px; margin: 0 auto; text-align: center"
      >
        <div style="margin: auto; width: 60%">
          <h2>포함된 영양소</h2>
          <br />
          <!-- <p>{{ tonic.nutrients }}</p> -->
          <v-row style="margin-left: 20px;height:200px; text-align: center; background-color:#dadada;">
            <div v-for="(nutrient, i) in tonic.nutrients" :key="i">
              <p v-if="i == 0">{{ nutrient.name }}</p>
              <p v-if="i != 0">, {{ nutrient.name }}</p>
            </div>
          </v-row>
          <br />
          <br />
          <h2>효능</h2>
          <v-row style="margin-left: 20px; height:200px; background-color:#dadada;">
            <div v-for="(nutrient, l) in tonic.nutrients" :key="l">
              <v-row style="margin-left:0px">
                <div v-for="(functional, i) in nutrient.functionals" :key="i">
                  <!-- {{ functional.content }} -->
                  <p v-if="i == 0 && l == 0">{{ functional.content }}</p>
                  <p v-else>, {{ functional.content }}</p>
                </div>
              </v-row>
            </div></v-row
          >

          <h2>주의사항</h2>
          <v-row style="margin-left: 20px; background-color:#dadada;height:200px;">
            <div v-for="(nutrient, i) in tonic.nutrients" :key="i">
              <p v-if="i == 0">{{ nutrient.precaution }}</p>
              <p v-if="i != 0">, {{ nutrient.precaution }}</p>
            </div>
          </v-row>

          <br />
        </div>
        <br/><br/><br/>
        <div style="margin: auto; width: 80%; text-align:left;">
          <Review />
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import simage1 from "../../assets/images/noimage.gif";
import Review from "../../components/post/Review";

// import axios from "axios";
const API_BASE_URL = "http://localhost:8000";
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