<template>
  <div id="Profile">
    <NavigationBar class="nav-top" @type="onChangeSearch($event)" :logged="logged" :key="logged" :email="email" :token="token" />
    <b-alert style="z-index: 999; position:fixed; right:1rem; margin: 10px auto; top: 0"
        :show="dismissCountDown"
        variant="success"
        @dismissed="dismissCountDown=0"
        @dismiss-count-down="countDownChanged"
        fade
      >
      <p>Datos actualizados correctamente!</p>
    </b-alert>
    <div class="row">
      <div class="col-2">
        <Menu @type="onChangeSearch($event)"/>
      </div>
      <div class="col">
        <!-- Perfil Usuari -->
        <div class="card bg-light" v-if="type==='profile'">
          <div class="card-body">
            <h3 class="card-title text-center"><b>Perfil</b></h3>
            <b-form-rating class="text-center" v-model="avg_stars" variant="warning" size="lg" readonly show-value no-border></b-form-rating>
            <hr/>
            <div id="imProfile" class="container-card">
              <div class="container" style="display: flex; align-items: center; justify-content: center;">
                <!-- 1. Create the button that will be clicked to select a file -->
                <div class="row">
                  <b-avatar
                    size="10rem"
                    :src=profile_img
                    variant="dark"
                    id="changeImgButton"
                    :loading="isSelecting"
                    button @click="handleFileImport"
                  ></b-avatar>
                </div>
                <!-- Create a File Input that will be hidden but triggered with JavaScript -->
                <input
                    ref="uploader"
                    class="d-none"
                    type="file"
                    @change="onFileChanged"
                    accept="image/*"
                  >
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
          <div class="card bg-light" id="big-card1" style="width: 40rem;">
            <h5 class="card-title"><b>Historial de compras</b></h5>
            <h6 class="card-subtitle">Productos comprados desde la creación de la cuenta:</h6>
            <br>
            <div v-if="(purchases.length === 0)">
              <a>No se han comprado productos hasta la fecha</a>
            </div>
            <div class="card" id="bought-card" v-else v-for="purchase in purchases" :key="purchase.id" style="width: 39rem;">
              <div class="row no-gutters"> <!--v-on:click="goToProduct(purchase.product.id)"-->
                <div class="col-auto">
                  <b-img :src="purchase.product.image" class="productImg" width="100" height="100" alt="Circle image"></b-img>
                </div>
                <div class="col-5">
                  <div class="card-block px-2" v-on:click="goToProduct(purchase.product.id)">
                      <h4 class="card-title">{{purchase.product.name}}</h4>
                      <p class="card-text">{{purchase.product.category}}</p>
                  </div>
                    </div>
                    <div class="col-3">
                      <a style="font-size:14px; margin-left:40px;">{{purchase.date}}</a>
                    </div>
                    <div class="col">
                      <h5 class="card-text" id="bought-price1">{{purchase.product.price}}€</h5>
                      <b-button class="mt-3" variant="success" v-on:click="openReviewModal(purchase.product.id)">Puntuar</b-button>
                </div>
              </div>
            </div>
            <!--Modal de pregunta reseña-->
            <b-modal v-model="modalShow" id="askReview" title="Deseas añadir una reseña para el vendedor?" no-stacking hide-footer>
              <b-button class="mt-3" variant="danger" @click="$bvModal.hide('askReview')">No</b-button>
              <b-button class="mt-3" variant="success" v-b-modal.modal-3>Si!</b-button>
            </b-modal>
            <!--Modal de reseña-->
            <b-modal id="modal-3" title="Ayuda al vendedor a mejorar añadiendo una reseña:" hide-footer ref="review-modal">
              <div>
                <b-form-rating v-model="stars" size="lg" show-value no-border></b-form-rating>
                <b-form-textarea id="textarea-auto-height" placeholder="Dile al vendedor lo que te ha gustado... O lo que no!"
                  v-model="reviewMessage" rows="3" max-rows="8">
                </b-form-textarea>
                <b-button class="mt-3" @click="sendReview(); $bvModal.hide('modal-3')">Enviar reseña</b-button>
              </div>
            </b-modal>
          </div>
        </div>
            <!--HISTORIAL DE VENDES-->
        <div v-else-if="type==='sold'" id="sold-div">
          <div class="card bg-light" id="big-card2" style="width: 40rem;">
            <h5 class="card-title"><b>Historial de ventas</b></h5>
            <h6 class="card-subtitle">Productos vendidos desde la creación de la cuenta:</h6>
            <br>
            <div v-if="(sales.length === 0)">
              <a>No se han vendido productos hasta la fecha</a>
            </div>
            <div class="card" id="sold-card" v-else v-for="sale in sales" :key="sale.id" style="width: 39rem;">
              <div class="row no-gutters" v-on:click="goToProduct(sale.product.id)">
                <div class="col-auto">
                  <b-img :src="sale.product.image" class="productImg" width="100" height="100" alt="Circle image"></b-img>
                </div>
                <div class="col-5">
                  <div class="card-block px-2">
                    <h4 class="card-title">{{ sale.product.name }}</h4>
                    <p class="card-text">{{ sale.product.category }}</p>
                  </div>
                </div>
                <div class="col-3">
                  <a style="font-size:14px; margin-left:40px;">{{ sale.date }}</a>
                </div>
                <div class="col">
                  <h5 class="card-text" id="bought-price">{{sale.product.price}}€</h5>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- HISTORIAL REVIEWS -->
        <div v-else-if="type==='reviews'" id="review-div">
          <div class="card bg-light" id="big-card3" style="width: 40rem;">
            <h5 class="card-title"><b>Historial de reviews</b></h5>
            <h6 class="card-subtitle">Reviews recibidas desde la creación de la cuenta:</h6>
            <br>
            <div v-if="(reviews.length === 0)">
              <a>No se han vendido productos hasta la fecha</a>
            </div>
            <div class="card" id="review-card" v-else v-for="review in reviews" :key="review.id" style="width: 39rem;">
              <div class="row" v-on:click="goToProduct(review.product.id)">
                <div class="col-auto">
                  <b-img :src="review.product.image" class="productImg" width="100" height="100" alt="Circle image"></b-img>
                </div>
                <div class="col">
                  <div class="row">
                    <div class="col-8">{{review.reviewer.name}}</div>
                    <div class="col-4">
                      <b-form-rating v-model=review.stars id="estrellas" readonly no-border></b-form-rating>
                    </div>
                  </div>
                  <div class="row-auto">
                    <div class="row-auto" style="text-align: center; font-weight: bold;">{{review.product.name}}</div>
                    <div v-if="review.comment" class="row-auto" style="text-align: center;">{{review.comment}}</div>
                  </div>
                  <div class="row-8" style="text-align: right; margin-right:10px">{{review.date}}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!--HISTORIAL DE FAVS-->
        <div v-else-if="type==='favourites'" id="favourites-div">
          <div class="card bg-light" id="big-card" style="width: 40rem;">
            <h5 class="card-title"><b>Tus productos favoritos</b></h5>
            <h6 class="card-subtitle">Productos añadidos a favoritos</h6>
            <br>
            <div v-if="(favourites.length === 0)">
              <a>No hay actualmente productos en favoritos.</a>
            </div>
            <div class="card" id="favourites-card" v-else v-for="fav in favourites" :key="fav.id" style="width: 39rem;">
              <div class="row no-gutters" v-on:click="goToProduct(fav.product.id)">
                <div class="col-auto">
                  <b-img :src="fav.product.image" class="productImg" width="100" height="100" alt="Circle image"></b-img>
                </div>
                <div class="col-5">
                  <div class="card-block px-2">
                    <h4 class="card-title">{{fav.product.name}}</h4>
                    <p class="card-text">{{fav.product.category}}</p>
                  </div>
                </div>
                <div class="col-3">
                  <a style="font-size:14px; margin-left:40px;">{{fav.date}}</a>
                </div>
                <div class="col">
                  <h5 class="card-text" id="fav-price">{{fav.product.price}}€</h5>
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
      type: this.$route.params.type,
      prodPath: prodWeb,
      devPath: devWeb,
      changeImgBoolean: false,
      isSelecting: false,
      selectedFile: null,
      stars: 1,
      reviewMessage: '',
      product_id: null,
      modalShow: false,
      purchases: [],
      sales: [],
      reviews: [],
      favourites: [],
      profile_img: null,
      avg_stars: null
    }
  },
  methods: {
    countDownChanged (dismissCountDown) {
      this.dismissCountDown = dismissCountDown
    },
    showAlert () {
      this.dismissCountDown = this.dismissSecs
    },
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
      const customHeader = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      var formData = new FormData()
      formData.append('file', e.target.files[0])
      axios.post(this.prodPath + '/upload/profile/' + this.email, formData, customHeader).then((res) => {
        const path = this.prodPath + '/account/' + this.email
        axios.get(path, {
          auth: { username: this.token }
        })
          .then((res) => {
            this.profile_img = res.data.account.profile
            this.showAlert()
          })
          .catch((error) => {
            console.error(error)
          })
        console.log(res)
      })
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
          this.showAlert()
        })
        .catch((error) => {
          alert('Ha ocurrido un error al actualizar los datos, vuelve a intentarlo más tarde')
          console.error(error)
        })
    },
    openReviewModal (id) {
      this.product_id = id
      this.modalShow = !this.modalShow
    },
    sendReview () {
      let reviewed = false
      for (let i = 0; i < this.purchases.length; i++) {
        if (this.purchases[i]['product_id'] === this.product_id) {
          reviewed = this.purchases[i]['reviewed']
        }
      }
      let dataToSend = {
        email: this.email,
        product_id: this.product_id,
        stars: this.stars,
        comment: this.reviewMessage
      }
      console.log(dataToSend)
      if (reviewed) {
        axios.put(this.prodPath + '/reviews/' + this.product_id, dataToSend, {
          auth: {username: this.token}
        }).then((response) => {
          console.log(response)
          alert('Review actualizada correctamente')
        }).catch(err => {
          console.log(err)
        })
      } else {
        axios.post(this.prodPath + '/reviews', dataToSend, {
          auth: {username: this.token}
        }).then((response) => {
          console.log(response)
          alert('Review enviada correctamente')
        }).catch(err => {
          console.log(err)
        })
      }
    },
    getUserInfo () {
      const path = this.prodPath + '/account/' + this.email
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
          this.profile_img = res.data.account.profile
        })
        .catch((error) => {
          console.error(error)
          alert('Error al mostrar info del usuario')
        })
    },
    getPurchases () {
      const path = this.prodPath + '/order/purchases/' + this.email
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
      const path = this.prodPath + '/order/sales/' + this.email
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
    },
    getReviews () {
      const path = this.prodPath + '/reviews/' + this.email
      axios.get(path, {
        auth: { username: this.token }
      })
        .then((res) => {
          console.log('reviews')
          console.log(res.data.reviews_list)
          if (res.data.reviews_list != null) {
            this.reviews = res.data.reviews_list
            let stars = 0
            for (let i = 0; i < this.reviews.length; i++) {
              stars += this.reviews[i].stars
            }
            this.avg_stars = (stars > 0) ? (stars / this.reviews.length) : 0
          }
        })
        .catch((error) => {
          console.error(error)
          alert('Error al mostrar reviews')
        })
    },
    getFavs () {
      const path = this.prodPath + '/favourites/' + this.email
      axios.get(path, {
        auth: { username: this.token }
      })
        .then((res) => {
          console.log('favourites')
          console.log(res.data.favourites_list)
          if (res.data.favourites_list != null) {
            this.favourites = res.data.favourites_list
          }
        })
        .catch((error) => {
          console.error(error)
          alert('Error al mostrar favoritos')
        })
    },
    onChangeSearch (param) {
      this.type = param
      localStorage.setItem('type', this.type)
    }
  },
  created () {
    this.type = localStorage.getItem('type')
    this.token = localStorage.getItem('token')
    this.email = localStorage.getItem('email')
    this.getUserInfo()
    this.getPurchases()
    this.getSales()
    this.getReviews()
    this.getFavs()
  }
}
</script>

<style scoped>

.card.bg-light {
  margin-left: 30vh;
  width: 50%;
  float:none;
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
