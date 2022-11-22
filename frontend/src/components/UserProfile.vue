<template>
  <div id="Profile">
    <NavigationBar class="nav-top" :logged="logged" :key="logged" :email="email" :token="token" />
        <!-- Card perfil usuario -->
        <div class="card bg-light">
          <div class="card-body">
            <h5 class="card-title"><b>Tu perfil</b></h5>
            <h6 class="card-subtitle">Aquí podrás ver y editar los datos de tu perfil</h6>
            <div class="container-card">
              <b> Imagen de perfil </b>
            </div>
          </div>
        </div>
  </div>
</template>

<script>
import NavigationBar from './NavigationBar.vue'

export default {
  name: 'UserProfile',
  components: {
    NavigationBar
  },
  data () {
    return {
      logged: true,
      token: 'g',
      email: 'e'
    }
  }
}
</script>

<style scoped>

.card-subtitle {
  font-size: medium;
}

.container-card {
  background-color: white;
}
</style>
