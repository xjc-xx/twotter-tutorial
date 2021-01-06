/*
 * @Author: CC-TSR
 * @Date: 2021-01-05 17:31:36
 * @LastEditTime: 2021-01-06 12:52:13
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\src\router\index.js
 * @可以输入预定的版权声明、个性签名、空行等
 */
import {
  createRouter,
  createWebHistory
} from 'vue-router'
import Home from '../views/Home.vue'

const routes = [{
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/user',
    name: 'UserProfile',
    component: () => import('../views/UserProfile.vue')
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

export default router