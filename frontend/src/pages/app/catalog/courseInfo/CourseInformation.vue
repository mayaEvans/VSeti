<template>
  <div name="content">
    <div style="margin-top: 108px">

      <div class="bg-secondary" v-if="$store.state.courses.current"
           style="color: white; padding: 40px; background-size: 100%">
        <p style="font-size: 45px; font-weight: bold;">{{ $store.state.courses.current.name }}</p>
        <p style="font-size: 30px">{{ $store.state.courses.current.short_description }}</p>
      </div>

      <div style="margin: 35px;">
        <p style="font-weight: bold">О курсе</p>
        <b-button v-if="this.$store.state.courses.current.user_status==1" style="position:absolute; right: 85px;"
                  class="btn-dark" @click="userCourse">К материалам курса
        </b-button>
        <b-button v-else style="position:absolute; right: 85px;"
                  class="btn-dark" @click="userOnCourse">Поступить на курс
        </b-button>
        <p style="width: 1000px;">{{ $store.state.courses.current.description }}</p>

        <div>
          <p style="font-weight: bold">Отзывы о курсе</p>
          <review-list></review-list>
          <p v-if="this.$store.state.reviews.list==undefined" style="font-size: 16px;"><i>Станьте первым, кто оставит
            отзыв!</i></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {router} from "@/router";
import ReviewList from "@/components/ReviewList";

export default {
  name: "CourseInformation",
  components: {ReviewList},
  mounted() {
    this.$store.dispatch('courses/GET_COURSE_DATA', this.$route.params.id),
        this.$store.dispatch('lessons/GET_LESSONS', this.$route.params.id)
  },
  computed: {
    function() {
      return this.$store.getters['courses/COURSE_DATA'], this.$store.getters['lessons/LESSONS'] ? this.$store.state.reviews.list.length : 0;
    }
  },
  methods: {
    userOnCourse: function () {
      this.$store.state.config.api_client.post('/api/v1/courses/' + this.$route.params.id + '/status').then(() => {
        router.push(this.$route.params.id + "/" + this.$store.state.lessons.list[0].id)
      })
    },
    userCourse: function () {
      router.push(this.$route.params.id + "/" + this.$store.state.lessons.list[0].id)
    }
  }
}

</script>
<style scoped>
p {
  font-size: 20px;
}
</style>