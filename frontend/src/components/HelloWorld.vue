<template>
  <div class="products">
    <NavigationBar
      class="nav-top"
      @searchText="onChangeSearch($event)"
      :logged="logged"
      :key="logged"
      :email="email"
      :token="token"
      :search_text="search_text"
    />
    <NavBarFiltros
      @productsList="onChangeFilters($event)"
      :category2="category"
    />
    <div class="container" style="min-height: 400px">
      <h3 v-if="category">{{ category }}</h3>
      <h3 v-else-if="search_text"> + {{ db.length }} resultados para {{ search_text }}</h3>
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
            :favourite_list="favourite"
            :logged="logged"
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
      category: null,
      search_text: null,
      filters: null,
      favourite: []
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
          this.db = res.data.Products_List
          this.db = this.db.slice()
        })
        .catch((error) => {
          console.error(error)
        })
    },
    getCategory (category) {
      const path = this.prodPath + `/category/${category}`
      axios.get(path)
        .then((res) => {
          console.log(res)
          this.db = res.data.products_list
          this.db = this.db.slice()
        })
        .catch((error) => {
          console.error(error)
        })
    },
    onChangeFilters (param) {
      this.filters = param
      this.applyFilter()
    },
    onChangeSearch (param) {
      this.search_text = param
      this.applyFilter()
    },
    applyFilter () {
      if (this.filters) {
        const path = this.prodPath + `/filter`
        const parameters = (this.search_text === null) ? this.filters : Object.assign(
          {search: this.search_text},
          this.filters
        )
        this.category = parameters.category
        axios.post(path, parameters)
          .then((res) => {
            console.log(res.data)
            this.db = res.data.products_list
            this.db = this.db.slice()
          })
          .catch((error) => {
            console.error(error)
            console.log(parameters)
          })
      } else if (this.search_text) {
        const path = this.prodPath + `/filter/${this.search_text}`
        axios.get(path)
          .then((res) => {
            console.log(res.data)
            this.category = null
            this.db = res.data.products_list
            this.db = this.db.slice()
          })
          .catch((error) => {
            console.error(error)
          })
      } else {
        this.getProducts()
      }
    },
    getFavourites () {
      axios.get(this.devPath + `/favourites/${this.email}`, {auth: {username: this.token}}).then((res) => {
        console.log(res.data)
        this.favourite = []
        for (var i = 0; i < res.data.favourites_list.length; i++) {
          this.favourite.push(res.data.favourites_list[i].product.id)
        }
        console.log(this.favourite)
      }).catch((error) => {
        console.error(error)
      })
    }
  },
  created () {
    this.category = this.$route.params.categoria
    this.search_text = this.$route.params.search_text
    if (this.search_text) {
      this.search_text = this.search_text.trim()
      this.applyFilter()
    } else if (this.category) this.getCategory(this.category)
    else this.getProducts()
    this.email = localStorage.getItem('email')
    this.token = localStorage.getItem('token')
    this.isLogged()
    if (this.logged) {
      this.getFavourites()
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
