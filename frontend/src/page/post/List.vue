<template>
  <div>
    <!-- <v-btn icon @click="showAlbum">
      <v-icon>mdi-view-module</v-icon>
    </v-btn>
    <v-btn icon @click="showList">
      <v-icon>mdi-view-list</v-icon>
    </v-btn>-->
    <section>
      <div
        class="d-flex"
        style="width: 80%; margin: auto; padding: 60px; padding-top: 10vh"
      >
        <div class="flex">
          <h4 class="p-2 d-flex" style="font-size: 30px; text-align: center">
            영양제 리스트
          </h4>
        </div>
        <br />
        <div>
          <div>
            <v-row>
              <v-col v-for="(tonic, i) in tonics" :key="i" md="3">
                <v-card
                  @click="goDetail(tonic)"
                  class="mx-auto"
                  max-width="374"
                  height="350"
                >
                  <v-img
                    :src="
                      'https://firebasestorage.googleapis.com/v0/b/pillsogood-764c8.appspot.com/o/images%2F' +
                      tonic.name +
                      '_1.jpg?alt=media'
                    "
                    @error="imgUrlAlt()"
                    style="width: 250px; height: 200px; margin: auto"
                    gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                  ></v-img>
                  <v-card-title text-center>{{ tonic.name }}</v-card-title>
                  <!-- <h4 style="text-align: center">{{ tonic.name }}</h4> -->
                  <!-- <v-divider class="mx-4"></v-divider> -->
                  <v-card-text class="ma-2">
                    <v-chip
                      class="ma-2"
                      style="margin: 0px 2px"
                      small
                      color="primary"
                      v-for="nutrient in tonic.nutrients"
                      :key="nutrient.id"
                      >{{ nutrient.name }}
                    </v-chip>
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </div>
        </div>
      </div>
    </section>

    <div
      class="btn-cover d-flex justify-content-center align-items-center"
      style="margin: auto; text-align: center"
    >
      <v-btn rounded x-large @click="nextPage">더보기</v-btn>
    </div>
  </div>
</template>

<script>
import http from "@/util/http-common";

import simage1 from "../../assets/images/noimage.gif";
export default {
  components: {
    // simage1
  },
  data: () => ({
    tonicName: "",
    channel_name: "",
    tonics: [],
    pageNum: 1,
    howto: true,
    listData: [],
    searchList: [],
  }),
  created() {
    this.fetchTonicList(1);
  },
  methods: {
    goDetail(tonic) {
      this.$router.push(`/list/${tonic.id}/`);
    },
    showAlbum() {
      this.howto = true;
    },
    showList() {
      this.howto = false;
    },
    fetchTonicList(page) {
      const config = {};
      http
        .get(`/supplements/list/${page}`, config)
        .then((res) => {
          // console.log(res.data);

          for (var i = 0; i < 8; i++) {
            this.tonics.push(res.data[i]);
          }
          // console.log(this.tonics);
        })
        .catch((err) => {
          console.error(err);
        });
    },

    nextPage() {
      this.pageNum += 1;

      this.fetchTonicList(this.pageNum);
    },

    handleSearchInput(e) {
      this.search = e.target.value;
      if (this.search.length !== 0) {
        clearTimeout(this.debounce);
        this.debounce = setTimeout(() => {
          const filteredList = this.tonics.filter((tonic) =>
            tonic.title.includes(this.search)
          );
          this.searchList = filteredList;
        }, 500);
      } else {
        clearTimeout(this.debounce);
        this.debounce = setTimeout(() => {
          this.searchList = [];
        }, 500);
      }
    },
    imgUrlAlt() {
      event.target.src = simage1;
    },
  },
};
</script>

<style scoped>
.theme--light.v-chip:not(.v-chip--active) {
  background-color: #aed2a3;
}

.v-card__title + .v-card__subtitle,
.v-card__title + .v-card__text {
  padding-top: 16px;
}
</style>