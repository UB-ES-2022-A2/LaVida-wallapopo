<template>
  <main class="hello">
    <NavigationBar />
  </main>
</template>

<script>
import NavigationBar from './NavigationBar.vue'
export default {
  name: 'HelloWorld',
  components: {
    NavigationBar
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
h1, h2 {
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
</style>
