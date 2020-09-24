<template>
  <div>
    <!-- <v-btn icon @click="showAlbum">
      <v-icon>mdi-view-module</v-icon>
    </v-btn>
    <v-btn icon @click="showList">
      <v-icon>mdi-view-list</v-icon>
    </v-btn>-->
    <section>
      <div class="d-flex" style="width:60%; margin:auto; padding:60px; padding-top:15vh;">
        <div class="flex">
          <h4 class="p-2 d-flex" style="font-size:30px;">영양제 리스트</h4>
        </div>
        <div class="flex">
          <v-text-field
            v-model="search"
            class="p-2 d-flex"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
        </div>
        <v-row>
          <v-col v-for="(tonic, i) in tonics" :key="i" cols="6" md="3" :search="search">
            <v-card @click="goDetail(tonic)" style="width:200px; height:250px;" :search="search">
              <!-- <div "> -->
              <v-img
                src="../../assets/images/sample1.png"
                style="width:200px; height:200px; margin:auto;"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              ></v-img>
              <!-- </div> -->
              <hr />
              <h4 style="text-align:center">{{tonic.name}}</h4>
            </v-card>
          </v-col>
        </v-row>
      </div>
    </section>

    <div class="btn-cover d-flex justify-content-center align-items-center">
      <button :disabled="pageNum === 0" @click="prevPage" class="page-btn btn btn-info m-2">
        <p>이전</p>
      </button>
      <span class="page-count m-0">
        <h4>{{ pageNum + 1 }} / 86</h4>
      </span>
      <button :disabled="pageNum >= 86" @click="nextPage" class="page-btn btn btn-info m-2">
        <p>다음</p>
      </button>
    </div>
  </div>
</template>

<script>
// import simage1 from "../../assets/images/sample1.png";
// import simage2 from "../../assets/images/sample2.jpg";
const API_BASE_URL = "http://localhost:8000";
export default {
  components: {
    // simage1
  },
  data: () => ({
    search: "",
    channel_name: "",
    tonics: [],
    pageNum: 0,

    // sampletonics: [
    //   {
    //     id: 1,
    //     name: "아이키커",
    //     src: simage1,
    //   },
    //   {
    //     id: 2,
    //     name: "솔가 비타민 B",
    //     src: simage2,
    //   },
    //   {
    //     id: 3,
    //     name: "솔가 비타민 C",
    //     src: simage2,
    //   },
    //   {
    //     id: 4,
    //     name: "솔가 비타민 D",
    //     src: simage2,
    //   },
    //   {
    //     id: 5,
    //     name: "솔가 비타민 E",
    //     src: simage2,
    //   },
    // ],
    howto: true,
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
      const API_TONIC_LIST_URL = API_BASE_URL + `/supplements/list/${page}`;
      const config = {};
      this.$axios
        .get(API_TONIC_LIST_URL, config)
        .then((res) => {
          console.log(res.data);
          this.tonics = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    nextPage() {
      this.pageNum += 1;

      this.fetchTonicList(this.pageNum);
    },
    prevPage() {
      this.pageNum -= 1;

      this.fetchTonicList(this.pageNum);
    },
  },
};
</script>

<style>
</style>