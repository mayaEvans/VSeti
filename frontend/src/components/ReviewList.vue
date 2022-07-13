<template>
  <div>
    <review
        style="margin: 10px"
        :elem="elem"
        v-for="elem in $store.state.reviews.list"
        :key="elem['id']"
    ></review>
  </div>
</template>

<script>
import Review from "@/components/Review";

export default {
  name: "ReviewList",
  components: {Review},
  mounted() {
    this.$store.dispatch('reviews/GET_REVIEWS', this.$route.params.id)
  },
  computed: {
    function () {
      return this.$store.getters['reviews/REVIEWS']
    }
  },
}
</script>

<style scoped>

</style>