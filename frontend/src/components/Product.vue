<template>
  <div>
    <NavigationBar :logged="logged" :key="logged" :token="token" />
    <div class="container">
      <div class="card">
        <div class="row row-title">
          <div class="col-5 row">
            <img
              src="../assets/default-profile.jpg"
              class="rounded-circle"
              style="width: 50px"
              alt="Avatar"
            />
            <p class="user-name col-8">{{ product.username }}</p>
          </div>
          <div class="col-3">
            <!-- valoraciones -->
            <div class="row">
              <img
                  v-for="i in 2"
                :key="i"
                src="../assets/star2.png"
                alt=""
                style="width: 20px"
              />
              <img
                v-for="i in 3"
                :key="i"
                src="../assets/star.png"
                alt=""
                style="width: 20px"
              />
            </div>
          </div>

          <div class="col-4 buttons">
            <button
              class="product-button"
              v-if="liked && logged"
              v-on:click="liked = !liked"
            >
              <img src="../assets/heart.png" alt="" style="width: 20px" />
            </button>
            <button
              class="product-button"
              v-if="!liked && logged"
              v-on:click="liked = !liked"
            >
              <img src="../assets/heart2.png" alt="" style="width: 20px" />
            </button>
            <button v-if="logged" class="product-button">Chat</button>
          </div>
        </div>

        <!-- Carrousel de imagenEs-->
        <div>
          <b-carousel
            id="carousel-1"
            v-model="slide"
            :interval="4000"
            controls

            background="#ababab"
            img-width="1024"
            img-height="480"
            style="text-shadow: 1px 1px 2px #333"
            @sliding-start="onSlideStart"
            @sliding-end="onSlideEnd"
          >
            <b-carousel-slide v-for="i in ['product_placeholder.png', 'Oso.jpeg', 'Parchis.jpeg']" :key=i
              :img-src="require('../assets/' + i)"
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
      token: localStorage.getItem('token'),
      prodPath: prodWeb,
      devPath: devWeb,
      logged: false,
      liked: false,
      product: {},
      slide: 0,
      sliding: null
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
        })
        .catch((error) => {
          console.error(error)
        })
    },
    onSlideStart (slide) {
      this.sliding = true
    },
    onSlideEnd (slide) {
      this.sliding = false
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

.card-img {
  height: 550px;
  object-fit: cover;
}
hr {
  width: 100%;
}

.row-title {
  height: 60px;
  align-items: center;
  margin-left: 0;
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
  background-color: red;
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
