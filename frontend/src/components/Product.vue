<template>
  <div>
    <NavigationBar :logged="logged" :key="logged" :token="token" />
    <div class="container">
      <div class="card">
        <div class="row row-title">
          <div class="col-5 row">
            <a v-on:click="goBack()"><img src="../assets/icons/back.png" style="width: 50px" alt="back" /></a>
            &nbsp;
            <img
              src="../assets/default-profile.jpg"
              class="rounded-circle"
              style="width: 50px"
              alt="Avatar"
            />
          <div class="col-4 buttons">
            <button
              class="product-button"
              v-if="!liked && logged"
              v-on:click="liked = !liked"
              @click="addFav()"
            >
              <img src="../assets/heart.png" alt="" style="width: 20px" />
            </button>
            <button
              class="product-button"
              v-if="liked && logged"
              v-on:click="liked = !liked"
              @click="addFav()"
            >
              <img src="../assets/heart2.png" alt="" style="width: 20px" />
            </button>
            <button v-if="logged" class="product-button">Chat</button>
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
            <button v-if="logged" class="product-button product-comprar">
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
              <font-awesome-icon
                class="miIcon"
                icon="fa-truck-fast"
                style="font-size: 28px"
              />
              <span>&nbsp;&nbsp;Hago envíos</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <Footer/>
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
      token: localStorage.getItem('token'),
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
    },
    goBack () {
      console.log('hi')
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
  align-items: center;
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

.product-button {
  border-radius: 20px;
  border: 1px solid rgb(184, 184, 184);
  background-color: rgb(207, 197, 197);
  color: white;
  width: 80px;
  padding: 0 15px;
  align-items: center;
  transition: 0.5s;
  margin-left: 5px;
  height: 40px;
  cursor: pointer;
}

.product-button:hover {
  background-color: darkgray;
}

.product-button {
  border-radius: 20px;
  border: 1px solid rgb(184, 184, 184);
  background-color: rgb(207, 197, 197);
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
.product-button:hover {
  background-color: red;
}

.buttons {
  display: flex;
  justify-content: flex-end;
}
.product-comprar {
  width: 100px;
}
</style>
