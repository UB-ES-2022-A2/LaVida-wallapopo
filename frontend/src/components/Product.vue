<template>
    <div>
        <NavigationBar/>

<div class="container">
      <div class="card" >
        <div>User naem</div>
    <img
      class="card-img"
      :src="require('../assets/' + getName(product.name) + '.jpeg')"
      alt="Image Product"

    />
    <div class="card-body" >
      <div class="container">
        <div class="">
          <h5 class="row">{{ product.price}}EUR</h5>
        </div>
        <div class="row">
          <p>
            <b>{{ product.name }}</b>

          </p>
        </div>
        <div class="row">
          <p>Estado: {{ product.status }}</p>
        </div>
        <div class="row card-text">
          <p>
            {{ product.description }}
          </p>

        </div>
      </div>
    </div>
  </div>
</div>

    </div>
</template>

<script>
import NavigationBar from './NavigationBar.vue'
import axios from 'axios'

export default {
  name: 'HelloWorld',
  components: {
    NavigationBar
  },
  data () {
    return {
      msg: this.$route.params.id,
      product: {
        id: 1,
        name: 'Oso de peluche',
        price: 23,
        status: 'nuevo',
        description: 'lallal'
      },
      db: []

    }
  },
  methods: {
    getName (nameProduct) {
      return nameProduct.split(' ')[0]
    },
    filterProduct (id, products) {
      let ids = id
      let filteredArray = products.filter(function (itm) {
        console.log('itm', itm.id)
        return parseInt(itm.id) === parseInt(ids)
      })
      console.log('Function filter', filteredArray)
      return filteredArray[0]
    },

    getProducts () {
      const path = 'http://127.0.0.1:5000/products'
      axios.get(path).then((res) => {
        console.log('PRODUCTS request', res)
        let db = res.data.Products_List
        this.product = this.filterProduct(this.$route.params.id, db)
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
    console.log('DB', this.db)

    this.msg = this.$route.params.id
    console.log('Product Data afeter mount', this.product)
  }
}
</script>
<style scoped>
.card {
  width: auto;
  border-radius: 10px;
width: 80%;
  margin-bottom: 10px;
  margin-bottom: 20px;
  border: 1px solid black;
box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
}

.card-img {
  height: 600px;
  object-fit: cover;
}
.card-text {
  height: 100px;
  color: rgb(134, 134, 139);
  display: block;
  display: -webkit-box;
  -webkit-line-clamp: 5; /* max line number */
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}
.row {
  height: 25px;
}
</style>
