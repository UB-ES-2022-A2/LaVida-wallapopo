<template>
  <div id="login">
    <div class="col d-flex justify-content-center">
      <!-- Card registro -->
      <div class="card bg-light" style="width: 30%;">
        <div class="card-body">
          <h5 class="card-title" align="center">Regístrate en Wallapopo</h5>
          <div class="container">
            <b-card-text>
              <div class="form-label-group">
                <br>
                <input type="text" id="inputName" class="form-control" placeholder="Nombre de usuario" required
                  v-model="addUserForm.username" @keyup="checkUsername()">
                <small v-if="!validName" id="nameStatus">El nombre debe contener entre 4 y 20 caracteres</small>
              </div>
              <div class="form-label-group">
                <br>
                <input type="email" id="inputEmail" class="form-control" placeholder="Dirección de correo" required
                  autofocus v-model="addUserForm.email" @keyup="checkEmail()">
                <small v-if="!validEmail" id="emailStatus">El email debe ser de un formato valido, p. ej.: 'aaaa@aaaa.com'.</small>
              </div>
              <div class="form-label-group">
                <br>
                <input type="password" id="inputPassword" class="form-control" placeholder="Contraseña" required
                  minlength="8" maxlength="20" v-model="addUserForm.password" @keyup="checkPassword()">
                <small v-if="!fullCheck" id="fullcheckStatus">La contraseña actual no incluye:</small>
                <br v-if="!fullCheck">
                <small v-if="!checkLength" id="lengthStatus">· 8 caracteres mínimo.</small>
                <br v-if="!checkLength">
                <small v-if="!checkSymbol" id="symbolStatus">· 1 símbolo.</small>
                <br v-if="!checkSymbol">
                <small v-if="!checkNumber" id="numberStatus">· 1 número.</small>
              </div>
              <div class="form-label-group">
                <br>
                <input type="password" id="inputPassword2" class="form-control" placeholder="Verificar contraseña" @keyup="checkPasswordMatch()"
                  required minlength="8" maxlength="20" v-model="password2">
                <small v-if="!fullCheck2" id="fullStatus">Requisitos: </small>
                <br v-if="!fullCheck2">
                <small v-if="!confirmPassword" id="confirmStatus">· Confirmar la contraseña.</small>
                <br v-if="!confirmPassword">
                <small v-if="!fullCheck" id="firstPasswordStatus">· Introducir una contraseña valida.</small>
                <br v-if="!fullCheck">
                <small v-if="!passwordsMatch" id="matchStatus">· Las contraseñas deben coincidir.</small>
              </div>
              <div>
                <br>
                <b-form-checkbox id="checkbox-1" v-model="checkPolicy" name="checkbox-1" value="1"
                  unchecked-value="0">
                  He leído y acepto las Condiciones de uso y la Política de privacidad de Wallapopo.
                </b-form-checkbox>
              </div>
            </b-card-text>
            <button class="btn btn-primary btn-lg my-2" @click="registerUser()"
              :disabled="checkPolicy === '0' || fullCheck === false || passwordsMatch === false || validName === false || validEmail == false" style="width: 100%;">Crear una
              cuenta</button>
            <button class="btn btn-secondary btn-lg my-2" @click="redirectToHome()"
              style="width: 100%;">Cancelar</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import db from '@/hardDB.js'
import axios from 'axios'
import { devWeb, prodWeb } from '../store'
export default {
  data () {
    return {
      checkPolicy: '0',
      fullCheck: false,
      fullCheck2: false,
      checkLength: false,
      checkSymbol: false,
      checkNumber: false,
      confirmPassword: false,
      passwordsMatch: false,
      validEmail: false,
      validName: false,
      password2: '',
      prodPath: prodWeb,
      devPath: devWeb,
      error: '',
      addUserForm: {
        username: null,
        email: null,
        password: ''
      }
    }
  },
  methods: {
    redirectToHome () {
      this.$router.push({path: '/'})
    },
    redirectToLogin () {
      this.$router.push({path: '/login'})
    },
    registerUser () {
      axios.post(this.devPath + '/API/account', this.addUserForm).then((response) => {
        console.log(response)
        alert('Usuario registrado correctamente')
        this.redirectToLogin()
      }).catch(err => {
        console.log(err)
        this.error = err.response.data.message
        alert(this.error)
      })
    },
    containsNumbers (str) {
      return /\d/.test(str)
    },
    containsValidSpecialChars (str) {
      // eslint-disable-next-line
      const validSpecialChars = /^(?=.*?[a-zA-Z])(?=.*?[0-9])(?=.*?[ ´`!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/¿?~]).{8,}$/
      return validSpecialChars.test(str)
    },
    checkPasswordMatch () {
      var p1 = this.addUserForm.password
      var p2 = this.password2

      if (p2 !== '') {
        this.confirmPassword = true
      } else {
        this.confirmPassword = false
      }

      if (p1 === p2) {
        this.passwordsMatch = true
      } else {
        this.passwordsMatch = false
      }
      this.fullCheck2 = this.confirmPassword && this.passwordsMatch && this.fullCheck
    },
    checkPassword () {
      var p = this.addUserForm.password
      if (p.length < 8) {
        this.checkLength = false
      } else {
        this.checkLength = true
      }

      if (!this.containsNumbers(p)) {
        this.checkNumber = false
      } else {
        this.checkNumber = true
      }

      if (!this.containsValidSpecialChars(p)) {
        this.checkSymbol = false
      } else {
        this.checkSymbol = true
      }
      this.fullCheck = this.checkLength && this.checkNumber && this.checkSymbol
    },
    // TODO: Check basico, habria que mejorarlo en el backend
    checkEmail () {
      var email = this.addUserForm.email
      var reg = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      this.validEmail = email.match(reg)
    },
    checkUsername () {
      var name = this.addUserForm.username
      this.validName = name.length >= 4 && name.length <= 20
    }
  }
}
</script>
