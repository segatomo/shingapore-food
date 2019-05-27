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
          <a class="nav-kink" href="/login">ログイン</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/logout">ログアウト</a>
        </li>
      </ul>
    </div>
  </nav>
  <div class="cocktailer-body">
    <form action="http://localhost:5000/api/login" method=post v-on:submit.prevent="onSubmit">

      <div class="form-group">
        <label for="InputTitle">ユーザ名</label>
        <!--<input type="text" class="form-control" id="InputTitle" name="username">-->
        <input　type="text" class="form-control" id="InputTitle" v-model="username">
      </div>
      <div class="form-group">
        <label for="InputPassword">パスワード</label>
        <!--<input type="password" class="form-control" id="InputPassword" name="password" >-->
        <input type="password" class="form-control" id="InputPassword" v-model="password" >
      </div>
      <button class="btn btn-primary" v-on:click="onSubmit">ログイン</button>
    </form>
  </div>
</div>
</template>

<script>
import ApiClient from './utils/ApiClient'
import axios from 'axios'
import Vue from 'vue'
import VueRouter from 'vue-router'
export default {
  name: 'LogIn',
  data () {
    return {
      name: ''
    }
  },
  //Formのsubmitイベントが発生したとき
  methods:{
  onSubmit:function(){
            //  axios.post('http://localhost:5000/api/login', {
              //          username:this.username,
            //            password:this.password}).then((response) => {
//
  //            if(reponse.data['accountinfo']==false){
    //            alert('ユーザー名またはパスワードが違います')
      //        }else{
        //          router.push('/mypage')
          //    }
          //    alert('username')
          //  ).catch(error => console.log(error.response))
            ApiClient.uploadaccount('/api/login', {'username':this.username,'password':this.password}, (response) => {
              console.log(response.data)
              if(response.data['accountinfo']==false){
                         alert('ユーザー名またはパスワードが違います')
                          }
                          else{
                              this.$router.push('/mypage')
                          }
            }, (error) => {
              console.error(error)
            })
//).then(response => {console.log(response.data)
  //HTTPリエストが失敗した
//}).catch(error => console.log(error.response))


              //ここでルートを/mypageに変える
  //},
  //onclick : function () {
    //ApiClient.uploadaccount('/api/login',this.username,this.password,(response) => {
      //console.log(response)
      //this.name = response.data.name
    //}, (error) => {
      //console.error(error)
    //})

}
  //}
}
}
</script>
<style></style>
