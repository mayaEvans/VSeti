<template>
  <div name="content" style="margin-top: 125px;">
    <div style="margin-left: 10%; margin-right: 10%;margin-bottom: 10px;">
      <h1>Завершение курса</h1>
      <p>Благодарим вас за участие в онлайн-курсе «{{ $store.state.courses.current.name }}»! Поздравляем с его
        завершением!<br>

        Мы рады, что вы прошли этот путь до конца. Надеемся, что материалы и задания были для вас полезны, а учебный
        процесс оставил положительные впечатления!<br><br>

        Для получения сертификата нажмите на соответсвующую кнопку. Он также появится у вас в личном кабинете.<br>

        Вы в свою очередь можете поделиться впечатлениями о прохождении курса, оставив отзыв.<br><br>

        <i>До новых встреч! Желаем дальнейших успехов!</i></p>

      <div>
        <h2>Получить сертефикат</h2>
        <button @click="getCertificate" class="btn-dark btn" style="margin: 16px 16px 40px 0px;">Скачать</button>
      </div>

      <div>
        <h2>Оставить отзыв</h2>
        <div class="form-group">
          <b-form-textarea
              v-model="review"
              id="textarea"
              placeholder="Enter something..."
              rows="3"
              max-rows="6"
          ></b-form-textarea>
          <div class="star-rating" style="margin-top: 15px">
            <div class="star-rating__wrap">
              <input class="star-rating__input" id="star-5" type="radio" name="rating" v-model="rating" value="5">
              <label class="star-rating__ico fa fa-star-o fa-lg" for="star-5" title="Отлично"></label>
              <input class="star-rating__input" id="star-4" type="radio" name="rating" v-model="rating" value="4">
              <label class="star-rating__ico fa fa-star-o fa-lg" for="star-4" title="Хорошо"></label>
              <input class="star-rating__input" id="star-3" type="radio" name="rating" v-model="rating" value="3">
              <label class="star-rating__ico fa fa-star-o fa-lg" for="star-3" title="Удовлетворительно"></label>
              <input class="star-rating__input" id="star-2" type="radio" name="rating" v-model="rating" value="2">
              <label class="star-rating__ico fa fa-star-o fa-lg" for="star-2" title="Плохо"></label>
              <input class="star-rating__input" id="star-1" type="radio" name="rating" v-model="rating" value="1">
              <label class="star-rating__ico fa fa-star-o fa-lg" for="star-1" title="Ужасно"></label>
            </div>
          </div>
        </div>
        <button @click="postReview" class="btn-dark btn" style="margin: 16px 0px 40px 0px;">Отправить</button>
      </div>
      <div>
        <button @click="toCatalog" class="btn-dark btn" style="margin:0 auto; display: block; padding: 5px 30px">Завершить</button>
      </div>
    </div>
  </div>
</template>

<script>
import {router} from "@/router";

export default {
  name: "CompleteCourse",
  data() {
    return {
      rating: null,
      review: null
    }
  },
  methods: {
    toCatalog: function () {
      router.push("../../../app/catalog/")
    },
    postReview: function (){
      this.$store.state.config.api_client.post('api/v1/reviews/course/' + this.$store.state.courses.current.id, {
        'user': this.$store.state.config.api_client,
        'course': this.$store.state.courses.current.id,
        'text': this.review,
        'rating': this.rating
      }).then(
          this.$toast.success("Отзыв оставлен!")
      )
    },
    getCertificate: function (){
          for(let i=0; i<this.$store.state.certificates.list.length; i++) {
            if (this.$store.state.certificates.list[i].course.name === this.$store.state.courses.current.name) {
              this.$store.state.config.api_client.get('api/v1/certificates/' + this.$store.state.certificates.list[i].id)
              break;
            }
          }
          this.$store.state.config.api_client.post('api/v1/certificates/course/' + this.$store.state.courses.current.id)

    },
    goUser: function(){

    }
  },
  mounted() {
    this.$store.dispatch('lessons/GET_COURSE_DATA', this.$route.params.id)
    this.$store.dispatch('certificates/GET_CERT')
  },
  computed: {
    function() {
      return this.$store.getters['lessons/COURSE_DATA'],
          this.$store.getters['certificates/CERT']
    }
  }
}
</script>

<style scoped>
.star-rating{
  font-size: 0;
}
.star-rating__wrap{
  display: inline-block;
  font-size: 1rem;
}
.star-rating__wrap:after{
  content: "";
  display: table;
  clear: both;
}
.star-rating__ico{
  float: right;
  padding-left: 2px;
  cursor: pointer;
  color: #FFB300;
}
.star-rating__ico:last-child{
  padding-left: 0;
}
.star-rating__input{
  display: none;
}
.star-rating__ico:hover:before,
.star-rating__ico:hover ~ .star-rating__ico:before,
.star-rating__input:checked ~ .star-rating__ico:before
{
  content: "\f005";
}

h1{
  font-weight: bold;
  font-size: 30px;
}
h2{
  font-size: 20px;
  font-weight: bold;
}
</style>