<template>
  <main class="hello">
    <NavigationBar class="nav-top" />
    <div class="container">
      <div class="row">
        <div class="col-6 col-lg-3 celda" v-for="product in db">
          <CardProduct
          :title="product.name" :price="product.price" :desc ="product.description" :productState="product.product_status" :date="product.date"
          />
          </div>

      </div>
    </div>
  </main>
</template>

<script>
import NavigationBar from './NavigationBar.vue'
import CardProduct from './CardProduct.vue'
import db from '@/hardDB.js'
console.log('hola')
console.log(db[0])
export default {
  name: 'HelloWorld',
  components: {
    NavigationBar,
    CardProduct
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      db: db
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
