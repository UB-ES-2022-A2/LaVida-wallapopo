<template>
  <div id="forgotPassword">
    <div class="col d-flex justify-content-center">
      <div class="card" style="width: 30%;">
        <div class="card-body">
          <h5 class="card-title" align="center">Cambiar Contraseña</h5>
          <div class="container">
            <div>
              <b-card-text>
                <div class="form-label-group">
                  <label for="inputEmail3">Correo</label>
                  <input type="email" id="inputEmail3" class="form-control"
                  placeholder="Introducir correo" required autofocus v-model="email">
                </div>
              </b-card-text>
              <button class="btn btn-primary btn-lg my-2" @click="forgotPassword()" style="width: 100%;">Enviar</button>
              <button class="btn btn-secondary btn-lg my-2" @click="redirectToLogin()" style="width: 100%;">Volver</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      email: null,
      password: null
    }
  },
  methods: {
    redirectToLogin () {
      this.$router.push({ path: '/login' })
    }
  }
}
</script>
