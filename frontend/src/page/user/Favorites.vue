<template>
    <div class="form">
        <h2>평소 관심있는 건강 항목을 선택해주세요!</h2>
        <h3>user님을 위한 맞춤 추천에 도움이 됩니다</h3>
        {{favorites}}
            <v-row justify="space-around" class="checkList">
                    <v-col>
                        <div v-for="item in list.slice(0,4)" v-bind:key="item.id" class="list1">
                            <button @click="addFavorites(item.id)">
                                <img :src=item.link />
                                <br>
                                {{item.value}}
                            </button>
                        </div>
                    </v-col>
                    <v-col>
                        <div v-for="item in list.slice(4,8)" v-bind:key="item.id" class="list2">
                            <button @click="addFavorites(item.id)">
                                <img :src=item.link />
                                <br>
                                {{item.value}}
                            </button>
                        </div>
                    </v-col>
                    <v-col>
                        <div v-for="item in list.slice(8,12)" v-bind:key="item.id" class="list3">
                            <button @click="addFavorites(item.id)">
                                <img :src=item.link />
                                <br>
                                {{item.value}}
                            </button>
                        </div>
                    </v-col>
                    <v-col>
                        <div v-for="item in list.slice(12,16)" v-bind:key="item.id" class="list4">
                            <button @click="addFavorites(item.id)">
                                <img :src=item.link />
                                <br>
                                {{item.value}}
                            </button>
                        </div>
                    </v-col>
                    <v-col>
                        <div v-for="item in list.slice(16,20)" v-bind:key="item.id" class="list5">
                            <button @click="addFavorites(item.id)">
                                <img :src=item.link />
                                <br>
                                {{item.value}}
                            </button>
                        </div>
                    </v-col>
            </v-row>
            <v-btn>추가</v-btn>
    </div>
</template>
<script>
import '../../assets/css/favorites.scss'
export default {
    name: "favorites",
    components: {},
    data: () => {
        return {
            list : [
                {id : 1, value : "면역", status : false, link : require('../../assets/images/favorites/1.png')},
                {id : 2, value : "혈관", status : false, link : require('../../assets/images/favorites/2.png')},
                {id : 3, value : "혈당", status : false, link : require('../../assets/images/favorites/3.png')},
                {id : 4, value : "피로감", status : false, link : require('../../assets/images/favorites/4.png')},
                {id : 5, value : "기억력", status : false, link : require('../../assets/images/favorites/5.png')},
                {id : 6, value : "피부", status : false, link : require('../../assets/images/favorites/6.png')},
                {id : 7, value : "간", status : false, link : require('../../assets/images/favorites/7.png')},
                {id : 8, value : "위", status : false, link : require('../../assets/images/favorites/8.png')},
                {id : 9, value : "체지방", status : false, link : require('../../assets/images/favorites/9.png')},
                {id : 10, value : "장", status : false, link : require('../../assets/images/favorites/10.png')},
                {id : 11, value : "눈", status : false, link : require('../../assets/images/favorites/11.png')},
                {id : 12, value : "운동", status : false, link : require('../../assets/images/favorites/12.png')},
                {id : 13, value : "뼈", status : false, link : require('../../assets/images/favorites/13.png')},
                {id : 17, value : "치아", status : false, link : require('../../assets/images/favorites/17.png')},
                {id : 18, value : "코", status : false, link : require('../../assets/images/favorites/18.png')},
                {id : 19, value : "수면", status : false, link : require('../../assets/images/favorites/19.png')},
                {id : 20, value : "신장", status : false, link : require('../../assets/images/favorites/20.png')},
                {id : 22, value : "신진대사", status : false, link : require('../../assets/images/favorites/22.png')},
                {id : 23, value : "갑상선", status : false, link : require('../../assets/images/favorites/23.png')},
            ],
            favorites : [],
            checker : false,
        }
    }, 
    methods: {
        addFavorites(id) {
            if (!this.list[id-1].status) this.favorites.push(id);
            else this.favorites.splice(this.favorites.indexOf(id),1);
            this.list[id-1].status = !this.list[id-1].status;
        }
    } 
}
</script>
