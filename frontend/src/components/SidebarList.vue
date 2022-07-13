<template>
  <div>
      <sidebar-nav-item
          v-for="elem in $store.state.lessons.list"
          :elem="elem"
          :key="elem['id']"></sidebar-nav-item>
  </div>
</template>

<script>
import SidebarNavItem from "@/components/SidebarNavItem";
export default {
name: "SidebarList",
  components: {SidebarNavItem},
  mounted() {
    this.$store.dispatch('lessons/GET_LESSONS', this.$store.state.lessons.current.course)
  },
  computed(){
    return this.$store.getters['lessons/LESSONS']
  }
}
</script>

<style scoped>

</style>