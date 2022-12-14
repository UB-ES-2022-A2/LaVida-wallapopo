<template>
  <div id="menu_lateral">
    <nav class="navbar navbar-light border" style="width: 90%;
    position: absolute;
    top: -10px;
    bottom: 0;
    background-color: #f8f9fa;
    ">
      <ul class="navbar-nav" style="height: 90%;">
        <li class="nav-item mb-5">
          <a style="color: #000000" class="nav-link h5" href="#profile"><img src="@/assets/icons/user.png" alt="User icon" style="width: 40px"/> Perfil </a>
        </li>
        <li class="nav-item mb-4">
          <a style="color: #000000" class="nav-link h6" href="#introducirlinkreseñas"><img src="@/assets/icons/review.png" alt="User icon" style="width: 30px"/> Reseñas </a>
        </li>
        <li class="nav-item mb-4">
          <a style="color: #000000" class="nav-link h6" href="#introducirlinkcompras"><img src="@/assets/icons/buy.png" alt="User icon" style="width: 30px"/> Compras </a>
        </li>
        <li class="nav-item mb-4">
          <a style="color: #000000" class="nav-link h6" href="#introducirlinkcompras"><img src="@/assets/icons/sell.png" alt="User icon" style="width: 30px"/> Ventas </a>
        </li>
        <li class="nav-item mb-4">
          <a style="color: #000000" class="nav-link h6" href="#introducirlinkfavoritos"><img src="@/assets/heart.png" alt="User icon" style="width: 30px"/> Favoritos </a>
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

<style>

.nav-item.mb-4:hover {
  background-color: #e6e8eb;
}

.nav-item.mb-5:hover {
  background-color: #e6e8eb;
}

</style>
