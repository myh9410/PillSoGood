<template>
  <div>
    <h1>리뷰</h1>
    <select v-model="ReviewInfo.rate">
      <option disabled value="">Please select one</option>
      <option value=0>☆☆☆☆☆</option>
      <option value=1>★☆☆☆☆</option>
      <option value=2>★★☆☆☆</option>
      <option value=3>★★★☆☆</option>
      <option value=4>★★★★☆</option>
      <option value=5>★★★★★</option>
    </select>
    <input v-model="ReviewInfo.content" type="text" placeholder="한줄평 남기기">
    <button @click="createReview" class="btn">작성</button>
    <table class="table">

      <tbody>
         <tr v-for="review in Review_list" :key="review.id" > 
          <td>{{review.title}}</td>
          <td>{{review.rate}}</td>
          <td>{{review.content}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
const API_BASE_URL = 'http://localhost:8000'
export default {
  data() {
    return {
      ReviewInfo: {
        title: '',
        rate: '',
        content: '',
      },
      Review_list:[],
      params: this.$route.params.tonic_pk,
    }
  },
  
  methods: {
    createReview() {
      const API_REVIEW_CREATE_URL = API_BASE_URL + `/reviews/${this.params}/`
      const config = {
      headers: {
                Authorization: `Token ${this.$cookies.get('auth-token')}`
              }
      }
      this.$axios.post(API_REVIEW_CREATE_URL, this.RevoewInfo, config)
        .then(() => {
          console.log(this.ReviewInfo)
          this.fetchReviewList()
        })
        .catch(err => {
          console.error(err)
          
        })
    },
    fetchReviewList() {
      const API_REVIEW_LIST_URL = API_BASE_URL + `/reviews/${this.params}/`
      const config = {}
      this.$axios.get(API_REVIEW_LIST_URL,config)
        .then(res => {
          this.Review_list = res.data
        })
        .catch(err => {
          console.error(err)
        })
    },
  },
  created() {
    this.fetchReviewList()

  },
}
</script>

<style>

</style>