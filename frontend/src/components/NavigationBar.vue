<template>
  <nav class="navbar navbar-expand-md bg-light">
    <a class="navbar-brand h1" href="/#">Wallapopo</a>
    <form class="container-fluid" role="search">
      <span>
        <img :src="require('@/assets/icons/search.svg')" alt="search_icon"
      /></span>
      <input
        class="form-control"
        type="search"
        placeholder="Search"
        aria-label="Search"
      />
    </form>
    <p v-if="!logged"  class="btn btn-primary">
      <a href="/#/login">Login</a>
    </p>
    <p v-if="!logged"  class="btn btn-secondary">
      <a href="/#/login">Register</a>
    </p>
    <p class="btn" v-if="logged"><img src="@/assets/icons/favorite_fill.svg" alt="Favorites" /></p>
    <p class="btn" v-if="logged"><img src="@/assets/icons/mail.svg" alt="Mail" /></p>
    <p class="btn" v-if="logged">
      <img src="@/assets/icons/account_circle.svg" alt="User icon" />
      User
    </p>
    <p class="btn" v-if="logged">
      <img src="@/assets/icons/add_circle.svg" alt="User icon" /> Agregar producto
    </p>
  </nav>
</template>

<script>
export default {
  name: 'NavigationBar',
  data () {
    return {
      logged: true
    }
  }
}
</script>

<style scoped>
a {
  color: inherit;
  text-decoration: inherit;
}
</style>
