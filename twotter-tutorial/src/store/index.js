/*
 * @Author: CC-TSR
 * @Date: 2021-01-06 11:12:35
 * @LastEditTime: 2021-01-06 15:34:09
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\src\store\index.js
 * @可以输入预定的版权声明、个性签名、空行等
 */
import {
  createStore
} from 'vuex'

export default createStore({
  state: {
    user: !sessionStorage.getItem('userInfo') ? null : JSON.parse(sessionStorage.getItem('userInfo')),
  },
  mutations: {
    setUser(state, user) {
      state.user = user
    }
  },
  actions: {},
  modules: {}
})