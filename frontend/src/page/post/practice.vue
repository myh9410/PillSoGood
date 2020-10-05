<template>
  <div id="app">
  <input type="text" v-model="carName" placeholder="검색할 차 이름"/>
  <ul>
      <li v-for="(car, i) in cars" :key="i" >
      <p v-if="car.name.includes(carName)">{{car.name}}: {{car.brand}}</p>
    </li>
  </ul>

</div>
</template>

<script>
export default {
 data() {
   return {
    cars: [
      { name: '소나타', brand: '현대'},
      { name: 'K5', brand: '기아'},
      { name: '티코', brand: '대우'},
      { name: '렉스턴', brand: '쌍용'},
    ],
   
    carName: ''
  }},
  methods: {
    
  }

}
</script>

<style>

</style>