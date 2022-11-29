<template>
  <div class="products">
    <NavigationBar class="nav-top" :logged="logged" :key="logged" :email="email" :token="token"/>
    <NavBarFiltros  @productsList="db=$event" :category2="category"/>
    <div class="container" style="min-height: 400px">
      <h3 v-if="category">{{ category }}</h3>
      <h3 v-else>Todos los productos</h3>
      <hr class="solid">
      <div class="row">
        <div
          class="col-6 col-lg-3 celda"
          v-for="product in db"
          :key="product.id"
        >
          <CardProduct
            :title="product.name"
            :img="product.image"
            :price="product.price"
            :desc="product.description"
            :productState="product.condition"
            :date="product.date"
            :link="product.id"
          />
        </div>
      </div>
    </div>
    <Footer/>
  </div>
</template>

<script>
import NavigationBar from './NavigationBar.vue'
import NavBarFiltros from './NavBarFiltros.vue'
import CardProduct from './CardProduct.vue'
import {devWeb, prodWeb} from '../store'
import Footer from './Footer.vue'

import axios from 'axios'
export default {
  name: 'HelloWorld',
  components: {
    NavigationBar,
    NavBarFiltros,
    CardProduct,
    Footer
  },
  data () {
    return {
      db: [],
      prodPath: prodWeb,
      devPath: devWeb,
      logged: false,
      token: localStorage.getItem('token'),
      email: 'e',
      category: null
    }
  },

  methods: {
    isLogged () {
      if (this.token !== null) {
        this.logged = true
      }
    },
    getProducts () {
      const path = this.devPath + '/products'
      axios.get(path)
        .then((res) => {
          console.log(res)
          let db = res.data.Products_List
          for (let index = 0; index < db.length; index++) {
            this.db.push(db[index])
          }
        })
        .catch((error) => {
          console.error(error)
        })
    },
    getCategory (category) {
      const path = this.devPath + `/filter/${category}`
      axios.get(path)
        .then((res) => {
          console.log(res)
          let db = res.data.products_list
          for (let index = 0; index < db.length; index++) {
            this.db.push(db[index])
          }
        })
        .catch((error) => {
          console.error(error)
        })
      const path = this.devPath + '/API/products'
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
    if (Object.keys(this.$route.params).length !== 0) {
      this.token = this.$route.params.token
      this.logged = this.$route.params.logged
      this.email = this.$route.params.email
    }
  },
  mounted () {
    this.category = this.$route.params.categoria
    if (this.category) this.getCategory(this.category)
    else this.getProducts()
    this.email = localStorage.getItem('email')
    this.token = localStorage.getItem('token')
    this.isLogged()
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
