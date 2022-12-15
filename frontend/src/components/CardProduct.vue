<template>
  <div class="card">
    <img
      class="card-img"
      :src=img
      v-on:click="goToProduct()"
      alt="Image Product"
    />
    <div class="card-body">
      <div class="container">
        <div class="">
          <h5 class="row">
            {{ price }} $
            <div class="col-2 buttons">
              <img
                class="clickable"
                v-if="!liked && logged"
                v-on:click="liked = !liked"
                @click="addFav()"
                src="../assets/heart.png" alt="" style="width: 20px"
              />
              <img
                class="clickable"
                v-if="liked && logged"
                v-on:click="liked = !liked"
                @click="addFav()"
                src="../assets/heart2.png" alt="" style="width: 20px"
              />
          </div>
          </h5>
        </div>
        <div class="row" v-on:click="goToProduct()">
          <p>
            <b class="clickable">{{ title }} </b>
          </p>
        </div>
        <div class="row">
          <p>Categoria: {{ category }}</p>
        </div>
        <div class="row">
          <p>Estado: {{ productState }}</p>
        </div>
        <div class="row card-text">
          {{ desc }}
        </div>
      </div>
    </div>
  </div>
</template>
<script>

import axios from 'axios'
import {devWeb, prodWeb} from '../store'

export default {
  props: {
    title: String,
    price: Number,
    desc: String,
    date: String,
    category: String,
    productState: String,
    img: String,
    link: Number,
    favourite_list: null,
    logged: Boolean
  },
  data () {
    return {
      email: null,
      token: null,
      liked: false,
      prodPath: prodWeb,
      devPath: devWeb
    }
  },
  methods: {
    isLogged () {
      if (this.token !== null) {
        this.logged = true
      }
    },
    goToProduct () {
      this.$router.push({
        path: '/product/' + this.$props.link
      })
    },
    addFav () {
      let favParams = {
        email: this.email,
        product_id: this.link
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
          data: favParams}).then((response) => {
          console.log(response)
          alert('Producto eliminado de favoritos correctamente ')
        }).catch((error) => {
          console.error(error)
        })
      }
    },
    updateFavList () {
      axios.get(this.devPath + `/favourites/${this.email}`, {auth: {username: this.token}}).then((res) => {
        console.log(res.data)
        for (var i = 0; i < res.data.favourites_list.length; i++) {
          if (this.link === res.data.favourites_list[i].product.id) {
            this.liked = true
          }
        }
      }).catch((error) => {
        console.error(error)
      })
    }
  },
  mounted () {
    this.token = localStorage.getItem('token')
    this.email = localStorage.getItem('email')
    this.isLogged()
    if (this.logged === true) {
      this.updateFavList()
    }
  }
}
</script>

<style scoped>
.card {
  border-radius: 10px;
  width: 250px;
  height: 380px;
  margin-bottom: 20px;
  box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
  transition: 0.5s;
}

.card-img {
  height: 200px;
  cursor: pointer;
}
.card-text {
  height: 100px;
  color: rgb(134, 134, 139);
  display: block;
  overflow: hidden;
}
.row {
  height: 25px;
  display: flex;
  justify-content: space-between;
}

.clickable {
  cursor: pointer;
}

.col-2 buttons {
  cursor: pointer;
}

</style>
