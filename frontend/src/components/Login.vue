<template>
  <div id="login">
    <div class="col d-flex justify-content-center">
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
              <button class="btn btn-success btn-lg my-2" @click="redirectToRegistro()" style="width: 100%;">Create
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
      password: '',
      status_policy: '0',
      check: true,
      actualPath: 'http://localhost:5000/'
    }
  },
  methods: {
    redirectToHome () {
      this.$router.push({ path: '/' })
    },
    redirectToRegistro () {
      this.$router.push({path: '/register'})
    }
  }
}
</script>
