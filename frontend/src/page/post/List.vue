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
        style="width: 60%; margin: auto; padding: 60px; padding-top: 15vh"
      >
        <div class="flex">
          <h4 class="p-2 d-flex" style="font-size: 30px; text-align: center">
            영양제 리스트
          </h4>
        </div>
        <div>
          <input
            v-model="tonicName"
            class="p-2 d-flex"
            append-icon="mdi-magnify"
            hide-details
            placeholder="검색"
            style="border: solid 1px #dadada"
          />  
          <!-- 검색창이 빈칸일떄 -->
          <div>

          <v-row>
            <v-col v-for="(tonic, i) in tonics" :key="i" cols="6" md="3">
              <v-card
                @click="goDetail(tonic)"
                style="width: 250px; height: 250px"
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

                <hr />
                <h4 style="text-align: center">{{ tonic.name }}</h4>
              </v-card>
            </v-col>
          </v-row>
        </div>

     

        </div>
      </div>
    </section>

    <div class="btn-cover d-flex justify-content-center align-items-center">
      <button
        :disabled="pageNum >= 1000"
        @click="nextPage"
        class="page-btn btn btn-info m-2"
      >
        <p>더보기</p>
      </button>
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

          for (var i = 0; i < 10; i++) {
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

<style>
</style>