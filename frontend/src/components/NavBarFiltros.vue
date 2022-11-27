<template>
  <div id="navbarfiltros">
      <p>
        <button type="button" class="btn btn-outline-dark mx-1" v-b-toggle.sidebar-backdrop>Filtros</button>
        <button type="button" class="btn btn-outline-dark mr-1" v-b-toggle.collapse-1>Categorías</button>
        <button type="button" class="btn btn-outline-dark mr-1" v-b-toggle.collapse-2>Precio</button>
        <button type="button" class="btn btn-outline-dark mr-1" v-b-toggle.collapse-3>Estado del Producto</button>
        <button type="button" class="btn btn-outline-dark mr-1" v-b-toggle.collapse-4>Ubicación</button>
        <button type="button" class="btn btn-outline-dark" v-b-toggle.collapse-5>Tiempo</button>
      </p>
      <div>
        <b-sidebar
          id="sidebar-backdrop"
          title="Filtros"
          bg-variant="white"
          :backdrop-variant="dark"
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
            <p><strong>¿Dónde?</strong></p>
            <b-form-group label="Escoge una zona:" label-for="bg-zonas" label-cols-sm="4" label-cols-lg="12">
              <b-form-select id="bg-zonas" v-model="zonas" :options="zonas"></b-form-select>
            </b-form-group>
            <hr/>
            <p><strong>¿Desde cuándo?</strong></p>
            <b-form-select v-model="date" :options="tiempo"></b-form-select>
            <hr/>
            <div class="text-right mt-3">
              <button type="button" class="btn btn-secondary" v-b-toggle.sidebar-backdrop>Cancelar</button>
              <button type="button" class="btn btn-success" @click="applyFilter">Aplicar</button>
            </div>
          </div>
        </b-sidebar>
      </div>
      <nav class="navbar navbar-expand-sm">
        <b-collapse id="collapse-1" class="mt-2">
          <b-card>
            <p><strong>¿Qué categoría buscas?</strong></p>
            <b-form-select v-model="category" :options="categorias"></b-form-select>
            <div class="text-right mt-3">
              <button type="button" class="btn btn-secondary" v-b-toggle.collapse-1>Cancelar</button>
              <button type="button" class="btn btn-success" @click="applyFilter">Aplicar</button>
            </div>
          </b-card>
        </b-collapse>
        <b-collapse id="collapse-2" class="mt-2">
          <b-card>
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
            <div class="text-right mt-3">
              <button type="button" class="btn btn-secondary" v-b-toggle.collapse-2>Cancelar</button>
              <button type="button" class="btn btn-success" @click="applyFilter">Aplicar</button>
            </div>
          </b-card>
        </b-collapse>
        <b-collapse id="collapse-3" class="mt-2">
          <b-card>
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
            <div class="text-right mt-3">
              <button type="button" class="btn btn-secondary" v-b-toggle.collapse-3>Cancelar</button>
              <button type="button" class="btn btn-success" @click="applyFilter">Aplicar</button>
            </div>
          </b-card>
        </b-collapse>
        <b-collapse id="collapse-4" class="mt-2">
          <b-card>
            <p><strong>¿Dónde?</strong></p>
            <b-form-group label="Escoge una zona:" label-for="bg-zonas" label-cols-sm="4" label-cols-lg="12">
              <b-form-select id="bg-zonas" v-model="zonas" :options="zonas"></b-form-select>
            </b-form-group>
            <div class="text-right mt-3">
              <button type="button" class="btn btn-secondary" v-b-toggle.collapse-4>Cancelar</button>
              <button type="button" class="btn btn-success" @click="applyFilter">Aplicar</button>
            </div>
          </b-card>
        </b-collapse>
        <b-collapse id="collapse-5" class="mt-2">
          <b-card>
            <p><strong>¿Desde cuándo?</strong></p>
            <b-form-select v-model="date" :options="tiempo"></b-form-select>
            <div class="text-right mt-3">
              <button type="button" class="btn btn-secondary" v-b-toggle.collapse-5>Cancelar</button>
              <button :disabled="date===-1" type="button" class="btn btn-success" @click="applyFilter">Aplicar</button>
            </div>
          </b-card>
        </b-collapse>
      </nav>
  </div>
</template>

<script>
import axios from 'axios'
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
      price1: 99999999,
      category: null,
      date: -1,
      prodPath: prodWeb,
      devPath: devWeb,
      zonas: null,
      tiempo: [
        { value: -1, text: 'Elige un orden', disabled: true },
        { value: 1, text: 'Más recientes' },
        { value: 0, text: 'Más antiguos' }
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
  methods: {
    applyFilter () {
      const path = this.prodPath + `/filter`
      let cond = []
      if (!this.status_usado && !this.status_nuevo && !this.status_casi_nuevo) {
        cond = this.cond
      } else {
        if (this.status_usado) cond.push('Usado')
        if (this.status_casi_nuevo) cond.push('Casi nuevo')
        if (this.status_nuevo) cond.push('Nuevo')
      }

      let category
      if (this.category !== null) {
        category = this.category
      } else {
        category = this.category2 ? this.category2 : this.category
      }
      const parameters = {
        category: category,
        conditions: cond,
        date: this.date === -1 ? 0 : this.date,
        price0: this.price0,
        price1: this.price1
      }
      axios.post(path, parameters)
        .then((res) => {
          console.log(res.data)
          this.$emit('productsList', res.data.products_list)
        })
        .catch((error) => {
          console.error(error)
          console.log(parameters)
        })
    }
  }
}
</script>
