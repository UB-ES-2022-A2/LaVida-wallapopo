<template>
  <b-modal id="modal-1" title="Aviso" header-text-variant="light" header-bg-variant="danger">
    <p class="my-4"><b>¿Estás seguro de que quieres cerrar la sesión actual?</b></p>
    <template #modal-footer="{ logout, cancel }">
      <b-button size="sm" variant="outline-danger" @click="confirmLogout(); changeLogged()">
        Cerrar sesión
      </b-button>
      <b-button size="sm" variant="outline-secondary" @click="cancel()">
        Cancelar
      </b-button>
    </template>
  </b-modal>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LogoutModal',
  props: {
    logged: Boolean,
    email: String,
    token: String,
    modalActive: Boolean
  },
  methods: {
    confirmLogout () {
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
    },
    changeLogged () {
      this.$emit('loggedStatus', false)
    }
  }
}
</script>

<style scoped>
p {
  font-size: 18px;
  margin: 20px 0;
}

button {
  width: 150px;
  height: 40px;
  font-size: 14px;
  border-radius: 16px;
  margin-top: 50px;
}
</style>
