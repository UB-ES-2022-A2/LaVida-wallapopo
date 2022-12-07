<template>
  <div id="menu_lateral">
    <nav class="navbar bg-dark navbar-dark" style="width: 90%;
    position: absolute;
    top: -10px;
    bottom: 0;">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="#">Perfil</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Compras</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Ventas</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Favoritos</a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  data () {
    return {
      name: 'menu'
    }
  }
}
</script>
