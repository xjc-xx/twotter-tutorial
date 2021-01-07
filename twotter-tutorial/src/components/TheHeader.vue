<!--
 * @Author: CC-TSR
 * @Date: 2021-01-05 14:18:26
 * @LastEditTime: 2021-01-07 17:27:04
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\src\components\TheHeader.vue
 * @可以输入预定的版权声明、个性签名、空行等
-->
<template>
  <nav id="nav">
    <router-link
      :to="{
        name: 'UserInfo',
      }"
      ><p class="logo">Twotter</p></router-link
    >
    <ul class="nav-links">
      <li class="links">
        <router-link to="/"> Home </router-link>
      </li>
      <li class="links">
        <router-link to="/info"> User </router-link>
      </li>
      <li class="links">
        <router-link to="/covid"> Covid-Map </router-link>
      </li>
      <li class="links">
        <a @click="logout"> Sign Out </a>
      </li>
      <li class="links"></li>
    </ul>
    <div
      class="links"
      style="color: #ba78fc; margin-left: auto; font-size: 3vh; cursor: pointer"
    >
      {{ username }}
    </div>
  </nav>
</template>

<script>
import { h } from "vue";
export default {
  computed: {
    username() {
      return `${this.$store.state.user.firstName} ${this.$store.state.user.lastName}`;
    },
  },
  methods: {
    logout() {
      this.$notify({
        title: "提示",
        message: h(
          "i",
          { style: "color: red" },
          `${this.username} 已经退出了登录`
        ),
      });
      sessionStorage.clear();
      this.$router.push({ name: "Login" });
    },
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
  background-color: white;
  z-index: 999;
  box-shadow: 0 2px 5px #2c3e50;
  border-bottom: 1px solid grey;
  .logo {
    margin-left: 2vw;
    font-size: 25px;
    padding: 0.5vw 1vw;
    color: purple;
    border-radius: 10px;
    text-align: center;
    font-weight: bold;
    &:hover {
      box-shadow: 2px 2px 2px #2c3e50;
    }
  }

  .nav-links {
    display: flex;
    margin-left: 3vw;
    .links {
      margin: auto 10px;
      padding: 10px;
      min-width: 8vw;
      box-sizing: border-box;
      list-style: none;
      border-radius: 4vw;
      text-align: center;
      &:hover {
        background-color: #e7e9eb;
        color: #ce73ce;
        box-shadow: 2px 2px 2px #2c3e50;
      }
    }
  }
  a {
    color: #2c3e50;
    text-decoration: none;
    font-weight: bold;
    font-size: 3vh;
    cursor: pointer;
    &.router-link-active {
      color: #cf16cf;
    }
  }
}
</style>
