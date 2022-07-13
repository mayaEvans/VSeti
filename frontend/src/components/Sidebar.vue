<template>
  <div aria-expanded="true">
    <b-sidebar id="sidebar-variant"
               bg-variant="dark"
               visible v-show="true"
               no-close-on-backdrop
               no-slide aria-expanded="true"
               no-close-on-route-change
               no-header shadow>
      <b-navbar-brand href="../" style="margin-top: 8px;">
        <img href="../" src="../../public/media/icons/logo.svg" width="144" height="82" class="d-inline-block align-text-center">
        <h4 style="font-weight: bold; display: inline-block; font-size: 20px;">#ВСЕТИ</h4>
      </b-navbar-brand>
      <div class="p-3">
        <nav class="mb-3" style="margin-left: 14px;">
          <b-nav vertical>
            <sidebar-list></sidebar-list>
            <b-nav-item :to="'/app/catalog/complete/' + $store.state.courses.current.id ">Завершение курса</b-nav-item>
          </b-nav>
        </nav>
      </div>
    </b-sidebar>
  </div>
</template>
<script>
import SidebarList from "@/components/SidebarList";

export default {
  components: {SidebarList},
  mounted() {
    this.$store.dispatch('lessons/GET_LESSONS', this.$store.state.lessons.current.course)
  },
  computed: {
    function() {
      return this.$store.getters['lessons/LESSONS']
    }
  }
}
</script>