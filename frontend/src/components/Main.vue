<template>
  <main class="main">
    <NavigationBar class="nav-top" :logged="logged" :key="logged" :email="email" :token="token"/>
    <div class="div-2 my-5 container">
      <div class="pt-3 row text-center">
        <div
          class="col-6 col-lg-3 celda top-buffer"
          v-for="(categoria, index) in categorias"
          :key="categoria.name"
        >
          <div class="div-1" @click="goToProducts(categoria.name)">
            <img id="icon" class="pt-2" :src="require('../assets/icons/categories/'+index+'.png')" alt='Category Image' style="width: 50px"/>
            <p id="category-name">{{categoria.name}}</p>
          </div>
        </div>
      </div>
    </div>
    <Footer/>
  </main>
</template>

<script>
import NavigationBar from './NavigationBar.vue'
import {prodWeb, devWeb} from '../store'
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
      prodPath: prodWeb,
      devPath: devWeb,
      logged: false,
      token: 'g',
      email: 'e',
      categoria: null,
      categories_list: [
        'Todas las categorias',
        'Coches',
        'Motos',
        'Motor y Accesorios',
        'Moda y Accesorios',
        'TV, Audio y Foto',
        'Móviles y Telefonía',
        'Informática y Electrónica',
        'Deporte y Ocio', 'Bicicletas',
        'Consolas y Videojuegos',
        'Hogar y Jardín',
        'Electrodomésticos',
        'Cine',
        'Libros y Música',
        'Niños y Bebés',
        'Coleccionismo',
        'Construcción y Reformas',
        'Industria y Agricultura',
        'Otros'
      ],
      categorias: []
    }
  },
  methods: {
    isLogged () {
      if (this.token !== null) {
        this.logged = true
      }
    },
    getCategorias () {
      for (let i = 0; i < this.categories_list.length; i++) {
        this.categorias.push({
          name: this.categories_list[i]
        })
      }
    },
    goToProducts (categoria) {
      if (categoria === 'Todas las categorias') {
        this.$router.push({
          path: '/products'
        })
      } else {
        this.$router.push({
          path: '/categoria/' + categoria
        })
      }
    }
  },
  mounted () {
    this.token = localStorage.getItem('token')
    this.email = localStorage.getItem('email')
    this.isLogged()
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
.div-1 {
  background-color: white;
  cursor: pointer;
  transition: 0.6s;
  border-radius: 20px;
  padding: 10px;
  transition: transform .2s; /* Animation */
}
.div-1:hover{
  background-color: rgb(224, 224, 224);
  transform: scale(1.1);
}
.div-2 {
  background-color: white;
}
.top-buffer { margin-top:20px; }
</style>
