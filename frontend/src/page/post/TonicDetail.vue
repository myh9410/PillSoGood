<template>
  <div>
    <section style="width: 100vw; height: 100vh; padding: 10px; margin: 0 auto">
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
          <div style="width: 80%" class="center">
            <v-img
              src="../../assets/images/sample1.png"
              style="
                text-align: center;
                margin-top: auto;
                margin-bottom: auto;
                margin-left: 50px;
                padding: 0px;
              "
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            ></v-img>
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

          <dl class="product-table">
            <dt>제조사</dt>
            <dd>{{ tonic.manufacturer }}</dd>
            <dt>타입</dt>
            <dd>{{ tonic.product_form }}</dd>
          </dl>
        </div>
      </div>
      <section
        style="width: 100vw; height: 100vh; padding: 10px; margin: 0 auto"
      >
        <div style="margin: auto; width: 80%">
          <h2>포함된 영양소</h2>
          <br />
          <v-row style="margin-left: 20px">
            <div v-for="(nutrient, i) in tonic.nutrients" :key="i">
              <p v-if="i == 0">{{ nutrient.name }}</p>
              <p v-if="i != 0">, {{ nutrient.name }}</p>

              <!-- <v-col v-for="(functional, i) in nutrient.functionals" :key="i" >
               <p>{{functional.category}}</p>
               
              </v-col>-->
            </div>
          </v-row>
        </div>
        <div style="margin: auto; width: 80%">
          <Review />
        </div>
      </section>
    </section>
  </div>
</template>

<script>
import simage1 from "../../assets/images/sample1.png";
import Review from "../../components/post/Review";
// import axios from "axios";
const API_BASE_URL = "http://localhost:8000";
export default {
  data() {
    return {
      sample: { name: "아이키커", effect: "뼈 발달에 좋다", src: simage1 },
      tonic: [],
      params: this.$route.params.tonic_pk,
      tonicsrc: "",
    };
  },
  components: {
    Review,
  },
  created() {
    this.fetchTonic();
    this.tonicsrc = `https://firebasestorage.googleapis.com/v0/b/pillsogood-764c8.appspot.com/o/images%2F${this.tonic.name}_1.jpg?alt=media`;
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
        })
        .catch((err) => {
          console.error(err);
        });
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