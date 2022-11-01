<template>
  <main class="hello">
    <NavigationBar class="nav-top" :logged="logged" :key="logged" :email="email" :token="token" />
    <div class="container">
      <div class="row">
        <p>CONFIRMED</p>
      </div>
    </div>
    <Footer />
  </main>
</template>

<script>
import NavigationBar from './NavigationBar.vue'
import Footer from './Footer.vue'

export default {
  name: 'EmailConfirmation',
  components: {
    NavigationBar,
    Footer
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      db: [],
      prodPath: 'https://firm-affinity-366616.ew.r.appspot.com',
      devPath: 'http://localhost:5000/emailConfirmation',
      logged: false,
      token: 'g',
      email: 'e'
    }
  },

  methods: {
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
