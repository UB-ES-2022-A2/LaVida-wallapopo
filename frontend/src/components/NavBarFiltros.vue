<template>
  <div id="navbarfiltros">
    <nav class="navbar navbar-expand-md style-navbar">
      <div>
        <button type="button" class="btn btn-outline-dark mr-1" v-b-toggle.collapse-1>Categorías</button>
        <b-collapse id="collapse-1" class="mt-2">
          <b-card>
            <p>
            <b-form-group label="¿Qué categoría buscas?" label-for="bg-categorias" label-cols-sm="4" label-cols-lg="12">
              <b-form-select id="bg-categorias" v-model="categorias" :options="categorias"></b-form-select>
            </b-form-group>
            <div class="text-right">
              <button type="button" class="btn btn-secondary" v-b-toggle.collapse-1>Cancelar</button>
              <button type="button" class="btn btn-success">Aplicar</button>
            </div>
          </b-card>
        </b-collapse>
      </div>
      <div>
        <button type="button" class="btn btn-outline-dark" v-b-toggle.collapse-2>Precio</button>
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
      </div>
      <div>
        <button type="button" class="btn btn-outline-dark" v-b-toggle.collapse-2>Precio</button>
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
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  data () {
    return {
      name: 'navbarfiltros',
      precio: '0'
    }
  }
}
</script>
