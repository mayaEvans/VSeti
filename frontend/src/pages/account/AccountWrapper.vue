<template>
  <div>
    <b-container fluid class="account-wrapper h-100 w-100">
      <b-row>
        <before-login></before-login>
      </b-row>
      <b-row class="content-wrapper">
        <b-col>
          <router-view name="content"></router-view>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import BeforeLogin from "@/components/BeforeLogin";
export default {
name: "AccountWrapper",
  components: {BeforeLogin},
}
</script>

<style scoped>
.BeforeLogin{
  margin-bottom: 10px;
}
</style>
