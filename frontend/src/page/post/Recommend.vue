<template>
    <div>
        <div class="checkbox">
            <!-- <p>{{checkList}}</p> -->
            <p>체크박스</p>
            <v-row justify="space-around" class="checkList">
                <v-col>
                    <v-checkbox v-model="checkList" value="활력" label="활력"></v-checkbox>
                    <v-checkbox v-model="checkList" value="체지방/혈당" label="체지방/혈당"></v-checkbox>
                </v-col>
                <v-col>
                    <v-checkbox v-model="checkList" value="스트레스/수면" label="스트레스/수면"></v-checkbox>
                    <v-checkbox v-model="checkList" value="소화기" label="소화기"></v-checkbox>
                </v-col>
                <v-col>
                    <v-checkbox v-model="checkList" value="간" label="간"></v-checkbox>
                    <v-checkbox v-model="checkList" value="치아/잇몸" label="치아/잇몸"></v-checkbox>
                </v-col>
                <v-col>
                    <v-checkbox v-model="checkList" value="면역력" label="면역력"></v-checkbox>
                    <v-checkbox v-model="checkList" value="뼈/관절" label="뼈/관절"></v-checkbox>
                </v-col>
                <v-col>
                    <v-checkbox v-model="checkList" value="눈" label="눈"></v-checkbox>
                    <v-checkbox v-model="checkList" value="두뇌/운동" label="두뇌/운동"></v-checkbox>
                </v-col>
                <v-col>
                    <v-checkbox v-model="checkList" value="심장/혈관" label="심장/혈관"></v-checkbox>
                    <v-checkbox v-model="checkList" value="피부" label="피부"></v-checkbox>
                </v-col>
            </v-row>
        </div>
        <br>
        <hr>
        <div class="d-flex" style="width:60%; margin:auto; padding:60px; padding-top:15vh;">
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
    </div>
</template>
<script>
// import http from  "@/util/http-common";
import '../../assets/css/recommend.scss'
import simage1 from "../../assets/images/sample1.png";
import simage2 from "../../assets/images/sample2.jpg";

export default {
    name: 'Recommend',
    components: {

    },
    data: () => ({
        checkList : [],
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
    }),
    methods: {
        goDetail(sampletonic) {
            this.$router.push(`/list/${sampletonic.id}/`);
        },
    }
}
</script>