<template>
  <div id="login">
    <div v-if="creatingAccount" class="col d-flex justify-content-center">
      <div class="card" style="width: 30%;">
        <div class="card-body">
          <h5 class="card-title" align="center">Crear Cuenta</h5>
          <div class="container">
            <b-card-text>
              <div class="form-label-group">
                <label for="inputEmail">Correo</label>
                <input type="email" id="inputEmail" class="form-control"
                placeholder="Introducir correo" required autofocus v-model="addUserForm.email">
              </div>
              <div class="form-label-group">
                <br>
                <label for="inputPassword">Contraseña</label>
                <input type="password" id="inputPassword" class="form-control"
                placeholder="Introducir contraseña" required v-model="addUserForm.password">
              </div>
            </b-card-text>
            <button class="btn btn-primary btn-lg my-2" @click="createAccount()" style="width: 100%;">Enviar</button>
            <button class="btn btn-secondary btn-lg my-2" @click="creatingAccount= false" style="width: 100%;">Volver</button>
          </div>
        </div>
      </div>
    </div>
    <div v-else-if="forgotPassword" class="col d-flex justify-content-center">
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
              <button class="btn btn-secondary btn-lg my-2" @click="forgotPassword= false" style="width: 100%;">Volver</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="col d-flex justify-content-center">
      <div class="card" style="width: 30%;">
        <div class="card-body">
          <h5 class="card-title" align="center">Iniciar Sesión</h5>
          <div class="container">
            <div>
              <b-card-text>
                <div class="form-label-group">
                  <label for="inputEmail2">Correo</label>
                  <input type="email" id="inputEmail2" class="form-control"
                  placeholder="Introducir correo" required autofocus v-model="email">
                </div>
                <div class="form-label-group">
                  <br>
                  <label for="inputPassword2">Contraseña</label>
                  <input type="password" id="inputPassword2" class="form-control"
                  placeholder="Introducir contraseña" required v-model="password">
                </div>
              </b-card-text>
              <p class="text-center" @click="forgotPassword= true">¿Has olvidado la contraseña?</p>
              <button class="btn btn-primary btn-lg my-2" @click="checkLogin()" style="width: 100%;">Entrar</button>
              <button class="btn btn-success btn-lg my-2" @click="creatingAccount= true" style="width: 100%;">Registrarme</button>
              <button class="btn btn-secondary btn-lg my-2" @click="redirectToHome()" style="width: 100%;">Volver</button>
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
      password: null,
      creatingAccount: false,
      forgotPassword: false,
      actualPath: 'http://localhost:5000/',
      addUserForm: {
        email: null,
        password: null
      }
    }
  },
  methods: {
    redirectToHome () {
      this.$router.push({ path: '/' })
    }
  }
}
</script>
