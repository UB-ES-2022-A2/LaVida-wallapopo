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
                  minlength="8" maxlength="20" v-model="addUserForm.password" @keyup="checkPassword(this)">
                <small v-if="check" id="passwordStatus">Mínimo 8 caracteres, 1 símbolo y 1 número.</small>
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
      check: true,
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
    }
  }
}
</script>
