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
        <b-form-group
          id="input-group-1"
          label="Tarjeta de credito"
          label-for="input-1"
          description="We'll never share your credit card  with anyone else."
        >
          <b-form-input
            id="input-1"
            v-model="form.credit_card"
            type="email"
            placeholder="Mete tu tarjeta :D"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group
          id="input-group-1"
          label="Propietario de Tarjeta"
          label-for="input-2"
        >
          <b-form-input
            id="input-2"
            v-model="form.name"
            placeholder="Nombre "
            required
          ></b-form-input>
        </b-form-group>
        <b-row cols="2">
          <b-col>
            <b-form-group id="input-group-3" label="CVC" label-for="input-3">
              <b-form-input
                id="input-1"
                v-model="form.cvc"
                type="email"
                placeholder="Mete tu tarjeta :D"
                required
              ></b-form-input>
            </b-form-group>
          </b-col>
          <b-col>
            <b-form-group id="input-group-3" label="Date" label-for="input-3">
              <b-form-input
                id="input-1"
                v-model="form.exp_date"
                type="email"
                placeholder="Mete tu tarjeta :D"
                required
              ></b-form-input>
            </b-form-group>
          </b-col>
        </b-row>
        <b-row align-h="center">
          <b-col><b-button type="reset">Cancelar</b-button></b-col>
          <b-col
            ><b-button type="submit" v-b-modal.modal-2>Comprar</b-button></b-col
          >
        </b-row>
        <!-- Modal de confirmacion-->
        <b-modal id="modal-2" title="Confirmar pago" hide-footer ref="my-modal">
          <p class="my-4">Hello from modal!</p>
          <b-button class="mt-3" variant="danger" block @click="hideModal"
            >Cancelar</b-button
          >
          <b-button class="mt-3" variant="success" block @click="confirmPayment"
            >Comprar</b-button
          >
        </b-modal>
      </b-form>
    </b-container>
  </div>
</template>

<script>
import NavigationBar from './NavigationBar.vue'
import { primaryColor, devWeb, prodWeb, secondaryColor } from '../store'
import axios from 'axios'

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
      form: {
        email: '',
        name: '',
        credit_card: '',
        cvc: '',
        exp_date: '',
        checked: []
      },
      color: {
        primary: primaryColor,
        secondary: secondaryColor
      },
      product: {
        name: ' ',
        image: 'Oso.jpeg',
        price: ' '
      },
      show: true
    }
  },
  methods: {
    onsubmit (event) {
      event.preventDefault()
      alert(JSON.stringify(this.form))
    },
    onReset (event) {
      console.log(event)
      this.form.email = ''
      this.form.name = ''
      this.form.cvc = ''
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
      this.$refs['my-modal'].hide()
      let dataToSend = {
        product_id: this.id | ' ',
        credit_card: this.form.credit_card | ' ',
        cvc: this.form.cvc | ' ',
        cc_owner: this.form.name | ' ',
        cc_exp_date: this.form.exp_date | ' '
      }

      const path = this.devPath + `/order/add/${this.email}`
      console.log(dataToSend)

      axios.post(path, dataToSend, {
        auth: { username: this.token }
      })
        .then((res) => {
          console.log('RESPOND ORDER', res)
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
</style>
