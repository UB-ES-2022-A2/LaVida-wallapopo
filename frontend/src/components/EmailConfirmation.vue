<template>
  <main class="hello">
    <div class="container">
      <div class="row">
        <div>
          <b-jumbotron class="d-flex justify-content-center" bg-variant="success" text-variant="white" border-variant="dark" >
            <template #header>Bienvenido a <b>Wallapopo</b></template>
            <template #lead>
              Tu plataforma de elección para compra y venta de articulos de
              segunda mano.
            </template>
            <hr class="my-4">
            <p>
              Puedes cerrar esta pagina e iniciar sesión.
            </p>
          </b-jumbotron>
        </div>
      </div>
    </div>
    <Footer/>
  </main>
</template>

<script>
import Footer from './Footer.vue'
import axios from 'axios'

export default {
  name: 'EmailConfirmation',
  components: {
    Footer
  },
  data () {
    return {
      prodPath: 'https://firm-affinity-366616.ew.r.appspot.com',
      devPath: 'http://localhost:5000'
    }
  },

  methods: {
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
      alert('Verificación correcta')
    }).catch(err => {
      console.log(err)
      var error = err.response.data.message
      alert(error)
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
