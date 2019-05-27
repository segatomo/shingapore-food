<template>
<div>
  <center>
    <label class="pic">
      choose picture
      <input type="file" accept="image/*" id="files" name="picture_data" v-on:change="handleFileSelect($event)" style="display:none;" multiple />
    </label>
    <p class="choosed">
      <output id="list"></output>
    </p>
    <p>
      <input type="submit" value="投稿する" v-on:click="uploadData">
    </p>
  </center>
</div>
</template>

<script>
import ApiClient from './utils/ApiClient'

export default {
  name: 'HelloWorld',
  data () {
    return {
      targetFile: {},
      name: ''
    }
  },
  methods: {
    handleFileSelect: function (event) {
      console.log(event.target.files)

      this.targetFile = event.target.files[0]
    },
    uploadData: function () {
      console.log(this.targetFile)

      const targetPath = '/api/upload-pictures'
      ApiClient.uploadFile(targetPath, this.targetFile, {}, (response) => {
        console.log(response)
      }, (error) => {
        console.error(error)
      })
    }
  },
  created: function () {
  }
}
</script>

<style></style>
