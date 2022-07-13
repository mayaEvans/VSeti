<template>
  <div>
    <b-nav-item href="${this.elem['id']}">
      {{ elem['name'] }}
    </b-nav-item>
  </div>
</template>

<script>
export default {
name: "Sidebar",
  props:['elem']
}
</script>

<style scoped>

</style>