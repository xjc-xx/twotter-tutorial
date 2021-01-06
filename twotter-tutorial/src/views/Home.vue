<!--
 * @Author: CC-TSR
 * @Date: 2021-01-05 18:27:33
 * @LastEditTime: 2021-01-06 11:21:24
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\twotter-tutorial\src\views\Home.vue
 * @可以输入预定的版权声明、个性签名、空行等
-->
<template>
  <div><h1>Home</h1></div>
</template>

<script>
import { useRouter } from 'vue-router'
import {useStore} from 'vuex'
export default {
  setup() {
    const store = useStore()
    const router = useRouter()
    if (!store.state.user) {
      router.push("/login")
    }
  }
  
}
</script>

<style>
</style>