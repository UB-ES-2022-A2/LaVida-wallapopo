<template>
  <div class="card">
    <div class="card-body">
      <img
        class="card-img-top"
        src="@/assets/descarga.png"
        alt="Image Product"
      />
      <h5 class="card-title">{{ title }}</h5>
      <div class="container">
        <div class="row">
          <div class="col-sm">
            {{ price }}
          </div>
          <div class="col-sm">
            {{ productState }}
          </div>
          <div class="col-sm">
            {{ date }}
          </div>
        </div>
      </div>
      <p class="card-text">
        {{ desc }}
      </p>
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
    productState: String
  }
}
</script>

<style scoped>
.card {
  background-color: rgb(51, 189, 159);
  width: auto;
  border-radius: 10px;
  padding: 10px;
  width: 210px;
  height: 500px;
}
</style>
