<!--
 * @Author: CC-TSR
 * @Date: 2021-01-05 14:18:26
 * @LastEditTime: 2021-01-05 16:26:44
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\src\components\TheHeader.vue
 * @可以输入预定的版权声明、个性签名、空行等
-->
<template>
  <nav id="nav">
    <p class="logo">Twotter</p>
    <ul class="nav-links">
      <li class="links">
        <router-link to="/"> Home </router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
};
</script>

<style lang="scss" scoped>
#nav {
  display: flex;
  align-items: center;
  position: sticky;
  top: 0;
  box-sizing: border-box;
  height: 8vh;
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

    .links {
      padding-right: 20px;
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

    &.vue-school-active-class {
      color: #ab26ab;
    }
  }
}
</style>
