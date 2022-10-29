<template>
  <div class="card">
    <img
      class="card-img"
      :src="require('../assets/' + getName(title) + '.jpeg')"
      alt="Image Product"
    />
    <div class="card-body">
      <div class="container">
        <div class="">
          <h5 class="row">{{ price }} $
            <button type="button" class="fav-button" @click="toggle_fav">
              <img class="fav-img" src="../assets/logo_favorito.png" width="24px" height="24px" alt="don't load">
            </button>
          </h5>
        </div>
        <div class="row">
          <p>
            <b>{{ title }}</b>
          </p>
        </div>
        <div class="row">
          <p>Estado: {{ productState }}</p>
        </div>
        <div class="row card-text">
          <p>
            {{ desc }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

export default {
  props: {
    title: String,
    price: Number,
    desc: String,
    date: String,
    productState: String,
    img: String,
    is_fav: Boolean(false)
  },
  data () {
    return {}
  },
  methods: {
    getName (nameProduct) {
      return nameProduct.split(' ')[0]
    },
    toggle_fav () {
      this.is_fav = !this.is_fav
      console.log('Boton cambiado a true', this.is_fav)
    }
  }
}
</script>

<style scoped>
.card {
  width: auto;
  border-radius: 10px;
  width: 250px;
  height: 380px;
  margin-bottom: 10px;
  margin-bottom: 20px;
box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
}

.card-img {
  height: 200px;
}
.card-text {
  height: 100px;
  color: rgb(134, 134, 139);
  display: block;
  display: -webkit-box;
  -webkit-line-clamp: 5; /* max line number */
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}
.row {
  height: 25px;
  display: flex;
  justify-content: space-between;
}

.fav-img {
  background: white;
  border: none;
  border-radius: 8px;
}

.fav-button {
  height: 25px;
  width: 25px;
  background: white;
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  position: relative;
  border: none;
  overflow: hidden;
  border-radius: 8px;
  cursor: pointer;
}

.fav-button:after {
  content: "";
  background: #ff6857;
  display: block;
  position: absolute;
  padding-top: 300%;
  padding-left: 300%;
  margin-left: -30px!important;
  margin-top: -120%;
  opacity: 0;
  transition: all 0.8s
}

.fav-button:active:after {
  padding: 0;
  margin: 0;
  opacity: 1;
  transition: 0s
}
</style>
