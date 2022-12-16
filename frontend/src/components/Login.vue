<template>
  <div id="login">
    <b-alert style="z-index: 999; position:fixed; right:1rem; margin: 10px auto; top: 0"
        :show="dismissCountDown"
        variant="danger"
        @dismissed="dismissCountDown=0"
        @dismiss-count-down="countDownChanged"
        fade
      >
      <p>Correo o contraseña incorrecta</p>
    </b-alert>
    <div class="row d-flex justify-content-center">
      <div class="container">
        <h2 class="text-center">Bienvenido a Wallapopo</h2>
        <h3 class="text-center">Regístrate o inicia sesión</h3>
      </div>
      <div class="card" style="width: 30%">
        <div class="card-body">
          <div class="container">
            <div>
              <b-card-text>
                <div class="form-label-group">
                  <label for="login_input_emailField">Correo</label>
                  <input
                    type="email"
                    id="login_input_emailField"
                    class="form-control"
                    placeholder="Introducir correo"
                    required
                    autofocus
                    v-model="email"
                  />
                </div>
                <div class="form-label-group">
                  <br />
                  <label for="login_input_pwdField">Contraseña</label>
                  <input
                    type="password"
                    id="login_input_pwdField"
                    class="form-control"
                    placeholder="Introducir contraseña"
                    required
                    v-model="password"
                  />
                </div>
              </b-card-text>
              <div class="text-center">
                <a
                  href="#forgotPassword"
                  class="stretched-link"
                  @click="redirectToForgot()"
                  >¿Has olvidado la contraseña?</a
                >
              </div>
              <button
              id="login_button_enter"
                class="btn btn-primary btn-lg my-2"
                @click="checkLogin()"
                style="width: 100%"
              >
                Entrar
              </button>
              <button
                class="btn btn-success btn-lg my-2"
                @click="redirectToRegister()"
                style="width: 100%"
              >
                Registrarme
              </button>
              <button
                class="btn btn-secondary btn-lg my-2"
                @click="redirectToHome()"
                style="width: 100%"
              >
                Volver
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if='logged' id='login_div_loginExitoso'>
      Login Exitoso
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {devWeb, prodWeb} from '../store'
export default {
  data () {
    return {
      email: null,
      password: null,
      logged: false,
      prodPath: prodWeb,
      devPath: devWeb,
      dismissSecs: 2,
      dismissCountDown: 0
    }
  },
  methods: {
    countDownChanged (dismissCountDown) {
      this.dismissCountDown = dismissCountDown
    },
    showAlert () {
      this.dismissCountDown = this.dismissSecs
    },
    redirectToHome () {
      this.$router.push({ path: '/' })
    },
    redirectToRegister () {
      this.$router.push({ path: '/register' })
    },
    redirectToForgot () {
      this.$router.push({ path: '/forgotPassword' })
    },
    checkLogin () {
      const path = this.devPath + '/login'
      const parameters = {
        email: this.email,
        password: this.password
      }

      axios
        .post(path, parameters)
        .then((res) => {
          this.logged = true
          console.log('RESPONSE', res)
          localStorage.setItem('token', res.data.token)
          localStorage.setItem('email', this.email)
          this.$router.push({
            name: 'Main',
            params: {data: res.data, logged: true, email: this.email}
          })
        })
        .catch((error) => {
          console.error(error)
          this.showAlert()
        })
    }
  }
}
</script>
