<!--
 * @Author: CC-TSR
 * @Date: 2020-12-28 16:07:36
 * @LastEditTime: 2021-01-04 16:07:06
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\twotter-tutorial\src\App.vue
 * @可以输入预定的版权声明、个性签名、空行等
-->
<template>
  <div id="app">
    <UserProfile/>
  </div>
</template>

<script>
import UserProfile from '@/components/UserProfile'
export default {
  components: {
    UserProfile
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  min-height: 100vh;
  background-color: #F3F5FA;
}
.twoot-item__content{
  padding: 0 15px;
}
</style>
