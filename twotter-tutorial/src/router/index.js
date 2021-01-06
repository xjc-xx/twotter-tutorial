/*
 * @Author: CC-TSR
 * @Date: 2021-01-05 17:31:36
 * @LastEditTime: 2021-01-06 14:53:32
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\src\router\index.js
 * @可以输入预定的版权声明、个性签名、空行等
 */
import {
  createRouter,
  createWebHistory
} from 'vue-router'
import UserProfile from '../views/UserProfile.vue'
import store from '../store'

const routes = [
  {
    path: '/',
    name: 'UserProfile',
    component: UserProfile,
  },
  {
    path: '/info',
    name: 'UserInfo',
    component: ()=>import("../views/UserInfo.vue"),
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  console.log(store)
  if (to.name !== 'Login' && !store.state.user) next({
    name: 'Login'
  })
  else next()
});


export default router