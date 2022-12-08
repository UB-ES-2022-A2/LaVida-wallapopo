<template>
  <div id="Profile">
    <NavigationBar class="nav-top" :logged="logged" :key="logged" :email="email" :token="token" />
    <!-- Perfil Usuari -->
    <div class="card bg-light" v-if="type==='profile'">
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
    <!--HISTORIAL DE COMPRES-->
    <div v-else-if="type==='bought'" id="bought-div">
      <div class="card bg-light" id="big-card" style="width: 40rem;">
        <h5 class="card-title"><b>Historial de compras</b></h5>
        <h6 class="card-subtitle">Productos comprados desde la creación de la cuenta:</h6>
        <br>
        <div v-if="(purchases.length === 0)">
          <a>No se han comprado productos hasta la fecha</a>
        </div>
        <div class="card" id="bought-card" v-else v-for="purchase in purchases" :key="purchase.id" style="width: 39rem;">
          <div class="row no-gutters" v-on:click="goToProduct(purchase.product.id)">
            <div class="col-auto">
              <b-img :src="require('../assets/product_placeholder.png')" class="productImg" width="100" height="100" alt="Circle image"></b-img>
            </div>
            <div class="col-5">
              <div class="card-block px-2">
                <h4 class="card-title">{{purchase.product.name}}</h4>
                <p class="card-text">{{purchase.product.category}}</p>
              </div>
            </div>
            <div class="col-3">
              <a style="font-size:14px; margin-left:40px;">{{purchase.date}}</a>
            </div>
            <div class="col">
              <h5 class="card-text" id="bought-price">{{purchase.product.price}}€</h5>
              <a href="#" class="btn btn-primary">Puntuar</a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--HISTORIAL DE VENDES-->
    <div v-else-if="type==='sold'" id="sold-div">
      <div class="card bg-light" id="big-card" style="width: 40rem;">
        <h5 class="card-title"><b>Historial de ventas</b></h5>
        <h6 class="card-subtitle">Productos vendidos desde la creación de la cuenta:</h6>
        <br>
        <div v-if="(sales.length === 0)">
          <a>No se han vendido productos hasta la fecha</a>
        </div>
        <div class="card" id="bought-card" v-else v-for="sale in sales" :key="sale.id" style="width: 39rem;">
          <div class="row no-gutters" v-on:click="goToProduct(purchase.product.id)">
            <div class="col-auto">
              <b-img :src="require('../assets/product_placeholder.png')" class="productImg" width="100" height="100" alt="Circle image"></b-img>
            </div>
            <div class="col-5">
              <div class="card-block px-2">
                <h4 class="card-title">{{sale.product.name}}</h4>
                <p class="card-text">{{sale.product.category}}</p>
              </div>
            </div>
            <div class="col-3">
              <a style="font-size:14px; margin-left:40px;">{{sale.date}}</a>
            </div>
            <div class="col">
              <h5 class="card-text" id="bought-price">{{sale.product.price}}€</h5>
              <a href="#" class="btn btn-primary">Puntuar</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavigationBar from './NavigationBar.vue'
import { devWeb, prodWeb } from '../store'
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
      birthday: '',
      logged: true,
      token: this.$route.params.token,
      email: this.$route.params.email,
      type: this.$route.params.type,
      prodPath: prodWeb,
      devPath: devWeb,
      changeImgBoolean: false,
      isSelecting: false,
      selectedFile: null,
      purchases: [],
      sales: [],
      mainProps: { blank: false, blankColor: '#777', width: 70, height: 70, class: 'profileImg' }
    }
  },
  methods: {
    goToProduct (id) {
      this.$router.push({
        path: '/product/' + id
      })
    },
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
      const path = this.devPath + '/profile/' + this.email
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
    },
    getUserInfo () {
      const path = this.devPath + '/account/' + this.email
      axios.get(path, {
        auth: { username: this.token }
      })
        .then((res) => {
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
    },
    getPurchases () {
      const path = this.devPath + '/order/purchases/' + this.email
      axios.get(path, {
        auth: { username: this.token }
      })
        .then((res) => {
          console.log('purchases')
          console.log(res.data.orders_list)
          if (res.data.orders_list != null) {
            this.purchases = res.data.orders_list
          }
        })
        .catch((error) => {
          console.error(error)
          alert('Error al mostrar purchases')
        })
    },
    getSales () {
      const path = this.devPath + '/order/sales/' + this.email
      axios.get(path, {
        auth: { username: this.token }
      })
        .then((res) => {
          console.log('sales')
          console.log(res.data.orders_list)
          if (res.data.orders_list != null) {
            this.sales = res.data.orders_list
          }
        })
        .catch((error) => {
          console.error(error)
          alert('Error al mostrar sales')
        })
    }
  },

  created () {
    this.getUserInfo()
    this.getPurchases()
    this.getSales()
  }
}
</script>

<style scoped>

.card.bg-light {
  margin: auto;
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
