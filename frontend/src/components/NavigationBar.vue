<template>
  <nav class="navbar navbar-expand-md style-navbar" id="navbar-identifier">
    <div class="container-fluid col-9">
      <img class="img-logo" src="../assets/logo1.png" alt="" @click="goToHome()" />
        <b-form-input
          type="search"
          placeholder="Buscar en todas las categorías"
          aria-label="Buscar"
          v-model="text"
          @keydown.enter.native="onEnter"
          style="border-radius: 30px"
        >
        </b-form-input>
    </div>
    <div v-if="!logged" class="container buttons-session col-2">
      <b-button id="login-button" variant="outline-success" v-on:click="goToLogin" style="border-radius: 30px">
        Iniciar sesión
      </b-button>
      <b-button id="register-button" variant="outline-success" v-on:click="goToRegister" style="border-radius: 30px">
        Registrarse
      </b-button>
    </div>
    <div v-else class="container col-3">
      <div class="dropdown-dark my-3 text-right" id="navbar-button-profile">
        <b-dropdown toggle-class="rounded-circle px-2" variant="outline-info" id="dropdown-1" no-caret>
          <template #button-content>
            <b-icon icon="person-fill" aria-hidden="true"></b-icon>
          </template>
          <b-dropdown-item id="perfil" v-on:click="goToUserProfile('profile')">Perfil</b-dropdown-item>
          <b-dropdown-item id="compras" v-on:click="goToUserProfile('bought')">Compras</b-dropdown-item>
          <b-dropdown-item id="ventas" v-on:click="goToUserProfile('sold')">Ventas</b-dropdown-item>
          <b-dropdown-item id="reviews" v-on:click="goToUserProfile('reviews')">Reseñas recibidas</b-dropdown-item>
          <b-dropdown-item id="reviews" v-on:click="goToUserProfile('favourites')">Favoritos</b-dropdown-item>
          <b-dropdown-divider></b-dropdown-divider>
          <b-dropdown-item variant="danger" id="cerrar_sesion" v-b-modal.modal-1>
            <b-icon icon="power" aria-hidden="true"></b-icon>
            Cerrar Sesión
          </b-dropdown-item>
        </b-dropdown>
        <LogoutModal @loggedStatus="loggedOut($event)" class="modal" :logged="logged" :key="logged" :email="email" :token="token"/>
      </div>

      <b-button class="round-btn" variant="info" @click="goToAddProduct()" id='navigationBar_div_addProduct'>
        <b-icon icon="plus-circle" aria-hidden="true"></b-icon> Agregar producto
      </b-button>
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
    loggedOut (logged) {
      localStorage.removeItem('token')
      localStorage.removeItem('email')
      this.logged = logged
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
      if (this.$route.name !== 'AddProduct') {
        this.$router.push({
          name: 'AddProduct',
          params: {logged: this.logged, email: this.email, token: this.token}
        })
      }
    },
    goToHome () {
      if (this.$route.name !== 'Main') {
        this.$router.push({
          name: 'Main',
          params: {logged: this.logged, email: this.email, token: this.token}
        })
      }
    },
    goToUserProfile (type2) {
      if (this.$route.name !== 'UserProfile') {
        localStorage.setItem('type', type2)
        this.$router.push({
          name: 'UserProfile',
          params: {logged: this.logged, email: this.email, token: this.token, type: type2}
        })
      } else {
        this.$emit('type', type2)
      }
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
  cursor: pointer;
  transition: 0.5s;

}

.navbar-brand:hover{
  background-color: rgba(0, 0, 0, 0.103);
}

a {
  text-decoration: inherit;
  color: white;
}
.navbar{
  border-bottom: 1px solid rgb(221, 221, 221);
  margin-bottom: 10px;
  background-color: white;
}
.container {
  justify-content: end;
  margin-right:0px;
}
.buttons-session div {
  margin-left: 3px;
}

.btn{
  margin-left: 2px;

}
.round-btn {
  border-radius:30px;
  margin-left:5px;
}

.container-fluid {
  margin-left:0px;
}

.img-logo {
  user-drag: none;
  -webkit-user-drag: none;
  cursor:pointer;
  margin-right:4rem;
  height:4rem;
}

#login-button{
  color: rgb(137, 189, 158);
  font-weight: 400;
  background-color: rgb(255, 255, 255);
  border: solid 2px rgb(137, 189, 158);
  border-radius: 20px;
}

#register-button{
  color: rgb(137, 189, 158);
  font-weight: 400;
  background-color: rgb(255, 255, 255);
  border: solid 2px rgb(137, 189, 158);
  border-radius: 20px;
}

</style>
