<template>
  <div class="card" v-on:click="goToProduct()">
    <img
      class="card-img"
      :src="require('../assets/' + getName(title) + '.jpeg')"
      alt="Image Product"

    />
    <div class="card-body" >
      <div class="container">
        <div class="">
          <h5 class="row">{{ price }}$</h5>
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
    link: Number
  },
  data () {
    return {

    }
  },
  methods: {
    getName (nameProduct) {
      return nameProduct.split(' ')[0]
    },
    goToProduct () {
      this.$router.push({
        path: '/product/' + this.$props.link
      })
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
}
</style>
