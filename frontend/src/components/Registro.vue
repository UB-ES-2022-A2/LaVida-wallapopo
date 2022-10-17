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
                  v-model="addUserForm.username">
              </div>
              <div class="form-label-group">
                <br>
                <input type="text" id="inputSurname" class="form-control" placeholder="Apellidos" required
                  v-model="addUserForm.usersurname">
              </div>
              <div class="form-label-group">
                <br>
                <input type="email" id="inputEmail" class="form-control" placeholder="Dirección de email" required
                  autofocus v-model="addUserForm.email">
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
                <input type="password" id="inputPassword2" class="form-control" placeholder="Verificar contraseña"
                  required minlength="8" maxlength="20" v-model="addUserForm.password2">
              </div>
              <div>
                <br>
                <b-form-checkbox id="checkbox-1" v-model="status_policy" name="checkbox-1" value="1"
                  unchecked-value="0">
                  He leído y acepto las Condiciones de uso y la Política de privacidad de Wallapopo.
                </b-form-checkbox>
              </div>
            </b-card-text>
            <button class="btn btn-primary btn-lg my-2" :disabled="status_policy !== '1'" @click="checkPasswordMatch()"
              style="width: 100%;">Crear una
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
      status_policy: '0',
      fullCheck: false,
      checkLength: false,
      checkSymbol: false,
      checkNumber: false,
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
      const validSpecialChars = /[!&_\-?]/
      return validSpecialChars.test(str)
    },
    checkPasswordMatch () {
      var p1 = this.addUserForm.password
      var p2 = this.addUserForm.password2

      if (p1 === '') {
        alert('Introduce una contraseña')
      } else if (p2 === '') {
        alert('Confirma la contraseña')
      } else if (p1 !== p2) {
        alert('Las contraseñas no coinciden')
      } else {
        alert('Bienvenido')
      }
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
    }
  }
}
</script>
