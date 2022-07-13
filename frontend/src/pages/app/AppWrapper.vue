<template>
  <div>
      <header-wrapper></header-wrapper>
      <router-view name="content"/>
  </div>
</template>

<script>
import HeaderWrapper from "@/components/HeaderWrapper";

export default {
  name: "AppWrapper",
  components: {HeaderWrapper},
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@400;700&display=swap');
</style>