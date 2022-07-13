<template>
  <div>
    <course-card
        :elem="elem"
        v-for="elem in $store.state.courses.list"
        :key="elem['id']"
    ></course-card>
  </div>
</template>

<script>
import CourseCard from "@/components/CourseCard";

export default {
  name: "CoursesListMy",
  components: {CourseCard},
  mounted() {
    this.$store.dispatch('courses/GET_MY_COURSES')
  },
  computed: {
    function() {
      return this.$store.getters['courses/COURSES']
    }
  },
}

</script>

<style scoped>

</style>