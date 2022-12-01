<template>
  <div id="navbarfiltros">
    <div class="mb-4">
      <button type="button" class="btn btn-outline-dark mx-1" v-b-toggle.sidebar-backdrop>Filtros</button>
      <b-button variant="info" v-if="chip1" @click="checkChipCategories">
        {{ category }}
        <font-awesome-icon icon="fa-circle-xmark"/>
      </b-button>
      <b-button variant="info" v-if="chip2" @click="checkChipPrice">
        {{this.price0}} - {{this.price1}}€
        <font-awesome-icon icon="fa-circle-xmark"/>
      </b-button>
      <b-button variant="info" v-if="chip3" @click="checkChipStat1">
        Nuevo
        <font-awesome-icon icon="fa-circle-xmark"/>
      </b-button>
      <b-button variant="info" v-if="chip5" @click="checkChipStat2">
        Casi Nuevo
        <font-awesome-icon icon="fa-circle-xmark"/>
      </b-button>
      <b-button variant="info" v-if="chip6" @click="checkChipStat3">
        Usado
        <font-awesome-icon icon="fa-circle-xmark"/>
      </b-button>
      <b-button variant="info" v-if="chip4" @click="checkChipTime">
        {{this.tiempo[this.date].text}}
        <font-awesome-icon icon="fa-circle-xmark"/>
      </b-button>
    </div>
      <div>
        <b-sidebar
          id="sidebar-backdrop"
          title="Filtros"
          bg-variant="white"
          backdrop
          shadow
        >
          <div class="px-3 py-2">
            <hr/>
            <p><strong>¿Qué categoría buscas?</strong></p>
            <b-form-select v-model="category" :options="categorias"></b-form-select>
            <hr/>
            <p><strong>¿Cuánto quieres pagar?</strong></p>
            <div class="row">
              <div class="col-sm">
                <p>Desde:</p>
                <input v-model="price0" type="number" placeholder="0" min="0" :max="price1" step="5">
              </div>
              <div class="col-sm">
                <p>Hasta:</p>
                <input v-model="price1" type="number" placeholder="10000" :min="price0" step="5">
              </div>
            </div>
            <hr/>
            <p><strong>¿Qué estado buscas?</strong></p>
            <b-form-checkbox
              id="checkbox-1"
              v-model="status_nuevo"
              name="checkbox-1"
            >
              Nuevo
            </b-form-checkbox>
            <b-form-checkbox
              id="checkbox-2"
              v-model="status_casi_nuevo"
              name="checkbox-2"
            >
              Casi nuevo
            </b-form-checkbox>
            <b-form-checkbox
              id="checkbox-3"
              v-model="status_usado"
              name="checkbox-3"
            >
              Usado
            </b-form-checkbox>
            <hr/>
            <p><strong>¿Desde cuándo?</strong></p>
            <b-form-select v-model="date" :options="tiempo"></b-form-select>
            <hr/>
            <div class="text-right mt-3">
              <button type="button" class="btn btn-secondary" v-b-toggle.sidebar-backdrop>Cancelar</button>
              <button type="button" class="btn btn-success" v-b-toggle.sidebar-backdrop @click="applyFilter">Aplicar</button>
            </div>
          </div>
        </b-sidebar>
      </div>
  </div>
</template>

<script>
import { devWeb, prodWeb } from '../store'

export default {
  props: {
    category2: String
  },
  data () {
    return {
      name: 'navbarfiltros',
      status_nuevo: false,
      status_casi_nuevo: false,
      status_usado: false,
      cond: ['Nuevo', 'Casi nuevo', 'Usado'],
      price0: 0,
      price1: 10000,
      category: null,
      date: -1,
      chip1: false,
      chip2: false,
      chip3: false,
      chip4: false,
      chip5: false,
      chip6: false,
      prodPath: prodWeb,
      devPath: devWeb,
      zonas: null,
      removeCat: false,
      tiempo: [
        { value: -1, text: 'Elige un orden', disabled: true },
        { value: 1, text: 'Más recientes' },
        { value: 2, text: 'Más antiguos' }
      ],
      categorias: [
        { value: null, text: 'Elige una categoria', disabled: true },
        { value: 'Coches', text: 'Coches' },
        { value: 'Motos', text: 'Motos' },
        { value: 'Motor y Accesorios', text: 'Motor y Accesorios' },
        { value: 'Moda y Accesorios', text: 'Moda y Accesorios' },
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
      ]
    }
  },
  created () {
    this.category = this.category2
    if (this.category) this.applyFilter()
  },
  methods: {
    applyFilter () {
      this.checkChips()
      let cond = []
      if (!this.status_usado && !this.status_nuevo && !this.status_casi_nuevo) {
        cond = this.cond
      } else {
        if (this.status_usado) cond.push('Usado')
        if (this.status_casi_nuevo) cond.push('Casi nuevo')
        if (this.status_nuevo) cond.push('Nuevo')
      }

      let category
      if (this.category !== null || this.removeCat) {
        this.removeCat = false
        category = this.category
      } else {
        category = this.category2 ? this.category2 : this.category
      }
      const parameters = {
        category: category,
        conditions: cond,
        date: this.date === -1 ? 0 : this.date,
        price0: parseInt(this.price0),
        price1: parseInt(this.price1)
      }
      this.$emit('productsList', parameters)
    },
    checkChips () {
      if (this.category !== null) {
        this.chip1 = true
      }
      if (parseInt(this.price0) !== 0 || parseInt(this.price1) !== 10000) {
        this.chip2 = true
      }
      if (this.status_nuevo) {
        this.chip3 = true
      }
      if (this.status_casi_nuevo) {
        this.chip5 = true
      }
      if (this.status_usado) {
        this.chip6 = true
      }
      if (this.date !== -1) {
        this.chip4 = true
      }
      if (parseInt(this.price0) === 0 && parseInt(this.price1) === 10000) {
        this.chip2 = false
      }
    },
    checkChipCategories () {
      this.chip1 = false
      this.category = null
      this.removeCat = true
      this.applyFilter()
    },
    checkChipPrice () {
      this.chip2 = false
      this.price0 = 0
      this.price1 = 10000
      this.applyFilter()
    },
    checkChipStat1 () {
      this.chip3 = false
      this.status_nuevo = false
      this.applyFilter()
    },
    checkChipTime () {
      this.chip4 = false
      this.date = -1
      this.applyFilter()
    },
    checkChipStat2 () {
      this.chip5 = false
      this.status_casi_nuevo = false
      this.applyFilter()
    },
    checkChipStat3 () {
      this.chip6 = false
      this.status_usado = false
      this.applyFilter()
    }
  }
}
</script>
