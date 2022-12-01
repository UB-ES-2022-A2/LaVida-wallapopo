<template>
  <div id="login">
    <div class="col d-flex justify-content-center">
      <div class="card" style="width: 30%">
        <div class="card-body">
          <h5 class="card-title" align="center">Iniciar Sesión</h5>
          <div class="container">
            <div>
              <b-card-text>
                <div class="form-label-group">
                  <label for="inputEmail2">Correo</label>
                  <input
                    type="email"
                    id="inputEmail2"
                    class="form-control"
                    placeholder="Introducir correo"
                    required
                    autofocus
                    v-model="email"
                  />
                </div>
                <div class="form-label-group">
                  <br />
                  <label for="inputPassword2">Contraseña</label>
                  <input
                    type="password"
                    id="inputPassword2"
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
      devPath: devWeb
    }
  },
  methods: {
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
      const path = this.prodPath + '/login'
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
          alert('Username or Password incorrect')
        })
    }
  }
}
</script>
