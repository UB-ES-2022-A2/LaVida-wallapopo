<template>
  <main class="hello">
    <NavigationBar class="nav-top" :logged="logged" :key="logged" :email="email" :token="token" />
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
    </div>
    <Footer/>
  </main>
</template>

<script>
import NavigationBar from './NavigationBar.vue'
import CardProduct from './CardProduct.vue'
import Footer from './Footer.vue'

import axios from 'axios'
export default {
  name: 'HelloWorld',
  components: {
    NavigationBar,
    CardProduct,
    Footer
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      db: [],
      logged: false,
      token: 'g',
      email: 'e'
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
    this.getProducts()
  },
  mounted () {
    console.log('ROUTE', this.$route)
    if (Object.keys(this.$route.params).length !== 0) {
      this.token = this.$route.params.data.token
      this.logged = this.$route.params.logged
      this.email = this.$route.params.email
    }
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
