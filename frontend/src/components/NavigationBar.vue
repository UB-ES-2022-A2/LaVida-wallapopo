<template>
  <nav class="navbar navbar-expand-md style-navbar" id="navbar-identifier">
    <a class="navbar-brand h1" @click="goToHome()">Wallapopo</a>
    <div class="container-fluid">
      <font-awesome-icon class="nav-icon" icon="fa-magnifying-glass" @click="onEnter"/>
      <b-form-input
        type="search"
        placeholder="Buscar"
        aria-label="Buscar"
        v-model="text"
        @keydown.enter.native="onEnter"
      />
    </div>
    <div v-if="!logged" class="container buttons-session">
      <div v-on:click="goToLogin" class="btn btn-primary">
        Login
      </div>
      <div v-if="!logged" v-on:click="goToRegister"  class="btn btn-secondary ">
        Register
      </div>
    </div>
    <div v-else class="container">
      <div class="btn">
        <img src="@/assets/heart.png" alt="User icon" style="width: 20px" />
        </div>
      <div class="btn"><font-awesome-icon class="nav-icon" icon="fa-envelope" /></div>

      <div class="dropdown-dark my-3 text-right">
        <b-dropdown id="dropdown-1" :src="require('@/assets/user.png')" alt="User icon" text="Usuario" class="m-md-2" variant="dark">
          <b-dropdown-item v-b-modal.modal-1 v-on:click="goToUserProfile('profile')">Ver Perfil</b-dropdown-item>
          <b-dropdown-item v-b-modal.modal-1 v-on:click="goToUserProfile('bought')">Ver historial de compras</b-dropdown-item>
          <b-dropdown-item v-b-modal.modal-1 v-on:click="goToUserProfile('sold')">Ver historial de ventas</b-dropdown-item>
          <b-dropdown-item v-b-modal.modal-1 v-on:click="loggedOut()">Cerrar Sesión</b-dropdown-item>
        </b-dropdown>
        <LogoutModal @loggedStatus="logged=$event" class="modal" :logged="logged" :key="logged" :email="email" :token="token"/>
      </div>

      <div class="btn btn-product" @click="goToAddProduct()" id='navigationBar_div_addProduct'>
        <img src="@/assets/add.png" alt="User icon" style="width: 20px" />
        Agregar producto
      </div>
    </div>
  </nav>
</template>

<script>

import LogoutModal from './LogoutModal'

export default {
  name: 'NavigationBar',
  components: { LogoutModal },
  props: {
    logged: Boolean,
    search_text: String
  },
  data () {
    return {
      text: this.search_text,
      token: localStorage.getItem('token'),
      email: localStorage.getItem('email')
    }
  },
  methods: {
    onEnter () {
      if (this.$route.name === 'Main') {
        this.$router.push({
          name: 'HelloWorld',
          params: {search_text: this.text}}
        )
      } else {
        this.$emit('searchText', this.text)
      }
    },
    isLogged () {
      if (this.token !== null) {
        this.logged = true
      } else {
        this.logged = false
      }
    },
    loggedOut () {
      localStorage.removeItem('token')
      localStorage.removeItem('email')
    },
    goToLogin () {
      this.$router.push({name: 'Login'})
    },
    goToRegister () {
      this.$router.push({name: 'Registro'})
    },
    goToProducts () {
      this.$router.push({name: 'HelloWorld'})
    },
    goToAddProduct () {
      this.$router.push({
        name: 'AddProduct',
        params: {logged: this.logged, email: this.email, token: this.token}
      })
    },
    goToHome () {
      this.$router.push({
        name: 'Main',
        params: {logged: this.logged, email: this.email, token: this.token}
      })
    },
    goToUserProfile (type2) {
      this.$router.push({
        name: 'UserProfile',
        params: {logged: this.logged, email: this.email, token: this.token, type: type2}
      })
    }
  },
  computed () {
    this.token = localStorage.getItem('token')
    this.email = localStorage.getItem('email')
    this.isLogged()
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
  margin-bottom:10px;
}
.container{
  justify-content: end;
}
.buttons-session div {
  margin-left: 3px;
}

.nav-icon{
  font-size: 33px;
  margin-right: 3px;
  transition: 0.3s;}
.btn{
  margin-left: 2px;

}
.nav-icon:hover{
  font-size: 35px;
  color: rgb(59, 187, 170);
}
.btn-product{
  display: contents;
  justify-content: center;
}

</style>
