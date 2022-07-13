<template>
  <div name="content" style="margin-top: 125px;">
    <sidebar></sidebar>
    <div style="margin-left: 340px; margin-bottom: 15px;">
      <h1>{{ $store.state.lessons.current.name }}</h1>
      <h2>Теория</h2>
      <p v-html="$store.state.lessons.current.theory" style="width: 90%"></p>
      <div v-if="$store.state.question.list.length()!=undefined">
        <h2>Задание</h2>
        <div v-for="(Record, index) in $store.state.question.list" :key="`Record-${index}`" style="margin-bottom: 10px">
          <p v-html="Record.text"></p>
          <div v-if="Record.options.length()!=undefined">
              <b-form-checkbox-group
                            style="text-indent: 5px; margin-left: 5px"
                            v-model="selected"
                            :options="Record.options"
                            text-field="option"
                            value-field="id"
                            >{{ option }}
              </b-form-checkbox-group>
          </div>
          <b-form-input v-else v-model="inputForm" style="width: 90%"></b-form-input>
        </div>
        <b-button @click="sendOptions" style="margin-top: 10px">Отправить</b-button>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "@/components/Sidebar";

export default {
  name: "Course",
  components: {Sidebar},
  mounted() {
    this.$store.dispatch('lessons/GET_LESSON_DATA', this.$route.params.id),
        this.$store.dispatch('question/GET_QUESTION_DATA', this.$route.params.id)
  },
  computed: {
    function() {
      return this.$store.getters['lessons/LESSON_DATA'],
          this.$store.getters['question/QUESTION_DATA']
    }
  },
  data() {
    return {
      selected: [],
      inputForm: null
    }
  },
  methods: {
    sendOptions: function () {
        this.$store.state.config.api_client.post('/api/v1/answers/question/' + this.$store.state.question.list[0].id, {
          'question': this.$store.state.question.list[0].id,
          'user': this.$store.state.config.api_client,
          'text': this.inputForm,
          'selected_options': this.selected
        }).then((response) => {
          if(response.status == 200) {
            this.$toast.success("Задание отправлено!")
          } else {
            this.$toast.error("Произошла ошибка")
          }
        })
    }
  }
}
</script>

<style scoped>
h1 {
  font-weight: bold;
  font-size: 30px;
}

h2 {
  font-size: 20px;
  font-weight: bold;
}
</style>