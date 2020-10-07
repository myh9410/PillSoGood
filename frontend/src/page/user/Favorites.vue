<template>
  <div style="text-align: center; padding-top: 10vh" class="form">
    <h1>평소 관심있는 건강 항목을 선택해주세요!</h1>
    <br />
    <br />
    <h3>{{ user }}님을 위한 맞춤 추천에 도움 이 됩니다</h3>
    <h4>최대 3개까지 선택할 수 있어요!</h4>
    <h5>(선택하지 않으셔도 됩니다!)</h5>
    <br />
    <br />
    <v-row justify="space-around" class="checkList">
      <v-col>
        <div
          v-for="item in list.slice(0, 4)"
          v-bind:key="item.id"
          class="list1"
        >
          <button
            @click="addFavorites(item.idx, item.id)"
            :class="`${item.id}`"
            :style="item.status ? on : off"
          >
            <img :src="item.link" />
            <br />
            {{ item.value }}
          </button>
        </div>
      </v-col>
      <v-col>
        <div
          v-for="item in list.slice(4, 8)"
          v-bind:key="item.id"
          class="list2"
        >
          <button
            @click="addFavorites(item.idx, item.id)"
            :class="`${item.id}`"
            :style="item.status ? on : off"
          >
            <img :src="item.link" />
            <br />
            {{ item.value }}
          </button>
        </div>
      </v-col>
      <v-col>
        <div
          v-for="item in list.slice(8, 12)"
          v-bind:key="item.id"
          class="list3"
        >
          <button
            @click="addFavorites(item.idx, item.id)"
            :class="`${item.id}`"
            :style="item.status ? on : off"
          >
            <img :src="item.link" />
            <br />
            {{ item.value }}
          </button>
        </div>
      </v-col>
      <v-col>
        <div
          v-for="item in list.slice(12, 16)"
          v-bind:key="item.id"
          class="list4"
        >
          <button
            @click="addFavorites(item.idx, item.id)"
            :class="`${item.id}`"
            :style="item.status ? on : off"
          >
            <img :src="item.link" />
            <br />
            {{ item.value }}
          </button>
        </div>
      </v-col>
      <v-col>
        <div
          v-for="item in list.slice(16, 20)"
          v-bind:key="item.id"
          class="list5"
        >
          <button
            @click="addFavorites(item.idx, item.id)"
            :class="`${item.id}`"
            :style="item.status ? on : off"
          >
            <img :src="item.link" />
            <br />
            {{ item.value }}
          </button>
        </div>
      </v-col>
    </v-row>
    <br />
    <div class="submit" v-if="favorites.length <= 3">
      <v-btn
        style="
          width: 200px;
          background-color: #5aa6ee;
          color: white;
          font-size: 20px;
        "
        rounded
        x-large
        @click="sendFavorites"
        >등록</v-btn
      >
    </div>

    <!-- <v-col>
        <div
          v-for="item in list.slice(4, 8)"
          v-bind:key="item.id"
          class="list2"
        >
          <button
            @click="addFavorites(item.idx, item.id)"
            :class="`${item.id}`"
            :style="item.status ? on : off"
          >
            <img :src="item.link" />
            <br />
            {{ item.value }}
          </button>
        </div>
      </v-col>
      <v-col>
        <div
          v-for="item in list.slice(8, 12)"
          v-bind:key="item.id"
          class="list3"
        >
          <button
            @click="addFavorites(item.idx, item.id)"
            :class="`${item.id}`"
            :style="item.status ? on : off"
          >
            <img :src="item.link" />
            <br />
            {{ item.value }}
          </button>
        </div>
      </v-col>
      <v-col>
        <div
          v-for="item in list.slice(12, 16)"
          v-bind:key="item.id"
          class="list4"
        >
          <button
            @click="addFavorites(item.idx, item.id)"
            :class="`${item.id}`"
            :style="item.status ? on : off"
          >
            <img :src="item.link" />
            <br />
            {{ item.value }}
          </button>
        </div>
      </v-col>
      <v-col>
        <div
          v-for="item in list.slice(16, 20)"
          v-bind:key="item.id"
          class="list5"
        >
          <button
            @click="addFavorites(item.idx, item.id)"
            :class="`${item.id}`"
            :style="item.status ? on : off"
          >
            <img :src="item.link" />
            <br />
            {{ item.value }}
          </button>
        </div>
      </v-col>

    <br />
    <div class="submit" v-if="favorites.length <= 3">
      <v-btn rounded x-large @click="sendFavorites">추가</v-btn>
    </div> -->
  </div>
</template>
<script>
import swal from "sweetalert";
import "../../assets/css/favorites.scss";
import http from "@/util/http-common";
export default {
  name: "favorites",
  components: {},
  data: () => {
    return {
      list: [
        {
          idx: 0,
          id: 1,
          value: "면역",
          status: false,
          link: require("../../assets/images/favorites/1.png"),
        },
        {
          idx: 1,
          id: 2,
          value: "혈관",
          status: false,
          link: require("../../assets/images/favorites/2.png"),
        },
        {
          idx: 2,
          id: 3,
          value: "혈당",
          status: false,
          link: require("../../assets/images/favorites/3.png"),
        },
        {
          idx: 3,
          id: 4,
          value: "피로감",
          status: false,
          link: require("../../assets/images/favorites/4.png"),
        },
        {
          idx: 4,
          id: 5,
          value: "기억력",
          status: false,
          link: require("../../assets/images/favorites/5.png"),
        },
        {
          idx: 5,
          id: 6,
          value: "피부",
          status: false,
          link: require("../../assets/images/favorites/6.png"),
        },
        {
          idx: 6,
          id: 7,
          value: "간",
          status: false,
          link: require("../../assets/images/favorites/7.png"),
        },
        {
          idx: 7,
          id: 8,
          value: "위",
          status: false,
          link: require("../../assets/images/favorites/8.png"),
        },
        {
          idx: 8,
          id: 9,
          value: "체지방",
          status: false,
          link: require("../../assets/images/favorites/9.png"),
        },
        {
          idx: 9,
          id: 10,
          value: "장",
          status: false,
          link: require("../../assets/images/favorites/10.png"),
        },
        {
          idx: 10,
          id: 11,
          value: "눈",
          status: false,
          link: require("../../assets/images/favorites/11.png"),
        },
        {
          idx: 11,
          id: 12,
          value: "운동",
          status: false,
          link: require("../../assets/images/favorites/12.png"),
        },
        {
          idx: 12,
          id: 13,
          value: "뼈",
          status: false,
          link: require("../../assets/images/favorites/13.png"),
        },
        {
          idx: 13,
          id: 17,
          value: "치아",
          status: false,
          link: require("../../assets/images/favorites/17.png"),
        },
        {
          idx: 14,
          id: 18,
          value: "코",
          status: false,
          link: require("../../assets/images/favorites/18.png"),
        },
        {
          idx: 15,
          id: 19,
          value: "수면",
          status: false,
          link: require("../../assets/images/favorites/19.png"),
        },
        {
          idx: 16,
          id: 20,
          value: "신장",
          status: false,
          link: require("../../assets/images/favorites/20.png"),
        },
        {
          idx: 17,
          id: 22,
          value: "신진대사",
          status: false,
          link: require("../../assets/images/favorites/22.png"),
        },
        {
          idx: 18,
          id: 23,
          value: "갑상선",
          status: false,
          link: require("../../assets/images/favorites/23.png"),
        },
      ],
      favorites: [],
      checker: false,
      user: "",
      on: {
        opacity: 1.0,
        backgroundColor: "#eebb4d",
        outline: "none",
      },
      off: {
        opacity: 0.7,
        backgroundColor: "white",
        outline: "none",
      },
    };
  },
  beforeMount() {
    this.user = this.$store.state.userInfo.username;
  },
  methods: {
    addFavorites(idx, id) {
      // console.log(id);
      if (this.list[idx].status) {
        this.list[idx].status = !this.list[idx].status;
        this.favorites.splice(this.favorites.indexOf(id), 1);
      } else {
        if (this.favorites.length === 3) {
          swal("증상은 최대 3개까지 선택할 수 있습니다");
        } else {
          this.list[idx].status = !this.list[idx].status;
          this.favorites.push(id);
        }
      }
    },
    sendFavorites() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      http
        .post(
          "accounts/interest/",
          {
            interests: this.favorites,
          },
          config
        )
        .then(() => {
          // console.log(this.$store.state.userInfo);
          swal("관심증상이 등록되었습니다");
          this.$router.push("/");
        });
    },
  },
};
</script>
