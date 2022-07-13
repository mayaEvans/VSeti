<template>
  <div style="font-family: Rubik, sans-serif">
    <b-navbar type="dark" variant="dark" fixed="top">
      <b-navbar-nav>
        <b-navbar-brand to="/app/catalog/">
          <img src="../../public/media/icons/logo.svg" to="/app/catalog/" width="144" height="82" class="d-inline-block align-text-center">
          #ВСЕТИ</b-navbar-brand>
      </b-navbar-nav>
      <div class="position-absolute text-center end-0" style="margin-right: 10px;">
        <b-navbar-nav>
          <b-nav-item to="/app/catalog/">Каталог</b-nav-item>
          <b-nav-item to="/app/mycourses/">Мои курсы</b-nav-item>
          <b-nav-item class="text" to="/account/login/">Выйти</b-nav-item>
        </b-navbar-nav>
      </div>
      </b-navbar>
  </div>
</template>
<script>
export default {
  name: "HeaderWrapper"
}
</script>

<style scoped>
b-navbar{

}
div{
  font-weight: bold;
  font-size: 20px;
}
</style>