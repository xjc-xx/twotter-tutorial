<!--
 * @Author: CC-TSR
 * @Date: 2021-01-04 11:27:46
 * @LastEditTime: 2021-01-05 16:44:52
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\src\components\UserProfile.vue
 * @可以输入预定的版权声明、个性签名、空行等
-->
<template>
  <div class="user-profile">
    <div class="user-profile-sidebar">
      <div class="user-profile__user-panel">
        <h1 class="user-profile__username">@ {{ state.user.username }}</h1>
        <div v-if="state.user.isAdmin" class="user-profile__admin-badge">
          admin
        </div>
        <div>
          <strong id="followerCount">Followers: </strong>{{ state.followers }}
        </div>
      </div>
      <create-twoot-panel @publish="publishTwoot" />
    </div>
    <transition-group name="fade" tag="div" class="user-profile__twoots-wraper">
      <twoot-item
        v-for="twoot in state.user.twoots"
        :key="twoot.id"
        :username="state.user.username"
        :twoot="twoot"
        :isStar="state.user.twoots_star.indexOf(twoot.id) > -1"
        @event__star="toggleStar"
      />
    </transition-group>
  </div>
</template>

<script>

import { h } from "vue";
import TwootItem from "./TwootItem.vue";
import CreateTwootPanel from "./CreateTwootPanel.vue";
import { reactive } from "vue";

export default {
  name: "UserProfile",
  setup() {
    const state = reactive({
      isLoading: false,
      followers: 0,
      user: {
        id: 1,
        username: "cc_tsr",
        firstName: "渐成",
        lastName: "谢",
        email: "xiejiancheng1999@qq.com",
        isAdmin: true,
        twoots: [
          { id: 1, content: "Twotter is Amazing" },
          { id: 2, content: "Vue is Awaresome" },
        ],
        twoots_star: [],
      },
    });

    function followUser() {
      state.followers++;
    }
    function toggleStar(id) {
      state.user.twoots_star.indexOf(id) > -1
        ? state.user.twoots_star.splice(state.user.twoots_star.indexOf(id), 1)
        : state.user.twoots_star.push(id);
    }
    function publishTwoot(twoot) {
      let newId = state.user.twoots.length + 1;
      let newTwoot = {
        id: newId,
        content: twoot.value.content,
      };
      gotoTop();
      state.user.twoots.unshift(newTwoot);
    }
    function gotoTop() {
      let top = document.documentElement.scrollTop;

      // 实现滚动效果

      const timeTop = setInterval(() => {
        document.documentElement.scrollTop = top -= 15;

        if (top <= 0) {
          clearInterval(timeTop); //清除定时器
        }
      }, 10);
    }
    return {
      state,
      followUser,
      toggleStar,
      publishTwoot,
    };
  },

  components: { TwootItem, CreateTwootPanel },
  
  watch: {
    followers(newFollowerCount, oldFollowerCount) {
      oldFollowerCount < newFollowerCount
        ? this.$notify({
            title: "提示",
            message: h(
              "i",
              { style: "color: teal" },
              `${this.user.username} has gained a follower`
            ),
          })
        : this.$notify({
            title: "提示",
            message: h(
              "i",
              { style: "color: pink" },
              `${this.user.username} has losed a follower`
            ),
          });
    },
  }
};
</script>

<style lang='scss' scoped>
.fade-leave-active {
  position: absolute;
}
.fade-leave-to,
.fade-enter-from {
  opacity: 0;
  transform: translateX(60px);
}

.user-profile {
  display: grid;
  grid-template-columns: 1fr 3fr;
  width: 100%;
  box-sizing: border-box;
  padding: 5vh 5%;
  min-height: 92vh;
  .user-profile-sidebar {
    display: flex;
    flex-direction: column;
    position: sticky;
    top: 15vh;
    box-sizing: border-box;
    z-index: 1;
    max-height: 50vh;
    .user-profile__user-panel {
      display: flex;
      flex-direction: column;
      padding: 20px;
      background-color: white;
      border-radius: 5px;
      border: 1px solid #57e6ce;
      h1 {
        margin: 0 0 10px 0;
      }
      .user-profile__admin-badge {
        background-color: purple;
        color: white;
        border-radius: 5px;
        padding: 0 10px;
        margin-right: auto;
        font-weight: bold;
      }
    }
  }
  .user-profile__twoots-wraper {
    display: grid;
    grid-gap: 10px;
    margin-bottom: auto;
    margin-left: 5vw;
  }
}
</style>