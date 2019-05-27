import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ChoosePictures from '@/components/ChoosePictures'
import TopPage from '@/components/TopPage'
import MyPage from '@/components/MyPage'
import LogIn from '@/components/LogIn'
Vue.use(Router)



export default new Router({
  routes: [
    {
      path: '/',
      name: 'TopPage',
      component: TopPage
    },
    {
      path: '/mypage',
      name: 'MyPage',
      component: MyPage
    },
    {
      path: '/choose-pictures',
      name: 'ChoosePictures',
      component: ChoosePictures
    },
    {
      path: '/login',
      name: 'LogIn',
      data:{username:'',password:''},
      component: LogIn
    }
  ]
})
