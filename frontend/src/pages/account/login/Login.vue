<template>
  <b-container fluid name="content" class="position-absolute top-50 start-50 translate-middle  d-flex flex-column container w-25">
    <b-form-input
        v-model="inputLogin"
        class="mt-3 login-input w-100"
        type="email"
        name="email"
        placeholder="Логин"
    ></b-form-input>
    <b-input
        v-model="inputPassword"
        class="my-3 login-input w-100 form-control"
        type="password"
        name="password"
        placeholder="Пароль"
    ></b-input>
    <button @click="loginUser" class="btn-dark btn">Войти</button>
    <button @click="forgetPassword" class="btn btn-link">Забыли пароль?</button>
  </b-container>
</template>

<script>
import {router} from "@/router";

export default {
  name: "Login",
  data() {
    return {
      inputLogin: null,
      inputPassword: null
    }
  },
  methods: {
    forgetPassword: function (){
      this.$store.state.config.api_client.post('/api/v1/users/forget_password/', {
        'email': this.inputLogin
      }).then(this.$toast.info("Запрос о смене пароля отправлен на почту"))
    },
    loginUser: function () {
      this.$store.state.config.api_client.post('/api/v1/users/login/', {
        'email': this.inputLogin,
        'password': this.inputPassword
      }).then((response) => {
        if(response.status == 200){
        this.$store.commit('config/setToken', response.data.result.key),
        router.push("/app/catalog/")
        } else if(response.status == 400) {
          this.$toast.error("Неверно введены данные или аккаунт не активирован")
        }
      })
    },
  },
}
</script>
<style scoped>

</style>
