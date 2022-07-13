<template>
  <div class="justify-content-md-center" style="float:left">
    <b-card style="width: 346px; height: 215px; margin: 15px; padding: 5px;">
      <div style="height: 50%;">
        <div>
          <strong class="card-title"
                  style="margin: 0;-webkit-line-clamp: 1; display: -webkit-box; -webkit-box-orient: vertical;  overflow: hidden; font-size: 24px;">{{
              elem['name']
            }}</strong>
        </div>
        <b-card-text
            style="margin: 0;-webkit-line-clamp: 2; display: -webkit-box; -webkit-box-orient: vertical;  overflow: hidden;">
          {{ elem['short_description'] }}
        </b-card-text>
      </div>
      <div style="height: 50%; display:inline-block; vertical-align: bottom;">
        <div>
          <b-avatar icon="people-fill"></b-avatar>
          {{ elem['listeners_number'] }}
          <b-avatar icon="star-fill"></b-avatar>
          {{ elem['rating'] }}
        </div>
        <b-button @click="openCourse">Узнать больше</b-button>
      </div>
    </b-card>
  </div>
</template>

<script>
import {router} from "@/router";

export default {
  name: "CourseCard",
  props: ['elem'],
  methods: {
    openCourse: function () {
      router.push("/app/catalog/" + this.elem['id']);
    }
  }
}
</script>

<style scoped>
</style>