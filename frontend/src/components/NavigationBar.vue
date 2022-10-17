<template>
  <nav class="navbar navbar-expand-md style-navbar">
    <a class="navbar-brand h1" href="/#/">Wallapopo</a>
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
    <div class="container ">
    <p v-if="!logged"  class="btn btn-primary">
      <a href="/#/login">Login</a>
    </p>
    <p v-if="!logged"  class="btn btn-secondary ">
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
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavigationBar',
  data () {
    return {
      logged: false
    }
  }
}
</script>

<style scoped>
a {
  color: inherit;
  text-decoration: inherit;
  color: aquamarine;
}
.navbar{
  border-bottom: 1px solid rgb(120, 120, 120);
  margin-bottom:10px ;
}
.container{
  justify-content: end;
}
.btn{
  margin-left: 2px;
}
</style>
