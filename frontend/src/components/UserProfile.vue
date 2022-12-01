<template>
  <div id="Profile">
    <NavigationBar class="nav-top" :logged="logged" :key="logged" :email="email" :token="token" />
        <!-- Card perfil usuario -->
        <div class="card bg-light">
          <div class="card-body">
            <b-button id="profileButton" class="profileButton">Perfil</b-button>
            <b-button id="reviewsButton" class="reviewsButton">Opiniones</b-button>
            <h5 class="card-title"><b>Tu perfil</b></h5>
            <h6 class="card-subtitle">Aquí podrás ver y editar los datos de tu perfil</h6>
            <br>
            <div id="imProfile" class="container-card">
              <b> Imagen de perfil </b>
              <div class="row">
                <div class="col"> <h6 class="imSubt"> Foto principal </h6> </div>
                <div class="col">
                  <div>
                    <b-img :src="require('../assets/product_placeholder.png')" class="profileImg" v-bind="mainProps" rounded="circle" width="70" height="70" alt="Circle image"></b-img>
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
                >
                <div class="row-name">
                  <label>Nombre</label>
                  <b-form-input
                    type="text"
                    id="input-name"
                    class="form-control"
                    placeholder= "Introduce tu nombre"
                    v-model= this.name
                    maxlength="50"
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
                    placeholder="Introduce un apellido"
                    v-model=this.surname
                    maxlength="50"
                    required
                    autofocus
                    trim
                  />
                </div>
                </b-form-group>
                <div class="row-name">
                  <label>Nombre de usuario</label>
                  <br>
                  <span id='userProfile_span_username'> {{username}} </span>
                </div>
                <div class="row-name">
                  <label>Email</label>
                  <br>
                  <span id='userProfile_span_email'> {{email}} </span>
                </div>
                <div class="row-name">
                  <label>Fecha de cumpleaños</label>
                  <br>
                  <label for="start">Introduce la fecha:</label>
                  <input type="date" id="start" name="birthday-start">
                </div>
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
import {devWeb, prodWeb} from '../store'
import axios from 'axios'

export default {
  name: 'UserProfile',
  components: {
    NavigationBar
  },
  data () {
    return {
      name: '',
      surname: '',
      username: '',
      birthdate: '',
      logged: true,
      token: this.$route.params.token,
      email: this.$route.params.email,
      prodPath: prodWeb,
      devPath: devWeb,
      mainProps: { blank: false, blankColor: '#777', width: 70, height: 70, class: 'profileImg' }
    }
  },

  created () {
    const path = this.devPath + '/account/' + this.email
    console.log(this.token)
    axios.get(path, {
      auth: {username: this.token}
    })
      .then((res) => {
        console.log(res)
        if (res.data.account.name != null) {
          this.name = res.data.account.name
        }
        if (res.data.account.surname != null) {
          this.surname = res.data.account.surname
        }
        if (res.data.account.username != null) {
          this.username = res.data.account.username
        }
        if (res.data.account.birthdate != null) {
          this.birthdate = res.data.account.birthdate
        }
      })
      .catch((error) => {
        console.error(error)
        alert('Error al mostrar info del usuario')
      })
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

.profileButton {
  border-radius: 20px 20px 20px 20px;
  background-color: #bdf5ff;
  animation-delay: 1s;
  margin-bottom: 10px;
  cursor: grab;
  color: #1b1e21;
  border-color: #1b1e21;
}

.reviewsButton {
  border-radius: 20px 20px 20px 20px;
  background-color: #bdf5ff;
  animation-delay: 1s;
  margin-bottom: 10px;
  margin-left: 5px;
  cursor: grab;
  color: #1b1e21;
  border-color: #1b1e21;
}
.saveButton {
  border-radius: 20px 20px 20px 20px;
  background-color: #bdf5ff;
  animation-delay: 1s;
  cursor: grab;
  margin-left: 80px;
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
