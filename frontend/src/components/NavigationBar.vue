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
    <div v-if="!logged" class="container">
      <p class="btn btn-primary">
        <a href="/#/login">Login</a>
      </p>
      <p v-if="!logged"  class="btn btn-secondary ">
        <a href="/#/register">Register</a>
      </p>
    </div>
    <div v-else class="container">
      <div class="btn"><img src="@/assets/icons/favorite_fill.svg" alt="Favorites"/></div>
      <div class="btn"><img src="@/assets/icons/mail.svg" alt="Mail"/></div>

      <div class="dropdown-dark my-3 text-right">
        <img src="@/assets/icons/account_circle.svg" alt="User icon" />
        <b-dropdown id="dropdown-1" text="Usuario" class="m-md-2" variant="dark">
          <b-dropdown-item @click="logout()">Cerrar Sesión</b-dropdown-item>
        </b-dropdown>
      </div>

      <div class="btn">
        <img src="@/assets/icons/add_circle.svg" alt="User icon" /> Agregar producto
      </div>
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
  },
  methods: {
    logout () {
      this.logged = false
      this.$router.push({ path: '/' })
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
