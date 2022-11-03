<template>
  <div>
    <NavigationBar :logged="logged" :key="logged" :token="token" />
    <div class="container">
      <div class="card">
        <div class="row row-title">
          <div class="col-6 row">
            <img
              src="../assets/default-profile.jpg"
              class="rounded-circle"
              style="width: 50px"
              alt="Avatar"
            />
            <p class="user-name col-8">{{ username }}</p>
          </div>
          <div class="col-2">
            <!-- valoraciones -->
          </div>

          <div class="col-4 buttons">
            <button v-if="logged" class="product-button">
              <font-awesome-icon class="miIcon" icon="fa-heart" />
            </button>
            <button v-if="logged" class="product-button">Chat</button>
          </div>
        </div>
        <img
          class="card-img"
          :src="require(`../assets/${image}`)"
          alt="Image Product"
        />
        <div class="card-body">
          <div class="price-product row">
            <h5 class="col  product-price">{{ price }} EUR</h5>
            <button v-if="logged" class="product-button product-comprar">Comprar</button>
          </div>
          <hr class="solid">
          <div class="row col">
            <p class="product-name">
              {{ name }}
            </p>
          </div>
          <hr class="solid">
          <div class="row col">
            <p>Estado: {{ condition }}</p>
          </div>
          <div class="row col">
            <p>
              {{ description }}
            </p>
          </div>
          <hr class="solid">
          <div class="row col">
            <p style="color:gray">
              {{ date }}
            </p>
            <div v-show="shipment" class="ml-auto">
              <font-awesome-icon class="miIcon" icon="fa-truck-fast" style="font-size: 28px" />
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
import { pathWeb } from '../store'

export default {
  name: 'HelloWorld',
  components: {
    Footer,
    NavigationBar
  },
  data () {
    return {
      id: '',
      name: '',
      price: '',
      condition: '',
      description: '',
      status: '',
      date: '',
      image: '',
      username: '',
      shipment: false,
      token: null,
      logged: false
    }
  },
  methods: {
    isLogged () {
      if (this.token != null) {
        this.logged = true
      }
    },
    getProduct () {
      const path = pathWeb + `API/product/${this.id}`
      axios.get(path).then((res) => {
        let db = res.data.product
        this.name = db.name
        this.price = db.price
        this.condition = db.condition
        this.description = db.description
        this.date = db.date
        this.status = db.status
        this.username = db.username
        this.image = db.image
        this.shipment = db.shipment
      })
        .catch((error) => {
          console.error(error)
        })
    }
  },
  created () {
    this.token = localStorage.getItem('token')
    this.isLogged()
    console.log('Token', this.token)
    this.id = this.$route.params.id
    this.getProduct()
  },
  mounted () {
    this.token = localStorage.getItem('token')
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
  width:100%;
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
.product-price{
  margin: 0;
  font-size: 25px;
  font-weight: 700;
}
.product-name{
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
.product-comprar{
  width: 100px;
}
</style>
