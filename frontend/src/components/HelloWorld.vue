<template>
  <main class="hello">
    <NavigationBar class="nav-top" />
    <div class="container">
      <div class="row">
        <div class="col-6 col-lg-3 celda"><CardProduct /></div>
        <div class="col-6 col-lg-3 celda"><CardProduct /></div>
        <div class="col-6 col-lg-3 celda"><CardProduct /></div>
        <div class="col-6 col-lg-3 celda"><CardProduct /></div>
      </div>
    </div>
  </main>
</template>

<script>
import NavigationBar from './NavigationBar.vue'
import CardProduct from './CardProduct.vue'
export default {
  name: 'HelloWorld',
  components: {
    NavigationBar,
    CardProduct
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
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
