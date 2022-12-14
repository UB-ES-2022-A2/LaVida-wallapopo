<template>
  <div>
    <NavigationBar :logged="logged" :key="logged" :token="token" />
    <b-container
      class="bv-example-row buyProductCard pb-2 pt-2"
      :style="cssVars"
    >
      <b-row align-h="center">
        <h2>Comprar producto</h2>
      </b-row>
      <!-- Card product-->
      <b-row align-h="center" class="mb-2 ml-0 mt-2 mr-2" style="width: 100%">
        <b-card
          no-body
          class="overflow-hidden p-3"
          style="justify-content: center"
        >
          <b-row no-gutters>
            <b-col md="4">
              <b-card-img
                :src="require('../assets/' + product.image)"
                alt="Image"
                class="rounded-0"
                style="max-width: 15rem"
              ></b-card-img>
            </b-col>
            <b-col md="8">
              <b-card-body :title="product.name">
                <b-card-text> {{ product.price }} euros </b-card-text>
              </b-card-body>
            </b-col>
          </b-row>
        </b-card>
      </b-row>

      <!-- Formulario -->

      <b-form v-if="show" class="ml-0 mr-2">
        <!--Numero de tarjeta de credito-->
        <b-form-group
          id="buyProduct_input_creditCard_group"
          label="Tarjeta de credito"
          label-for="buyProduct_input_creditCard"
          description="We'll never share your credit card  with anyone else."
        >
          <b-form-input
            id="buyProduct_input_creditCard"
            v-model="form.credit_card"
            type="email"
            placeholder="Mete tu tarjeta :D"
            required
          ></b-form-input>
        </b-form-group>
        <!--Propietario de la tarjeta-->
        <b-form-group
          id="buyProduct_input_owner_group"
          label="Propietario de Tarjeta"
          label-for="buyProduct_input_owner"
        >
          <b-form-input
            id="buyProduct_input_owner"
            v-model="form.name"
            placeholder="Nombre Apellidos"
            required
          ></b-form-input>
        </b-form-group>
        <!--CVC and experation date-->
        <b-row cols="2">
          <b-col>
            <b-form-group id="buyProduct_input_cvc_group" label="CVC" label-for="buyProduct_input_cvc">
              <b-form-input
                id="buyProduct_input_cvc"
                v-model="form.cvc"
                placeholder="Ej. 123"
                required
              ></b-form-input>
            </b-form-group>
          </b-col>
          <b-col>
            <b-form-group id="buyProduct_input_expDate_group" label="Date" label-for="buyProduct_input_expDate">
              <b-form-input
                id="buyProduct_input_expDate"
                v-model="form.exp_date"
                placeholder="Ej. MM/YY"
                required
              ></b-form-input>
            </b-form-group>
          </b-col>
        </b-row>
        <b-row align-h="center">
          <b-col><b-button type="reset" variant="danger" @click="onReset">Cancelar</b-button></b-col>
          <b-col><b-button type="submit" variant="success" v-b-modal.modal-2>Comprar</b-button></b-col>
          </b-row>
          <!-- Modal de confirmacion-->
          <b-modal id="modal-2" title="Confirmar pago" hide-footer ref="my-modal">
            <p class="my-4" id='buyProduct_p_textModal'>{{textLabel}} <b>{{product.name}}</b> </p>
            <b-button class="mt-3" variant="danger" @click="hideModal">Cancelar</b-button>
            <b-button class="mt-3" variant="success" @click="confirmPayment" v-b-modal.askReview>Comprar</b-button>
            <b-alert id='buyProduct_alert_buyConfirmation' show variant="warning" class="mt-2">Estado de compra</b-alert>
          </b-modal>

          <!--Modal de pregunta reseña-->
          <b-modal id="askReview" title="Deseas añadir una reseña para el vendedor?" no-stacking hide-footer>
            <b-button class="mt-3" variant="danger" @click="$bvModal.hide('askReview')">No</b-button>
            <b-button class="mt-3" variant="success" v-b-modal.modal-3>Si!</b-button>
          </b-modal>

          <!--Modal de reseña-->
          <b-modal id="modal-3" title="Ayuda al vendedor a mejorar añadiendo una reseña" hide-footer ref="review-modal">
            <div>
              <b-form-rating v-model="stars" size="lg" show-value no-border></b-form-rating>
              <p class="mt-2">Tu valoración: {{ stars }}</p>
              <b-form-textarea
                id="textarea-auto-height"
                placeholder="Dile al vendedor lo que te ha gustado... O lo que no!"
                v-model="reviewMessage"
                rows="3"
                max-rows="8">
              </b-form-textarea>
              <p class="mt-2">Tu mensaje: {{ reviewMessage }}</p>
              <b-button class="mt-3" @click="sendReview">Enviar reseña</b-button>
            </div>
          </b-modal>
          </b-form>

    </b-container>
  </div>
</template>

<script>
import NavigationBar from './NavigationBar.vue'
import { primaryColor, devWeb, prodWeb, secondaryColor } from '../store'
import axios from 'axios'
import JQuery from 'jquery'
/* eslint-disable */
let $ = JQuery
/* eslint-disable */
var bootbox = require('bootbox')

export default {
  name: 'BuyProdcut',
  components: {
    NavigationBar
  },
  data () {
    return {
      id: this.$route.params.id,
      token: localStorage.getItem('token'),
      prodPath: prodWeb,
      devPath: devWeb,
      logged: false,
      stars: 1,
      reviewMessage: '',
      showModal: false,
      form: {
        email: '',
        name: '',
        credit_card: '',
        cvc: '',
        exp_date: ''
      },
      color: {
        primary: primaryColor,
        secondary: secondaryColor
      },
      product: {
        name: 'algo',
        image: 'Oso.jpeg',
        price: ' '
      },
      textLabel: 'Por favor confirma la compra de',
      show: true
    }
  },
  methods: {
    onReset () {
      this.form.email = ''
      this.form.name = ''
      this.form.cvc = ''
      this.form.exp_date = ''
      this.$router.push({
        path: '/product/' + this.id
      })
    },
    isLogged () {
      if (this.token !== null) {
        this.logged = true
      }
    },
    hideModal () {
      this.$refs['my-modal'].hide()
    },
    confirmPayment () {
      let dataToSend = {
        product_id: this.id,
        credit_card: this.form.credit_card,
        cvc: this.form.cvc,
        cc_owner: this.form.name,
        cc_exp_date: this.form.exp_date
      }

      const path = this.devPath + `/order/add/${this.email}`
      console.log(dataToSend)
      axios.post(path, dataToSend, {
        auth: { username: this.token }
      })
        .then((res) => {
          console.log('RESPOND ORDER', res)
          this.textLabel = 'Exito en la compra de'
          document.getElementById('buyProduct_alert_buyConfirmation').textContent = 'Exito'
          setTimeout(() => this.$refs['my-modal'].hide(), 2000)
        }).catch((err) => {
          console.log(err)
          this.textLabel = 'Error en la compra de'
          document.getElementById('buyProduct_alert_buyConfirmation').textContent = 'Error en la compra'
          setTimeout(() => this.$refs['my-modal'].hide(), 2000)
        })
    },
    sendReview() {
      let dataToSend = {
        email: this.email,
        product_id: this.id,
        stars: this.stars,
        comment: this.message
      }
      console.log(dataToSend)
      axios.post(this.devPath + '/reviews', dataToSend, {
        auth: {username: this.token}
      }).then((response) => {
        console.log(response)
        alert('Review enviada correctamente')
      }).catch(err => {
        console.log(err)
      })
    },
    getProduct () {
      const path = this.devPath + `/product/${this.id}`
      axios
        .get(path)
        .then((res) => {
          console.log('PRODUCTS request', res)
          this.product = res.data.product
        })
        .catch((error) => {
          console.error(error)
        })
    }
  },
  computed: {
    cssVars: function () {
      return {
        '--primary': this.color.primary,
        '--secondary': this.color.secondary
      }
    }
  },
  mounted () {
    this.token = localStorage.getItem('token')
    this.email = localStorage.getItem('email')
    console.log('BUYPRPODYUCT', this.token)
    this.isLogged()
    this.id = this.$route.params.id
    this.getProduct()
  }
}
</script>

<style scoped>
.buyProductCard {
  border-radius: 15px;
  box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
}
#buyProduct_alert_buyConfirmation{
  transition: 0.5s;
}
</style>
