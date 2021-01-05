<!--
 * @Author: CC-TSR
 * @Date: 2021-01-05 14:18:26
 * @LastEditTime: 2021-01-05 21:13:56
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\twotter-tutorial\src\components\TheHeader.vue
 * @可以输入预定的版权声明、个性签名、空行等
-->
<template>
  <nav id="nav">
    <router-link
      :to="{
        name: 'Home'
      }"
      ><p class="logo">Twotter</p></router-link
    >
    <ul class="nav-links">
      <li class="links">
        <router-link to="/"> Home </router-link>
      </li>
      <li class="links">
        <router-link to="/user/0"> User </router-link>
      </li>
      <li class="links">
        <router-link to="/login"> Login </router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
import { useRoute } from "vue-router";
export default {
  setup() {
    const router = new useRoute();
    return {
      router,
    };
  },
};
</script>

<style lang="scss" scoped>
#nav {
  display: flex;
  align-items: center;
  position: sticky;
  top: 0;
  box-sizing: border-box;
  height: 7vh;
  box-shadow: 0 2px 5px #2c3e50;
  background-color: #57e6ce;
  border-bottom: 1px solid grey;
  z-index: 2;
  .logo {
    padding-left: 2vw;
    font-size: 25px;
    color: purple;
    font-weight: bold;
  }

  .nav-links {
    display: flex;
    margin-left: 60px;
    .links {
      padding-right: 30px;
      list-style: none;
      &:hover {
        text-decoration: underline;
      }
    }
  }
  a {
    color: #2c3e50;
    text-decoration: none;
    font-weight: bold;
    font-size: 3vh;
    &.router-link-active {
      color: #cf16cf;
    }
  }
}
</style>
