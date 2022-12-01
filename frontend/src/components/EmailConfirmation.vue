<template>
  <main class="emailConfirmation">
    <div class="container">
      <div class="row justify-content-center">
        <div v-if="error">
          <b-jumbotron class="d-flex justify-content-center" bg-variant="secondary" text-variant="white"
            border-variant="dark">
            <template #header>Oops</template>
            <template #lead>
              {{ message }}
            </template>
            <hr class="my-4">
            <div v-if="code === 409 || code === 500">
              <button class="btn btn-primary btn-lg my-2" @click="redirectToHome()">Volver al inicio</button>
            </div>
          </b-jumbotron>
        </div>
        <div v-if="!error">
          <b-jumbotron class="d-flex justify-content-center" bg-variant="success" text-variant="white"
            border-variant="dark">
            <template #header>Bienvenido a <b>Wallapopo</b></template>
            <template #lead>
              {{ message }}
            </template>
            <hr class="my-4">
            <div v-if="code===200">
              <div>
                <button class="btn btn-primary btn-lg my-2" @click="redirectToLogin()">Inicia sesión</button>
              </div>
            </div>
          </b-jumbotron>
        </div>
      </div>
    </div>
    <Footer />
  </main>
</template>

<script>
import Footer from './Footer.vue'
import axios from 'axios'
import {devWeb, prodWeb} from '../store'

export default {
  name: 'EmailConfirmation',
  components: {
    Footer
  },
  data () {
    return {
      prodPath: prodWeb,
      devPath: devWeb,
      error: false,
      code: 200,
      message: ''
    }
  },
  methods: {
    redirectToHome () {
      this.$router.push({path: '/'})
    },
    redirectToLogin () {
      this.$router.push({path: '/login'})
    }
  },
  created () {
    var str = window.location.href
    var res = str.split('/')
    var last = res[res.length - 1]
    var valToken = last.slice(17)
    console.log(valToken)
    axios.post(this.devPath + '/validation', {
      validation_token: valToken
    }).then((response) => {
      console.log(response)
      this.message = response.data.message
      this.error = false
      this.code = response.status
    }).catch(err => {
      console.log(err)
      this.message = err.response.data.message
      this.error = true
      this.code = err.response.status
      // alert(this.code)
    })
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
