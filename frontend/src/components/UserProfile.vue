<template>
  <div id="Profile">
    <NavigationBar class="nav-top" :logged="logged" :key="logged" :email="email" :token="token" />
    <div class="row">
      <div class="col-2">
        <Menu />
      </div>
      <div class="col">
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
                <div class="col">
                  <h6 class="imSubt"> Foto principal </h6>
                </div>
                <div class="col">
                  <div>
                  <!-- 1. Create the button that will be clicked to select a file -->
                    <b-img v-if="(changeImgBoolean===true)" :src="require('../assets/product_placeholder.png')" class="profileImg" v-bind="mainProps"
                      rounded="circle" width="70" height="70" alt="Circle image"></b-img>
                    <b-img v-else :src="require('../assets/Oso.jpeg')" class="profileImg" v-bind="mainProps"
                      rounded="circle" width="70" height="70" alt="Circle image"></b-img>
                    <b-btn
                      id="changeImgButton"
                      rounded
                      dark
                      :loading="isSelecting"
                      @click="handleFileImport"
                    >
                      Change Profile Image
                    </b-btn>
                    <!-- Create a File Input that will be hidden but triggered with JavaScript -->
                    <input
                      ref="uploader"
                      class="d-none"
                      type="file"
                      @change="onFileChanged"
                    >
                  </div>
                </div>
              </div>
            </div>
            <br>
            <div id="publicInfo" class="container-card">
              <b> Información pública </b>
              <div>
                <b-form-group invalid-feedback="Nombre no puede estar vacío">
                  <div class="row-name">
                    <label><b>Nombre</b></label>
                    <b-form-input type="text" id="input-name" class="form-control" placeholder="Introduce tu nombre"
                      v-model="name" maxlength="50" autofocus trim v-on:keydown="isLetter($event)" v-on:focusout="removeExtraSpaces($event)"/>
                  </div>
                  <div class="row-name">
                    <label><b>Apellidos</b></label>
                    <b-form-input type="text" id="input-surname" class="form-control" placeholder="Introduce un apellido"
                      v-model="surname" maxlength="50" required autofocus trim v-on:keydown="isLetter($event)" v-on:focusout="removeExtraSpaces($event)"/>
                  </div>
                </b-form-group>
                <div class="row-name" id="profile-div-username">
                  <label><b>Nombre de usuario</b></label>
                  <br>
                  <span> {{ username }} </span>
                </div>
                <div class="row-name" id="profile-div-email">
                  <label><b>Email</b></label>
                  <br>
                  <span> {{ email }} </span>
                </div>
                <div class="row-name">
                  <label><b>Fecha de cumpleaños:</b></label>
                  <br>
                  <input :max="new Date().toISOString().split('T')[0]" type="date" id="start" name="birthday-start" v-model="birthday">
                </div>
              </div>
              <div class="row align-items-end">
                <div class="col"></div>
                <div class="col"></div>
                <div class="col"><b-button id="saveBUtton" class="saveButton" @click="updateProfile()">Guardar</b-button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavigationBar from './NavigationBar.vue'
import Menu from './MenuLateral.vue'
import { devWeb, prodWeb } from '../store'
import axios from 'axios'

export default {
  name: 'UserProfile',
  components: {
    NavigationBar,
    Menu
  },
  data () {
    return {
      name: '',
      surname: '',
      username: '',
      birthday: '',
      logged: true,
      token: this.$route.params.token,
      email: this.$route.params.email,
      prodPath: prodWeb,
      devPath: devWeb,
      changeImgBoolean: false,
      isSelecting: false,
      selectedFile: null,
      mainProps: { blank: false, blankColor: '#777', width: 70, height: 70, class: 'profileImg' }
    }
  },
  methods: {
    handleFileImport () {
      this.isSelecting = true
      // After obtaining the focus when closing the FilePicker, return the button state to normal
      window.addEventListener('focus', () => {
        this.isSelecting = false
        this.changeImgBoolean = !this.changeImgBoolean
      }, { once: true })
      // Trigger click on the FileInput
      this.$refs.uploader.click()
    },
    onFileChanged (e) {
      this.selectedFile = e.target.files[0]
      // TODO: Do whatever you need with the file, liek reading it with FileReader
    },
    isLetter (e) {
      // Get the character
      let char = String.fromCharCode(e.keyCode)
      // Key codes for Backspace, Space, Ctrl, Shift and Arrows
      const allowedKeys = [8, 32, 16, 17, 37, 38, 39, 40]

      if (/^[A-Za-z]+$/.test(char) || allowedKeys.includes(e.keyCode)) {
        return true
      } else e.preventDefault() // If not match, don't add to input text
    },
    removeExtraSpaces (e) {
      e.target.value.replace(/(^\s*)|(\s*$)/gi, '') // Remove spaces at the beginning and end of input text
    },
    updateProfile () {
      const path = this.prodPath + '/profile/' + this.email
      const parameters = {
        email: this.email,
        name: this.name,
        surname: this.surname,
        birthday: this.birthday
      }
      axios.put(path, parameters, {
        auth: { username: this.token }
      })
        .then((res) => {
          console.log(res)
          alert('Datos actualizados correctamente!')
        })
        .catch((error) => {
          alert('Ha ocurrido un error al actualizar los datos, vuelve a intentarlo más tarde')
          console.error(error)
        })
    }
  },
  created () {
    const path = this.devPath + '/account/' + this.email
    console.log(this.token)
    axios.get(path, {
      auth: { username: this.token }
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
        if (res.data.account.birthday != null) {
          this.birthday = res.data.account.birthday
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

.card.bg-light {
  width: 50%;
  padding: 10px;
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
</style>
