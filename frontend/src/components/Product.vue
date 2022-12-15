<template>
  <div>
    <NavigationBar :logged="logged" :key="logged" :token="token" />
    <b-breadcrumb style="background-color: white; margin-left: 1rem">
      <b-breadcrumb-item @click="goHome">
        <b-icon icon="house-fill" scale="1.25" shift-v="1.25" aria-hidden="true"></b-icon>
        Inicio
      </b-breadcrumb-item>
      <b-breadcrumb-item @click="goBack">{{ product.category }}</b-breadcrumb-item>
      <b-breadcrumb-item active>{{ product.name }}</b-breadcrumb-item>
    </b-breadcrumb>
    <div class="container">
      <div class="card" style="padding-top:10px">
        <div class="row row-title">
          <div class="col-5 row">
            <div class="align-items-center">
              <b-avatar size="3rem" variant="info" :src=product.user_image class="mr-3"></b-avatar>
              <span class="mr-auto user-name">{{ product.username }}</span>
            </div>
          </div>
        </div>
        <!-- Carrousel de imagenes-->
        <div>
          <b-carousel
            id="carousel-1"
            v-model="slide"
            :interval="4000"
            controls
            indicators
            background="#ababab"
            img-width="1024"
            img-height="480"
            @sliding-start="onSlideStart"
            @sliding-end="onSlideEnd"
          >
            <b-carousel-slide v-for="image in product.image" :key=image
              :img-src="image"
              style="height:480px"
            ></b-carousel-slide>
          </b-carousel>
        </div>

        <div class="card-body">
          <div class="price-product row">
            <h5 class="col product-price">{{ product.price }} EUR</h5>
                        <button
              class="btn btn-light btn-large"
              v-if="liked && logged"
              v-on:click="liked = !liked"
              @click="addFav()"
            >
              <img src="../assets/heart2.png" alt="" style="width: 30px" />
            </button>
            <button
              class="btn btn-light btn-large"
              v-if="!liked && logged"
              v-on:click="liked = !liked"
              @click="addFav()"
            >
              <img src="../assets/heart.png" alt="" style="width: 30px" />
            </button>
            <button
              v-if="logged && product.status ==='Vendido' " class="btn btn-secondary btn-lg disabled ml-2">
              Vendido
            </button>
            <button v-show="buyButtonVisibility" id="product-button-buy"
              v-if="logged && product.status !=='Vendido' " class="product-button product-comprar" v-on:click="goToBuy">
              Comprar
            </button>
          </div>
          <hr class="solid" />
          <div class="row col">
            <p class="product-name">
              {{ product.name }}
            </p>
          </div>
          <hr class="solid" />
          <div class="row col">
            <p>Estado: {{ product.condition }}</p>
          </div>
          <div class="row col">
            <p>
              {{ product.description }}
            </p>
          </div>
          <hr class="solid" />
          <div class="row col">
            <p style="color: gray">
              {{ product.date }}
            </p>
            <div v-show="product.shipment" class="ml-auto">
              <b-icon icon="truck" aria-hidden="true"></b-icon>
              <span>&nbsp;&nbsp;Hago envíos</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import NavigationBar from './NavigationBar.vue'
import Footer from './Footer'
import axios from 'axios'
import { devWeb, prodWeb } from '../store'

export default {
  name: 'HelloWorld',
  components: {
    Footer,
    NavigationBar
  },
  data () {
    return {
      id: this.$route.params.id,
      token: null,
      email: null,
      prodPath: prodWeb,
      devPath: devWeb,
      logged: false,
      liked: false,
      product: {},
      slide: 0,
      sliding: null,
      buyButtonVisibility: true
    }
  },
  methods: {
    isLogged () {
      if (this.token !== null) {
        this.logged = true
      }
    },
    getProduct () {
      const path = this.devPath + `/product/${this.id}`
      axios
        .get(path)
        .then((res) => {
          console.log('PRODUCTS request', res)
          this.product = res.data.product
          this.buyButtonVisibility = this.product.user !== this.email
        })
        .catch((error) => {
          console.error(error)
        })
      if (this.logged) {
        axios.get(this.devPath + `/favourites/${this.email}`, {auth: {username: this.token}}).then((res) => {
          console.log(res.data)
          console.log(this.liked)
          for (var i = 0; i < res.data.favourites_list.length; i++) {
            if (parseInt(this.id) === res.data.favourites_list[i].product.id) {
              this.liked = true
            }
          }
          console.log(this.liked)
        }).catch((error) => {
          console.error(error)
        })
      }
    },
    goHome () {
      this.$router.push({name: 'Main'})
    },
    goBack () {
      event.preventDefault()
      window.history.back()
    },
    goToBuy () {
      this.$router.push({
        path: '/buy/' + this.product.id
      })
    },
    onSlideStart (slide) {
      this.sliding = true
    },
    onSlideEnd (slide) {
      this.sliding = false
    },
    addFav () {
      let favParams = {
        email: this.email,
        product_id: this.id
      }
      if (this.liked) {
        axios.post(this.devPath + '/favourites', favParams, {auth: {username: this.token}}).then((response) => {
          console.log(response)
          alert('Producto añadido a favoritos correctamente')
        }).catch((error) => {
          console.error(error)
        })
      } else {
        axios.delete(this.devPath + '/favourites', {auth: {username: this.token},
          data: {email: this.email, product_id: this.id}}).then((response) => {
          console.log(response)
          alert('Producto eliminado de favoritos correctamente')
        }).catch((error) => {
          console.error(error)
        })
      }
    }
  },
  mounted () {
    this.token = localStorage.getItem('token')
    this.email = localStorage.getItem('email')
    this.isLogged()
    console.log('Token', this.token)
    this.id = this.$route.params.id
    this.getProduct()
  }
}
</script>
<style scoped>
.container {
  width: 55%;
}
.card {
  border-radius: 10px;
  display: block;
  margin-bottom: 20px;
  box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
  padding: 25px;
}

hr {
  width: 100%;
}

.row-title {
  height: 60px;
  margin-left: 0;
}
.product-price {
  margin: 0;
  font-size: 25px;
  font-weight: 700;
}
.product-name {
  margin: auto 0;
  font-size: 25px;
  font-weight: 550;
}
.product-button:hover {
  background-color: #13c0ab;
}

.product-button {
  border-radius: 20px;
  border: 1px solid rgb(23, 161, 183);
  background-color: rgb(40, 166, 69);
  color: white;
  width: 80px;
  padding: 0 15px;
  align-items: center;
  transition: 0.5s;
  margin-left: 5px;
  height: 40px;
  cursor: pointer;
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
  text-decoration: none;
  display: inline-flex;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.product-button:active:after {
  padding: 0;
  margin: 0;
  opacity: 1;
  transition: 0s;
  font-size: 25px;
  font-weight: 700;
}

.user-name {
  margin: 0;
  font-size: 20px;
  font-weight: 600;
  letter-spacing: 1px;
}
.buttons {
  display: flex;
  justify-content: flex-end;
}
.product-comprar {
  width: 100px;
}
</style>
