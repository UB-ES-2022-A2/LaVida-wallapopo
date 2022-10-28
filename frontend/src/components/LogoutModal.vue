<template>
  <b-modal id="modal-1" title="Aviso" header-text-variant="light" header-bg-variant="danger">
    <p class="my-4"><b>¿Estás seguro que quieres cerrar la sesión actual?</b></p>
    <template #modal-footer="{ logout, cancel }">
      <b-button size="sm" variant="outline-danger" @click="confirmLogout()">
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
      const path = 'http://127.0.0.1:5000/logout/' + this.email
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
h6 {
  font-weight: 500;
  font-size: 28px;
  margin: 20px 0;
}

p {
  font-size: 16px;
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
