<template>
  <div id="Profile">
    <NavigationBar class="nav-top" :logged="logged" :key="logged" :email="email" :token="token" />
        <!-- Card perfil usuario -->
        <div class="card bg-light">
          <div class="card-body">
            <h5 class="card-title"><b>Tu perfil</b></h5>
            <h6 class="card-subtitle">Aquí podrás ver y editar los datos de tu perfil</h6>
            <br>
            <div id="imProfile" class="container-card">
              <b> Imagen de perfil </b>
              <div class="row">
                <div class="col"> <h6 class="imSubt"> Foto principal </h6> </div>
                <div class="col">
                  <div>
                    <b-img :src="require('../assets/logo_favorito.png')" class="profileImg" v-bind="mainProps" rounded="circle" width="70" height="70" alt="Circle image"></b-img>
                    <b-button id="changeImgButton" class="changeImgButton">Cambiar foto</b-button>
                  </div>
                  <h6 class="imSubt"> Aceptamos formatos .jpg y mínimo 400 x 400px </h6>
                </div>
              </div>
            </div>
            <br>
            <div id="publicInfo" class="container-card">
              <b> Información pública </b>
              <div>
                <b-form-group
                  invalid-feedback="Nombre no puede estar vacío"
                  :state="nameState"
                >
                <div class="row-name">
                  <label>Nombre</label>
                  <b-form-input
                    type="text"
                    id="input-name"
                    class="form-control"
                    placeholder="anterior nombre"
                    maxlength="50"
                    :state="nameState"
                    autofocus
                    trim
                  />
                </div>
                <div class="row-name">
                  <label>Apellidos</label>
                  <b-form-input
                    type="text"
                    id="input-surname"
                    class="form-control"
                    placeholder="anterior apellido"
                    maxlength="50"
                    :state="nameState"
                    required
                    autofocus
                    trim
                  />
                </div>
                </b-form-group>
              </div>
              <div class="row align-items-end">
                <div class="col"></div>
                <div class="col"></div>
                <div class="col"><b-button id="saveBUtton" class="saveButton">Guardar</b-button></div>
              </div>
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
      email: 'e',
      mainProps: { blank: false, blankColor: '#777', width: 70, height: 70, class: 'profileImg' }
    }
  }
}
</script>

<style scoped>

b {
  padding-left: 10px;
}

.imSubt {
  padding-top: 3px;
  padding-left: 15px;
  font-size: medium;
}

.card-subtitle {
  padding-left: 10px;
  font-size: medium;
}

.container-card {
  background-color: white;
  border-radius: 8px 20px 20px 20px;
}

.card-body {
  padding-left: 100px;
  width: 50%;
}
.row-name {
  padding-left: 30px;
  padding-top: 20px;
  padding-right: 20px;
}

.profileImg {
  margin-left: 10px;
  margin-bottom: 5px;
}

.saveButton {
  border-radius: 20px 20px 20px 20px;
  background-color: #bdf5ff;
  animation-delay: 1s;
  cursor: grab;
  margin-left: 48px;
  margin-bottom: 5px;
  color: #1b1e21;
  border-color: #1b1e21;
}

.changeImgButton {
  border-radius: 20px 20px 20px 20px;
  background-color: #bdf5ff;
  animation-delay: 1s;
  cursor: grab;
  margin-bottom: 5px;
  color: #1b1e21;
  border-color: #1b1e21;
}

</style>
