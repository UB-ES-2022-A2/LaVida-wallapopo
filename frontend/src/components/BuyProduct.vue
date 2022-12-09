<template>
  <div>
    <NavigationBar :logged="logged" :key="logged" :token="token" />
    <b-container class="bv-example-row">
      <b-row align-h="center">
        <h2>Comprar producto</h2>
      </b-row>
      <!-- Card product-->
      <b-row class="center mb-2 ml-0 mt-2 mr-2">
        <b-card
          no-body
          class="overflow-hidden p-3"
          style="max-width: 540px, justify-content:center"
        >
          <b-row no-gutters>
            <b-col md="4">
              <b-card-img
                src="https://picsum.photos/400/400/?image=20"
                alt="Image"
                class="rounded-0"
                style="max-width: 15rem"
              ></b-card-img>
            </b-col>
            <b-col md="8">
              <b-card-body title="Horizontal Card">
                <b-card-text>
                  This is a wider card with supporting text as a natural lead-in
                  to additional content. This content is a little bit longer.
                </b-card-text>
              </b-card-body>
            </b-col>
          </b-row>
        </b-card>
      </b-row>

      <!-- Formulario -->

      <b-form @submit="onSubmit" @reset="onReset" v-if="show" class="ml-0 mr-2">
        <b-form-group
          id="input-group-1"
          label="Tarjeta de credito"
          label-for="input-1"
          description="We'll never share your credit card  with anyone else."
        >
          <b-form-input
            id="input-1"
            v-model="form.email"
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
        <b-row>
          <b-col col="6">
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
          <b-col col="6">
            <b-form-group id="input-group-3" label="Date" label-for="input-3">
              <b-form-input
                id="input-1"
                v-model="form.cvc"
                type="email"
                placeholder="Mete tu tarjeta :D"
                required
              ></b-form-input>
            </b-form-group>
          </b-col>
          </b-row>
          <b-row align-h="center">
          <b-button>Comprar</b-button>
          </b-row>
      </b-form>
    </b-container>
  </div>
</template>

<script>
import NavigationBar from './NavigationBar.vue'

export default {
  name: 'BuyProdcut',
  components: {
    NavigationBar
  },
  data () {
    return {
      form: {
        email: '',
        name: '',
        cvc: '',
        food: null,
        checked: []
      },
      foods: [
        { text: 'Select One', value: null },
        'Carrots',
        'Beans',
        'Tomatoes',
        'Corn'
      ],
      show: true
    }
  }
}
</script>
