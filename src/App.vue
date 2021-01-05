<!--
 * @Author: CC-TSR
 * @Date: 2020-12-28 16:07:36
 * @LastEditTime: 2021-01-05 14:20:43
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\src\App.vue
 * @可以输入预定的版权声明、个性签名、空行等
-->
<template>
  <div id="app">
    <the-header />
    <UserProfile />
  </div>
</template>

<script>
import UserProfile from "@/components/UserProfile";
import TheHeader from './components/TheHeader.vue';
export default {
  components: {
    UserProfile,
    TheHeader
  },
};
</script>

<style lang='scss'>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  min-height: 100vh;
  background-color: #f3f5fa;
}
</style>
