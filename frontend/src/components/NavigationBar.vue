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
import axios from 'axios'

export default {
  name: 'NavigationBar',
  props: {
    logged: Boolean,
    email: String,
    token: String
  },
  data () {
    return {

    }
  },
  methods: {
    logout () {
      const path = 'https://lavida-wallapopo.herokuapp.com/logout/' + this.email
      axios.post(path, {}, {
        auth: {username: this.token}
      })
        .then(() => {
          console.log('logged out')
          this.logged = false
          this.token = 'g'
          this.email = 'e'
        })
        .catch((error) => {
          console.error(error)
        })
      this.$router.push({ path: '/' })
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
