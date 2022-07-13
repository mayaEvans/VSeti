<template>
  <b-container style="border-left:3px solid grey; padding-left:10px;">
    <div style="display:inline-block;">
      {{ elem['text'] }}
      <div style="display:inline-block;">
        <b-avatar icon="star-fill"></b-avatar>
        {{ elem['rating'] }}
      </div>
    </div>
  </b-container>
</template>

<script>
export default {
  name: "Review",
  props: ['elem'],
}
</script>

<style scoped>

</style>