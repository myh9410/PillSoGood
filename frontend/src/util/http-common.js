import axios from 'axios';

export default axios.create({
    baseURL: 'http://localhost:8000/'
    //추후 서버 url 추가필요
})