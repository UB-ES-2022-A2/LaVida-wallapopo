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
                <input type="text" id="inputName" class="form-control" placeholder="Nombre" required
                  v-model="addUserForm.username" @keyup="checkName()">
                <small v-if="validName" id="nameStatus">El nombre no puede contener numeros.</small>
              </div>
              <div class="form-label-group">
                <br>
                <input type="text" id="inputSurname" class="form-control" placeholder="Apellidos" required
                  v-model="addUserForm.usersurname" @keyup="checkSurname()">
                <small v-if="validSurname" id="nameStatus">El apellido no puede contener numeros.</small>
              </div>
              <div class="form-label-group">
                <br>
                <input type="email" id="inputEmail" class="form-control" placeholder="Dirección de email" required
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
                  required minlength="8" maxlength="20" v-model="addUserForm.password2">
                <small v-if="!fullCheck2" id="confirmStatus">Requisitos: </small>
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
            <button class="btn btn-primary btn-lg my-2"
              :disabled="checkPolicy === '0' || fullCheck === false || passwordsMatch === false || validName === true" style="width: 100%;">Crear una
              cuenta</button>
            <button class="btn btn-secondary btn-lg my-2" @click="redirectToLogin()"
              style="width: 100%;">Cancelar</button>
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
      validSurname: false,
      actualPath: 'http://localhost:5000/',
      addUserForm: {
        username: null,
        usersurname: null,
        email: null,
        password: '',
        password2: ''
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
    containsNumbers (str) {
      return /\d/.test(str)
    },
    containsValidSpecialChars (str) {
      // eslint-disable-next-line
      const validSpecialChars = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/
      return validSpecialChars.test(str)
    },
    checkPasswordMatch () {
      var p1 = this.addUserForm.password
      var p2 = this.addUserForm.password2

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
    checkName () {
      var name = this.addUserForm.username
      this.validName = /\d/.test(name)
    },
    checkSurname () {
      var surname = this.addUserForm.usersurname
      this.validSurname = /\d/.test(surname)
    }
  }
}
</script>
