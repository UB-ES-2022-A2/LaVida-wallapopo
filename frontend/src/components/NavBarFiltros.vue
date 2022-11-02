<template>
  <div id="navbarfiltros">
      <p>
        <button type="button" class="btn btn-outline-dark mx-1" v-b-toggle.sidebar-backdrop>Filtros</button>
        <button type="button" class="btn btn-outline-dark mr-1" v-b-toggle.collapse-1>Categorías</button>
        <button type="button" class="btn btn-outline-dark mr-1" v-b-toggle.collapse-2>Precio</button>
        <button type="button" class="btn btn-outline-dark mr-1" v-b-toggle.collapse-3>Estado del Producto</button>
        <button type="button" class="btn btn-outline-dark" v-b-toggle.collapse-4>Ubicación</button>
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
            <b-form-group label="Escoge una categoría:" label-for="bg-categorias" label-cols-sm="4" label-cols-lg="12">
              <b-form-select id="bg-categorias" v-model="categorias" :options="categorias"></b-form-select>
            </b-form-group>
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
            <b-form-group label="Escoge una categoría:" label-for="bg-categorias" label-cols-sm="4" label-cols-lg="12">
              <b-form-select id="bg-categorias" v-model="categorias" :options="categorias"></b-form-select>
            </b-form-group>
            <div class="text-right">
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
      status_usado: 'False'
    }
  }
}
</script>
