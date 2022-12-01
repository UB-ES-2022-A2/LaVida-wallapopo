<template>
  <div id="addProduct">
    <NavigationBar class="nav-top" :logged="logged" :key="logged" :email="email" :token="token" />
    <div class="container">
      <h4>INFORMACIÓN DE TU PRODUCTO</h4>
      <!--Product name-->
      <div>
        <b-form-group
          invalid-feedback="Nombre no puede estar vacío"
          :state="nameState"
        >
        <div class="row-2">
          <label>¿Qué estás vendiendo?</label>
          <span>{{nameCharactersLeft}}</span>
        </div>
        <b-form-input
          type="text"
          id="input-1"
          class="form-control"
          placeholder="En pocas palabras..."
          maxlength="50"
          v-model="name"
          :state="nameState"
          required
          autofocus
          trim
        />
        </b-form-group>
      </div>
      <!--Product category-->
      <div>
        <label>Categoría</label>
        <b-form-select
          id="categoryId"
          v-model="category"
          :state="category != null"
          :options="categories"
        >
        </b-form-select>
      </div>
      <!--Product price-->
      <div>
        <b-form-group
          invalid-feedback="Por favor introduce un precio"
          :state="priceState"
        >
          <div class="row-2">
            <label>Precio (€)</label>
          </div>
          <b-form-input
            type="number"
            id="input-2"
            class="form-control"
            placeholder="Sé razonable..."
            :state="priceState"
            required
            v-model="price"
          />
        </b-form-group>
      </div>
      <!--Product state-->
      <div>
        <label>Estado del producto</label>
        <b-form-select
          id="productStateId"
          v-model="state"
          :options="states"
          :state="state != null"
        >
        </b-form-select>
      </div>
      <!--Product description-->
      <div class="form-label-group">
        <div>
          <label>Descripción:</label>
          <span>{{descCharactersLeft}}</span>
        </div>
          <b-form-textarea
            class="form-control"
            id="productDescription" rows="3"
            placeholder="Añade información relevante como estado del producto..."
            maxlength="1000"
            :state="description.length > 0"
            required
            v-model="description"
            trim
          >
          </b-form-textarea>
          <small class="text-muted font-weight-bold">Escriba la descripción separados por coma para crear tags.</small>
      </div>
    </div>
    <!--Product images-->
    <div class="container">
      <h4>FOTOS</h4>
      <b-form-file
        v-model="images"
        multiple
        :state="images.length > 0"
        placeholder="Puedes seleccionar fotos o arrastrar y soltar fotos aquí"
        drop-placeholder="Suelta fotos aquí..."
        accept="image/*"
        @change="onFileChange"
      >
      </b-form-file>
      <div class="row" style="margin-top:14px">
        <div
          class=" col-6 col-lg-3"
          v-for="(image, key) in images"
          :key="key">
          <div v-if="key === 0">
            <img class="img-thumbnail" :ref="'image'" alt="..."/>
            <p class="text-center">Imagen principal</p>
          </div>
          <div v-else>
            <img class="img-thumbnail" :ref="'image'" alt="..."/>
          </div>
        </div>
      </div>
    </div>
    <!--Product shipment-->
    <div class="container">
      <h4>HAGO ENVÍOS</h4>
      <div>
        <b-form-checkbox
          id="checkboxId"
          v-model="shipment">
          Wallapopo envíos
        </b-form-checkbox>
      </div>
    </div>

    <!--addProduct button-->
    <button
      class="btn btn-primary btn-lg my-2"
      @click="addProduct()"
      style="width: 100%"
      :disabled="name.length===0 || category===null || price===null || state===null || images.length===0 || description.length===0"
    >
      Subir producto
    </button>
    <Footer/>
  </div>
</template>

<script>
import NavigationBar from './NavigationBar.vue'
import Footer from './Footer'
import axios from 'axios'
import {devWeb, prodWeb} from '../store'

export default {
  name: 'addProduct',
  components: {
    NavigationBar,
    Footer
  },
  data () {
    return {
      name: '',
      category: null,
      price: null,
      state: null,
      images: [],
      prodPath: prodWeb,
      devPath: devWeb,
      description: '',
      shipment: false,
      logged: false,
      token: 'g',
      email: localStorage.getItem('email'),
      categories: [
        { value: null, text: 'Selecciona una categoría', disabled: true },
        { value: 'Coches', text: 'Coches' },
        { value: 'Motos', text: 'Motos' },
        { value: 'Motor y Accesorios', text: 'Motor y Accesorios' },
        { value: 'TV, Audio y Foto', text: 'TV, Audio y Foto' },
        { value: 'Móviles y Telefonía', text: 'Móviles y Telefonía' },
        { value: 'Informática y Electrónica', text: 'Informática y Electrónica' },
        { value: 'Deporte y Ocio', text: 'Deporte y Ocio' },
        { value: 'Bicicletas', text: 'Bicicletas' },
        { value: 'Consolas y Videojuegos', text: 'Consolas y Videojuegos' },
        { value: 'Hogar y Jardín', text: 'Hogar y Jardín' },
        { value: 'Electrodomésticos', text: 'Electrodomésticos' },
        { value: 'Cine', text: 'Cine' },
        { value: 'Libros y Música', text: 'Libros y Música' },
        { value: 'Niños y Bebés', text: 'Niños y Bebés' },
        { value: 'Coleccionismo', text: 'Coleccionismo' },
        { value: 'Construcción y Reformas', text: 'Construcción y Reformas' },
        { value: 'Industria y Agricultura', text: 'Industria y Agricultura' },
        { value: 'Otros', text: 'Otros' }
      ],
      states: [
        { value: null, text: 'Escoge un estado', disabled: true },
        { value: 'Nuevo', text: 'Nuevo' },
        { value: 'Casi nuevo', text: 'Casi nuevo' },
        { value: 'Usado', text: 'Usado' }
      ]
    }
  },
  computed: {
    nameState () {
      /* check if name is introduced */
      return this.name.length > 0
    },
    priceState () {
      /* check if price is introduced */
      return this.price > 0
    },
    nameCharactersLeft () {
      /* name max limit is 50 */
      return (50 - this.name.length) + ' / ' + 50
    },
    descCharactersLeft () {
      /* desc max limit is 1000 */
      return (1000 - this.description.length) + ' / ' + 1000
    },
    invalidFeedback () {
      /* Not used for now */
      if (this.name.length > 0) {
        return 'Enter at least 4 characters.'
      }
      return 'Please enter something.'
    }
  },
  methods: {
    isLogged () {
      if (this.token !== null) {
        this.logged = true
      }
    },
    addProduct () {
      const path = this.prodPath + '/catalog/add/' + this.email
      /* params used to add a new product */
      const parameters = {
        name: this.name,
        category: this.category,
        price: this.price,
        condition: this.state,
        description: this.description,
        shipment: this.shipment
      }
      axios.post(path, parameters, {
        auth: {username: this.token}
      })
        .then((res) => {
          alert('Producto añadido correctamente')
          console.log(res)
          this.$router.push({
            name: 'HelloWorld',
            params: {token: this.token, logged: this.logged, email: this.email}
          })
        })
        .catch((error) => {
          alert('Ha ocurrido un error al añadir el producto, vuelve a intentarlo más tarde')
          console.error(error)
        })
    },
    onFileChange (e) {
      var selectedFiles = e.target.files
      /* Only add the first 10 images */
      for (let i = 0; i < selectedFiles.length && i < 10; i++) {
        console.log(selectedFiles[i])
        this.images.push(selectedFiles[i])
      }
      /* Generate URL for every image that the user added */
      for (let i = 0; i < this.images.length; i++) {
        let reader = new FileReader()
        reader.onload = (e) => {
          this.$refs.image[i].src = reader.result
          console.log(this.$refs.image[i].src)
        }
        reader.readAsDataURL(this.images[i])
      }
    }
  },
  mounted () {
    this.email = localStorage.getItem('email')
    this.token = localStorage.getItem('token')
    this.isLogged()
  }
}
</script>

<style scoped>
label {
  padding-top: 10px;
}
span {
  margin-top:16px;
  float: right;
  font-size: 12px;
  color: gray;
}
h4 {
  padding-top: 10px;
  padding-bottom: 5px;
}
.container {
  background-color: whitesmoke;
  border-radius: 10px;
  width: 45%;
  padding-bottom: 20px;
  margin-bottom: 20px;
}

</style>
