<template>
  <b-container name="content" style="margin-top: 125px; padding-bottom: 15px;"
               class="position-absolute top-50 start-50 translate-middle  d-flex flex-column w-50 container">

    <b-input-group>
      <template #prepend>
        <b-input-group-text>Фамилия</b-input-group-text>
      </template>
      <b-form-input
          v-model="first_name"
          :state="isFirstNameValid"
          name="firstName"
      ></b-form-input>
    </b-input-group>

    <b-input-group class="mt-3">
      <template #prepend>
        <b-input-group-text>Имя</b-input-group-text>
      </template>
      <b-form-input
          v-model="last_name"
          :state="isLastNameValid"
          name="lastName"
      ></b-form-input>
    </b-input-group>

    <b-input-group class="mt-3">
      <template #prepend>
        <b-input-group-text>Отчество</b-input-group-text>
      </template>
      <b-form-input
          v-model="patronymic"
          :state="isPatronymicValid"
          name="patronymic"
      ></b-form-input>
    </b-input-group>

    <b-input-group class="mt-3">
      <template #prepend>
        <b-input-group-text>Город</b-input-group-text>
      </template>
      <b-form-input
          v-model="city"
          placeholder="Санкт-Петербург"
          name="city"
      ></b-form-input>
    </b-input-group>

    <b-input-group class="mt-3">
      <template #prepend>
        <b-input-group-text>Дата рождения</b-input-group-text>
      </template>
      <b-form-input
          :state="isDateValid"
          v-model="birth_date"
          type="date"
          name="age"
      ></b-form-input>
    </b-input-group>

    <b-input-group class="mt-3">
      <template #prepend>
        <b-input-group-text>Почта</b-input-group-text>
      </template>
      <b-form-input
          :state="isEmailValid"
          v-model="email"
          type="email"
          name="email"
          placeholder="email@example.com"
      ></b-form-input>
    </b-input-group>

    <b-input-group class="mt-3">
      <template #prepend>
        <b-input-group-text>Ссылка на социальные сети</b-input-group-text>
      </template>
      <b-form-input
          v-model="social_networks"
          name="socNetwork"
          type="url"
          placeholder="example.com/your_page"
      ></b-form-input>
    </b-input-group>

    <div class="form-group mt-3" id="photo-input">
      <label for="photo-input">Фотография</label>
      <b-form-file
          v-model="image"
          ref="file"
          id="file"
          type="file"
          placeholder="Выберите файл..."
          drop-placeholder="Перенесите файл сюда..."
      ></b-form-file>
    </div>

    <b-form-group
        class="mt-3 login-input"
        name="platform"
        label="Операционная система телефона:"
        v-slot="{ ariaDescribedby }">
      <b-form-radio v-model="platform" :aria-describedby="ariaDescribedby" name="ios" value="1">IOS</b-form-radio>
      <b-form-radio v-model="platform" :aria-describedby="ariaDescribedby" name="android" value="2">Android
      </b-form-radio>
    </b-form-group>

    <b-input-group class="mt-3">
      <template #prepend>
        <b-input-group-text>Пароль</b-input-group-text>
      </template>
      <b-form-input
          v-model="password"
          type="password"
      ></b-form-input>
    </b-input-group>

    <b-input-group class="mt-3">
      <template #prepend>
        <b-input-group-text>Еще раз</b-input-group-text>
      </template>
      <b-form-input
          :state="passwordState"
          v-model="inputPassword2"
          type="password"
          name="password"
      >
      </b-form-input>
      <b-form-invalid-feedback aria-live="polite" id="input-live-feedback">
        Пароли не совпадают
      </b-form-invalid-feedback>
    </b-input-group>

    <b-button @click="registerUser" :disabled="!isFormValid" class="mt-3  btn-dark">Зарегистрироваться</b-button>
  </b-container>
</template>

<script>
import {post} from "axios";
import {router} from "@/router";

export default {
  name: "Register",
  data() {
    return {
      email: null,
      password: null,
      inputPassword2: null,
      first_name: null,
      last_name: null,
      patronymic: null,
      birth_date: null,
      social_networks: null,
      platform: null,
      image: null,
      city: null
    }
  },
  methods: {
    registerUser: function () {
      var formData = new FormData();

      formData.append("email", this.email);
      formData.append("password", this.password);
      formData.append("first_name", this.first_name);
      formData.append("last_name", this.last_name);
      formData.append("patronymic", this.patronymic);
      formData.append("birth_date", this.birth_date);
      formData.append("social_networks", this.social_networks);
      formData.append("platform", this.platform);
      formData.append("photo", this.image);
      formData.append("city", this.city);

      post('http://127.0.0.1:8000/api/v1/users/registration/',formData).then(() => {
          this.$toast.info("Запрос на активацию аккаунта отправлен на почту")
          router.push("/account/login/")
      })
    },
  },
  computed: {

    passwordState() {
      if (this.inputPassword2 == null && this.password == null) {
        return null;
      }
      return this.inputPassword2 === this.password;
    },
    isFirstNameValid() {
      return this.first_name != null
    },
    isLastNameValid() {
      return this.last_name != null
    },
    isPatronymicValid() {
      return this.patronymic != null
    },
    isDateValid() {
      return this.birth_date != null
    },
    isEmailValid() {
      return this.email != null
    },
    isFormValid() {
      return this.password != null && this.first_name != null && this.last_name != null && this.patronymic != null && this.birth_date != null && this.email != null && this.inputPassword2 === this.password

    }
  },
}
</script>

<style scoped>
</style>