<template>
  <main class="hello">
    <NavigationBar class="nav-top" />

    <div class="container">
      <div class="row">
        <div
          class="col-6 col-lg-3 celda"
          v-for="product in db"
          :key="product.id"
        >
          <CardProduct
            :title="product.name"
            :price="product.price"
            :desc="product.description"
            :productState="product.product_status"
            :date="product.date"

          />
        </div>
      </div>
            <div class="row">
        <div
          class="col-6 col-lg-3 celda"
          v-for="product in db.sort((a, b) => 0.5 - Math.random())"
          :key="product.id"
        >
          <CardProduct
            :title="product.name"
            :price="product.price"
            :desc="product.description"
            :productState="product.product_status"
            :date="product.date"

          />
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import NavigationBar from './NavigationBar.vue'
import CardProduct from './CardProduct.vue'

import axios from 'axios'
export default {
  name: 'HelloWorld',
  components: {
    NavigationBar,
    CardProduct
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      db: []
    }
  },

  methods: {
    getProducts () {
      const path = 'http://127.0.0.1:5000/products'
      axios.get(path).then((res) => {
        console.log(res)
        let db = res.data.Products_List
        for (let index = 0; index < db.length; index++) {
          this.db.push(db[index])
        }
      })
    }
  },
  created () {
    console.log('hola')
    this.getProducts()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.celda {
  height: auto;
  align-content: center;
}
</style>
