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
          <v-col v-for="(sampletonic, i) in sampletonics" :key="i" cols="6" md="3" :search="search">
            <v-card
              @click="goDetail(sampletonic)"
              style="width:200px; height:250px;"
              :search="search"
            >
              <!-- <div "> -->
              <v-img
                :src="sampletonic.src"
                style="width:200px; height:200px; margin:auto;"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              ></v-img>
              <!-- </div> -->
              <hr />
              <h4 style="text-align:center">{{sampletonic.name}}</h4>
            </v-card>
          </v-col>
        </v-row>
      </div>
    </section>
  </div>
</template>

<script>
import simage1 from "../../assets/images/sample1.png";
import simage2 from "../../assets/images/sample2.jpg";
export default {
  data: () => ({
    search: "",
    channel_name: "",
    tonics: [],
    sampletonics: [
      {
        id: 1,
        name: "아이키커",
        src: simage1,
      },
      {
        id: 2,
        name: "솔가 비타민 B",
        src: simage2,
      },
      {
        id: 3,
        name: "솔가 비타민 C",
        src: simage2,
      },
      {
        id: 4,
        name: "솔가 비타민 D",
        src: simage2,
      },
      {
        id: 5,
        name: "솔가 비타민 E",
        src: simage2,
      },
    ],
    howto: true,
  }),
  methods: {
    goDetail(sampletonic) {
      this.$router.push(`/list/${sampletonic.id}/`);
    },
    showAlbum() {
      this.howto = true;
    },
    showList() {
      this.howto = false;
    },
  },
};
</script>

<style>
</style>