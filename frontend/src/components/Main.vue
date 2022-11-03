<template>
  <main class="main">
    <NavigationBar class="nav-top" :logged="logged" :key="logged" :email="email" :token="token" />
    <div class="container">
      <div class="row">
        <div
          class="col-6 col-lg-3 celda"
          v-for="categoria in categories_list"
          :key="categoria.name"
        >
          <font-awesome-icon class="miIcon" icon="fa-heart" />
        </div>
      </div>
    </div>
    <Footer/>
  </main>
</template>

<script>
import NavigationBar from './NavigationBar.vue'
/* import {pathWeb} from '../store' */
import Footer from './Footer.vue'

export default {
  name: 'HelloWorld',
  components: {
    NavigationBar,
    Footer
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      db: [],
      prodPath: 'https://firm-affinity-366616.ew.r.appspot.com',
      devPath: 'http://localhost:5000',
      logged: false,
      token: 'g',
      email: 'e',
      categories_list: [
        'Coches', 'Motos', 'Motor y Accesorios', 'Moda y Accesorios', 'TV, Audio y Foto', 'Móviles y Telefonía', 'Informática y Electrónica', 'Deporte y Ocio', 'Bicicletas', 'Consolas y Videojuegos', 'Hogar y Jardín', 'Electrodomésticos', 'Cine', 'Libros y Música', 'Niños y Bebés', 'Coleccionismo', 'Construcción y Reformas', 'Industria y Agricultura', 'Otros'
      ],
      icons_list: [
        'fa-car', 'fa-motorcycle', 'fa-helmet-safety', 'fa-shirt', 'fa-tv', 'fa-mobile', 'fa-computer', 'fa-volleyball', 'fa-bicycle', 'fa-gamepad', 'fa-house', 'fa-fire-burner', 'fa-film', 'fa-book', 'fa-baby', 'fa-coins', 'fa-trowel-bricks', 'fa-seedling', 'fa-ellipsis'
      ],
      categorias: []
    }
  },
  methods: {
    getCategorias () {
      for (let i = 0; i < this.categories_list.length; i++) {
        this.categorias.push({
          name: this.categories_list[i],
          image: this.icons_list[i]
        })
      }
    }
  },
  mounted () {
    console.log('ROUTE', this.$route)
    if (Object.keys(this.$route.params).length !== 0) {
      this.token = this.$route.params.data.token
      this.logged = this.$route.params.logged
      this.email = this.$route.params.email
    }
  },
  created () {
    this.getCategorias()
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
