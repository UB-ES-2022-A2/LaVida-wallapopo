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
            <!--button id="swapHeart" class="btn btn-default swap">
                <span class="glyphicon glyphicon-heart-empty"></span>
            </-button-->
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
  transition: fill 150ms linear;
  transition-property: fill;
  transition-duration: 150ms;
  transition-timing-function: linear;
  transition-delay: 0s;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  position: relative;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}
</style>
