<template>
  <div id="menu_lateral">
    <nav class="navbar navbar-light border d-flex align-items-stretch pr-0 pl-0"
         style="width: 30vh; top:-10px; background-color: #f8f9fa; position:fixed"
    >
      <ul class="navbar-nav" style="height:95vh; margin-top:15vh">
        <li class="nav-item mb-4 my-3 pl-2">
          <a style="color: #000000" class="nav-link h6" v-on:click="goToUserProfile('profile')"><img :src="require('@/assets/icons/user.png')" alt="User icon" style="width: 40px"/> Tu Perfil  </a>
        </li>
        <li class="nav-item mb-4  pl-2">
          <a style="color: #000000" class="nav-link h6" v-on:click="goToUserProfile('reviews')"><img :src="require('@/assets/icons/review.png')" alt="User icon" style="width: 30px"/> Reseñas </a>
        </li>
        <li class="nav-item mb-4  pl-2">
          <a style="color: #000000" class="nav-link h6" v-on:click="goToUserProfile('bought')"><img :src="require('@/assets/icons/buy.png')" alt="User icon" style="width: 30px"/> Compras </a>
        </li>
        <li class="nav-item mb-4  pl-2">
          <a style="color: #000000" class="nav-link h6" v-on:click="goToUserProfile('sold')"><img :src="require('@/assets/icons/sell.png')" alt="User icon" style="width: 30px"/> Ventas </a>
        </li>
        <li class="nav-item mb-4  pl-2">
          <a style="color: #000000" class="nav-link h6" v-on:click="goToUserProfile('favourites')"><img :src="require('@/assets/heart.png')" alt="User icon" style="width: 30px"/> Favoritos </a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  data () {
    return {
      name: 'menu'
    }
  },
  methods: {
    goToUserProfile (type2) {
      this.$emit('type', type2)
    }
  }
}
</script>

<style scoped>

.nav-item{
  cursor: pointer;
  transition: 0.5s;
}

.nav-item.mb-4:hover {
  background-color: #e6e8eb;
}

.nav-item.mb-5:hover {
  background-color: #e6e8eb;
}

</style>
