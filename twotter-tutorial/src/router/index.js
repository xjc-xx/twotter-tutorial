/*
 * @Author: CC-TSR
 * @Date: 2021-01-05 17:31:36
 * @LastEditTime: 2021-01-05 18:42:20
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\twotter-tutorial\src\router\index.js
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
    path: '/user/:userId',
    name: 'UserProfile',
    component: () => import('../views/UserProfile.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router