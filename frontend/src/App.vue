<template>
  <div id="app">
    <router-view name="page"></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  created() {
    this.$store.dispatch('config/createAxiosClient')
  }
}
</script>
<style>
</style>

