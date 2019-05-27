<template>
<!--<title>Cocktail-selector</title>-->

<div class="container">
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="/">cocktailer</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav"
      aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="nav navbar-nav navbar-right">
        <li class="nav-item">
          <input class="nav-link" type="file" accept="image/*" id="files" name="picture_data" v-on:change="handleFileSelect($event)" style="display:none;" multiple>投稿する</a>
        </li>
        <li class="nav-item">
          <a class="nav-kink" href="/login">ログイン</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/logout">ログアウト</a>
        </li>
      </ul>
    </div>
  </nav>
  <div class="cocktailer-body">
    投稿がありません
  </div>
</div>
</template>

<script>
import ApiClient from './utils/ApiClient'

export default {
  name: 'MyPage',
  data () {
    return {
      targetFile:{},
      name: ''
    }
  },
  methods: {
    handleFileSelect: function (event) {
      console.log(event.target.files)

      this.targetFile = event.target.files[0]
    //},
    //uploadData: function () {
      console.log(this.targetFile)

      const targetPath = '/api/upload-pictures'
      ApiClient.uploadFile(targetPath, this.targetFile, {}, (response) => {
        console.log(response)
      }, (error) => {
        console.error(error)
      })
    }

  }
}
</script>
<style></style>
