<template>
  <div data-app>
    <h1 style="text-align: left">리뷰</h1>
    <br />
    <star-rating v-model="ReviewInfo.rank" />

    <br />
    <input
      v-model="ReviewInfo.title"
      style="border: solid 1px #dadada; width: 400px; float: left"
      type="text"
      placeholder="제목"
    />
    <input
      v-model="ReviewInfo.content"
      class="text-sm-left"
      type="text"
      style="border: solid 1px #dadada; height: 100px"
      placeholder="한줄평 남기기"
    />
    <button @click="createReview" style="border: solid 1px #dadada" class="btn">
      작성
    </button>
    <table class="table">
      <tbody>
        <div v-for="review in Review_list" :key="review.id">
          <div style="background-color: #dadada; width: 59vw; text-align: left">
            <div style="width: 200px">
              <h3 style="float: left; margin-right: 5px">
                {{ review.user.username }}님
              </h3>

              <div style="color: orange">
                <p v-if="review.rank == 0">☆☆☆☆☆</p>
                <p v-if="review.rank == 1">★☆☆☆☆</p>
                <p v-if="review.rank == 2">★★☆☆☆</p>
                <p v-if="review.rank == 3">★★★☆☆</p>
                <p v-if="review.rank == 4">★★★★☆</p>
                <p v-if="review.rank == 5">★★★★★</p>
              </div>
              <time :datetime="review.created_at" />
            </div>
            <br />

            <h3 style="text-align: left">{{ review.title }}</h3>
            <p>{{ review.content }}</p>
            <div
              v-if="review.user.username == nname"
              style="width: 300px; text-align: center"
            >
              <p
                style="width: 30%; cursor: pointer"
                class="btn"
                @click.stop="dialog = true"
              >
                수정
              </p>
              <v-dialog v-model="dialog" max-width="290">
                <v-card>
                  <input
                    :placeholder="review.title"
                    class="headline"
                    v-model="UpdateInfo.title"
                  />
                  <star-rating v-model="UpdateInfo.rank" :star-size="20" />

                  <input
                    :placeholder="review.content"
                    v-model="UpdateInfo.content"
                  />

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                      color="green darken-1"
                      text
                      @click="updateReview(review)"
                    >
                      수정
                    </v-btn>
                    <v-btn color="green darken-1" text @click="dialog = false">
                      취소
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>

              <p
                @click="deleteReview(review)"
                style="width: 30%; cursor: pointer"
                class="btn"
              >
                삭제
              </p>
            </div>
          </div>
          <br />
          <br />
        </div>
      </tbody>
    </table>
  </div>
</template>

<script>
import store from "@/store.js";
import StarRating from "vue-star-rating";
import http from "@/util/http-common";

export default {
  data() {
    return {
      nname: "",
      ReviewInfo: {
        title: "",
        rank: "",
        content: "",
      },
      UpdateInfo: {
        title: "",
        rank: "",
        content: "",
      },
      dialog: false,
      Review_list: [],
      params: this.$route.params.tonic_pk,
    };
  },
  components: {
    StarRating,
  },

  methods: {
    createReview() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      http
        .post(`/reviews/${this.params}/`, this.ReviewInfo, config)
        .then(() => {
          console.log(this.ReviewInfo);
          this.ReviewInfo.title = "";
          this.ReviewInfo.rank = 0;
          this.ReviewInfo.content = "";

          this.fetchReviewList();
        })
        .catch((err) => {
          console.log(this.ReviewInfo);
          console.error(err);
        });
    },
    deleteReview(review) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      http.delete(`/reviews/${review.id}/`, config).then(() => {
        console.log(review);

        this.fetchReviewList();
      });
    },
    updateReview(review) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      http
        .put(`/reviews/${review.id}/`, this.UpdateInfo, config)
        .then(() => {
          // console.log(this.ReviewInfo);
          this.UpdateInfo.title = "";
          this.UpdateInfo.rank = 0;
          this.UpdateInfo.content = "";
          this.dialog = false;
          this.fetchReviewList();
        })
        .catch((err) => {
          // console.log(this.ReviewInfo);
          console.error(err);
        });
    },
    fetchReviewList() {
      const config = {};
      http
        .get(`/reviews/${this.params}/`, config)
        .then((res) => {
          this.Review_list = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.fetchReviewList();

    this.nname = store.state.userInfo.username;
  },
};
</script>

<style>
</style>