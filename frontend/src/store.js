import Vue from 'vue';
import Vuex from 'vuex';
// import router from './router/index.js'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex);

export default new Vuex.Store({
    plugins: [createPersistedState()],
    state: {
        token: '',
        role:'',
        isLogged: false,
        userData:{
            username:'',
            password:'',
            gender:'',
            birthday:'',
            email:'',
            name:'',            
        },
        userInfo:{}
    },
    mutations:{
        mutateIsLogin(state, isLogin){
            state.isLogged = isLogin;
        },
        mutateUserInfo(state, userInfo){
            state.userInfo = userInfo;
        }
    },

    getters: {
        userInfo(state){
            return state.userInfo;
        }
    },
    actions: {
        login(context, user) {
            console.log(user);
            context.commit('mutateIsLogin', true);
            context.commit('mutateUserInfo', user);
        },
        logout(context){
            context.commit('mutateIsLogin',false);
            context.commit('mutateUserInfo',{});
            alert("로그아웃 되었습니다.");
        }
    }
})