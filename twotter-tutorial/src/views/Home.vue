<!--
 * @Author: CC-TSR
 * @Date: 2021-01-05 18:27:33
 * @LastEditTime: 2021-01-06 11:18:37
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\twotter-tutorial\src\views\Home.vue
 * @可以输入预定的版权声明、个性签名、空行等
-->
<template>
  <div><h1>Home</h1></div>
</template>

<script>
import {useStore} from 'vuex'
export default {
  setup(props) {
    const store = useStore()
    if (!store.state.user) {
      
    }
  }
  
}
</script>

<style>
</style>