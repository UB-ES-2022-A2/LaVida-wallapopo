<template>
  <div id="login">
    <div v-if="creatingAccount" class="col d-flex justify-content-center">
      <!-- Card registro -->
      <div class="card bg-light" style="width: 30%;">
        <div class="card-body">
          <h5 class="card-title" align="center">Registrate en Wallapopo</h5>
          <div class="container">
            <b-card-text>
              <div class="form-label-group">
                <br>
                <input type="text" id="inputName" class="form-control" placeholder="Nombre y apellidos" required
                  v-model="addUserForm.username">
              </div>
              <div class="form-label-group">
                <br>
                <input type="email" id="inputEmail" class="form-control" placeholder="Dirección de email" required
                  autofocus v-model="addUserForm.email">
              </div>
              <div class="form-label-group">
                <br>
                <input type="password" id="inputPassword" class="form-control" placeholder="Contraseña" required
                  minlength="8" maxlength="20" v-model="addUserForm.password" @change="checkPassword(this)">
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
            <button class="btn btn-primary btn-lg my-2" style="width: 100%;">Crear una
              cuenta</button>
            <button class="btn btn-secondary btn-lg my-2" @click="creatingAccount= false" style="width: 100%;">Cancelar</button>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="col d-flex justify-content-center">
      <div class="card" style="width: 30%;">
        <div class="card-body">
          <h5 class="card-title" align="center">Sign In</h5>
          <div class="container">
            <div>
              <b-card-text>
                <div class="form-label-group">
                  <label for="inputEmail2">Email</label>
                  <input type="email" id="inputEmail2" class="form-control" placeholder="Email" required autofocus
                    v-model="email">
                </div>
                <div class="form-label-group">
                  <br>
                  <label for="inputPassword2">Password</label>
                  <input type="password" id="inputPassword2" class="form-control" placeholder="Password" required
                    v-model="password">
                </div>
              </b-card-text>
              <button class="btn btn-primary btn-lg my-2" @click="checkLogin()" style="width: 100%;">Sign In</button>
              <button class="btn btn-success btn-lg my-2" @click="creatingAccount= true" style="width: 100%;">Create
                Account</button>
              <button class="btn btn-secondary btn-lg my-2" @click="redirectToHome()" style="width: 100%;">Back To
                Main</button>
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
      username: null,
      password: null,
      creatingAccount: false,
      status_policy: '0',
      actualPath: 'http://localhost:5000/',
      addUserForm: {
        username: null,
        email: null,
        password: null,
        password2: null
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
