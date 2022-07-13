<template>
  <div>
    <b-navbar type="dark" variant="dark" fixed="top">
      <b-navbar-nav>
        <b-navbar-brand href="#">
          <img src="../../public/media/icons/logo.svg" width="144" height="82" class="d-inline-block align-text-center">
          #ВСЕТИ
        </b-navbar-brand>
      </b-navbar-nav>
      <div style="margin-right: 10px;" class="position-absolute text-center end-0">
        <b-navbar-nav>
          <b-nav-item to="/account/login">Авторизация</b-nav-item>
          <b-nav-item >/</b-nav-item>
          <b-nav-item to="/account/register">Регистрация</b-nav-item>
        </b-navbar-nav>
      </div>
    </b-navbar>
  </div>
</template>

<style scoped>
</style>

<script>
export default {
  name: "DefaultHeader"
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@900&display=swap');
div{
  font-weight: bold;
  font-size: 20px;
}
</style>