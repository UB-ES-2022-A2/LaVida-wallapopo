<template>
  <div>
    <NavigationBar  :logged="logged" :key="logged" :email="email"/>
    <div class="container">
      <div class="card">
        <div class="row row-title">
          <div class="col-4 row">
            <img
              src="../assets/default-profile.jpg"
              class="rounded-circle"
              style="width: 50px"
              alt="Avatar"
            />
            <p class="user-name col-8">{{ user }}</p>
          </div>
          <div class="col-4">
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
          :src="require('../assets/' + getName(product.name) + '.jpeg')"
          alt="Image Product"
        />
        <div class="card-body">
          <div class="container">
            <div class="price-product row">
              <h5 class="col  product-price">{{ product.price }} EUR</h5>
              <button v-if="logged" class="product-button product-comprar">Comprar</button>
            </div>
            <hr class="solid">
            <div class="row">
              <p class="product-name">
                {{ product.name }}
              </p>
            </div>
            <hr class="solid">
            <div class="row">
              <p>Estado: {{ product.status }}</p>
            </div>
            <div class="row card-text">
              <p>
                {{ product.description }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavigationBar from './NavigationBar.vue'
import axios from 'axios'
import { devWeb, prodWeb } from '../store'

export default {
  name: 'HelloWorld',
  components: {
    NavigationBar
  },
  data () {
    return {
      msg: this.$route.params.id,
      user: 'User Name',
      token: localStorage.getItem('token'),
      prodPath: prodWeb,
      devPath: devWeb,
      logged: false,
      product: {
        id: 1,
        name: 'Oso de peluche',
        price: 23,
        status: 'nuevo',
        description: 'lallal'
      },
      db: []
    }
  },
  methods: {
    isLogged () {
      if (this.token.length > 0) {
        this.logged = true
      }
    },
    getName (nameProduct) {
      if (nameProduct !== undefined) {
        return nameProduct.split(' ')[0]
      }
    },

    getProducts () {
      const path = this.devPath + '/API/product/' + this.$route.params.id
      axios.get(path).then((res) => {
        console.log('PRODUCTS request', res)
        this.product = res
      })
    }
  },

  created () {
    this.getProducts()
  },

  mounted () {
    this.token = localStorage.getItem('token')
    this.isLogged()
    console.log('Token', this.token)

    this.msg = this.$route.params.id
    console.log('Product Data afeter mount', this.product)
  }
}
</script>
<style scoped>
.card {
  width: auto;
  border-radius: 10px;
  width: 75%;
  margin-bottom: 10px;
  margin-bottom: 20px;
  box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
  padding: 25px;
}

.card-img {
  height: 600px;
  object-fit: cover;
}
hr{
  width:100%;
}
.card-text {
  height: 100px;

  display: block;
  display: -webkit-box;
  -webkit-line-clamp: 5; /* max line number */
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
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
