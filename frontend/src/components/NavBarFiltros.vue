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
            <b-form-select v-model="selected" :options="categorias"></b-form-select>
            <hr/>
            <p><strong>¿Cuánto quieres pagar?</strong></p>
            <div class="row">
              <div class="col-sm">
                <p>Desde:</p>
                <input type="number" placeholder="0" min="0" max="10000" step="5">
              </div>
              <div class="col-sm">
                <p>Hasta:</p>
                <input type="number" placeholder="10000" min="0" max="10000" step="5">
              </div>
            </div>
            <hr/>
            <p><strong>¿Qué estado buscas?</strong></p>
            <b-form-checkbox
              id="checkbox-1"
              v-model="status_nuevo"
              name="checkbox-1"
              value="True"
              unchecked-value="False"
            >
              Nuevo
            </b-form-checkbox>
            <b-form-checkbox
              id="checkbox-2"
              v-model="status_casi_nuevo"
              name="checkbox-2"
              value="True"
              unchecked-value="False"
            >
              Casi nuevo
            </b-form-checkbox>
            <b-form-checkbox
              id="checkbox-3"
              v-model="status_usado"
              name="checkbox-3"
              value="True"
              unchecked-value="False"
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
            <b-form-select v-model="selected2" :options="tiempo"></b-form-select>
            <hr/>
            <div class="text-right mt-3">
              <button type="button" class="btn btn-secondary" v-b-toggle.sidebar-backdrop>Cancelar</button>
              <button type="button" class="btn btn-success">Aplicar</button>
            </div>
          </div>
        </b-sidebar>
      </div>
      <nav class="navbar navbar-expand-sm">
        <b-collapse id="collapse-1" class="mt-2">
          <b-card>
            <p><strong>¿Qué categoría buscas?</strong></p>
            <b-form-select v-model="selected" :options="categorias"></b-form-select>
            <div class="text-right mt-3">
              <button type="button" class="btn btn-secondary" v-b-toggle.collapse-1>Cancelar</button>
              <button type="button" class="btn btn-success">Aplicar</button>
            </div>
          </b-card>
        </b-collapse>
        <b-collapse id="collapse-2" class="mt-2">
          <b-card>
            <p><strong>¿Cuánto quieres pagar?</strong></p>
            <div class="row">
              <div class="col-sm">
                <p>Desde:</p>
                <input type="number" placeholder="0" min="0" max="10000" step="5">
              </div>
              <div class="col-sm">
                <p>Hasta:</p>
                <input type="number" placeholder="10000" min="0" max="10000" step="5">
              </div>
            </div>
            <div class="text-right mt-3">
              <button type="button" class="btn btn-secondary" v-b-toggle.collapse-2>Cancelar</button>
              <button type="button" class="btn btn-success">Aplicar</button>
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
              value="True"
              unchecked-value="False"
            >
              Nuevo
            </b-form-checkbox>
            <b-form-checkbox
              id="checkbox-2"
              v-model="status_casi_nuevo"
              name="checkbox-2"
              value="True"
              unchecked-value="False"
            >
              Casi nuevo
            </b-form-checkbox>
            <b-form-checkbox
              id="checkbox-3"
              v-model="status_usado"
              name="checkbox-3"
              value="True"
              unchecked-value="False"
            >
              Usado
            </b-form-checkbox>
            <div class="text-right mt-3">
              <button type="button" class="btn btn-secondary" v-b-toggle.collapse-3>Cancelar</button>
              <button type="button" class="btn btn-success">Aplicar</button>
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
              <button type="button" class="btn btn-success">Aplicar</button>
            </div>
          </b-card>
        </b-collapse>
        <b-collapse id="collapse-5" class="mt-2">
          <b-card>
            <p><strong>¿Desde cuándo?</strong></p>
            <b-form-select v-model="selected2" :options="tiempo"></b-form-select>
            <div class="text-right mt-3">
              <button type="button" class="btn btn-secondary" v-b-toggle.collapse-5>Cancelar</button>
              <button type="button" class="btn btn-success">Aplicar</button>
            </div>
          </b-card>
        </b-collapse>
      </nav>
  </div>
</template>

<script>
export default {
  data () {
    return {
      name: 'navbarfiltros',
      status_nuevo: 'False',
      status_casi_nuevo: 'False',
      status_usado: 'False',
      selected: null,
      selected2: null,
      tiempo: [
        { value: null, text: 'Elige un orden' },
        { value: 'a', text: 'Más recientes' },
        { value: 'b', text: 'Más antiguos' }
      ],
      categorias: [
        { value: null, text: 'Elige una categoria' },
        { value: '1', text: 'Coches' },
        { value: '2', text: 'Motos' },
        { value: '3', text: 'Motor y Accesorios' },
        { value: '4', text: 'Moda y Accesorios' },
        { value: '5', text: 'TV, Audio y Foto' },
        { value: '6', text: 'Móviles y Telefonía' },
        { value: '7', text: 'Informática y Electrónica' },
        { value: '8', text: 'Deporte y Ocio' },
        { value: '9', text: 'Bicicletas' },
        { value: '10', text: 'Consolas y Videojuegos' },
        { value: '11', text: 'Hogar y Jardín' },
        { value: '12', text: 'Electrodomésticos' },
        { value: '13', text: 'Cine' },
        { value: '14', text: 'Libros y Música' },
        { value: '15', text: 'Niños y Bebés' },
        { value: '16', text: 'Coleccionismo' },
        { value: '17', text: 'Construcción y Reformas' },
        { value: '18', text: 'Industria y Agricultura' },
        { value: '19', text: 'Otros' }
      ]
    }
  }
}
</script>
