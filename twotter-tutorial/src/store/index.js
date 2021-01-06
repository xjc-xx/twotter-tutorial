/*
 * @Author: CC-TSR
 * @Date: 2021-01-06 11:12:35
 * @LastEditTime: 2021-01-06 11:13:44
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\twotter-tutorial\src\store\index.js
 * @可以输入预定的版权声明、个性签名、空行等
 */
import { createStore } from 'vuex'

export default createStore({
  state: {
    user: null
  },
  mutations: {
    setUser(state,user){
      state.user = user
    }
  },
  actions: {
  },
  modules: {
  }
})
