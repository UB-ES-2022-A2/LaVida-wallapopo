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
      <a href="/#/register">Register</a>
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
  props: {
    logged: Boolean
  },
  data () {
    return {

    }
  }
}
</script>

<style scoped>
.navbar-brand{
  text-align: center;
  font-family: 'Trebuchet MS', sans-serif;
  margin: 0px auto;
  color: rgb(45, 177, 144);
  font-size: 40px;
  letter-spacing: 5px;

}
a {
  color: inherit;
  text-decoration: inherit;
  color: white;
}
.navbar{
  border-bottom: 1px solid rgb(134, 134, 139);
  margin-bottom:10px ;
}
.container{
  justify-content: end;
}
.btn{
  margin-left: 2px;
}
</style>
