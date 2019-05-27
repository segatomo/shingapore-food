<template>
<!--<title>Cocktail-selector</title>-->

<div>
  <!--built files will be auto injected -->
  <center>
  <p class = "title"> welcome to cocktailrecommender</p>
  <router-link to='/login' tag="button">ログイン画面へ</router-link>
</center>
</div>
</template>

<script>
import ApiClient from './utils/ApiClient'

export default {
  name: 'TopPage',
  data () {
    return {
      name: ''
    }
  },
  created: function () {
  }
}
</script>
<style></style>
