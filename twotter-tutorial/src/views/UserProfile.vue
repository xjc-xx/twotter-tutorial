<!--
 * @Author: CC-TSR
 * @Date: 2021-01-04 11:27:46
 * @LastEditTime: 2021-01-07 17:11:43
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\src\views\UserProfile.vue
 * @可以输入预定的版权声明、个性签名、空行等
-->
<template>
  <div>
    <Header />
    <div class="user-profile">
      <div class="user-profile-sidebar">
        <div class="user-profile__user-panel">
          <h1 class="user-profile__username">
            @ {{ state.user.username }}
            <div class="head_img">
              <img
                class="head-image"
                :src="state.baseUrl + state.user.userHeadImage"
                alt=""
              />
            </div>
          </h1>
          <div v-if="state.user.isAdmin" class="user-profile__admin-badge">
            admin
          </div>
          <div>
            <strong id="followerCount">Followers: </strong>{{ state.followers }}
          </div>
        </div>
        <create-twoot-panel @publish="publishTwoot" />
      </div>
      <transition-group
        name="fade"
        tag="div"
        class="user-profile__twoots-wraper"
      >
        <twoot-item
          v-for="twoot in state.Alltwoots"
          :key="twoot.id"
          :username="twoot.username"
          :faceUrl="state.user.userHeadImage"
          :twoot="twoot"
          :isStar="twoot.isStar"
          @event__star="toggleStar"
        />
      </transition-group>
    </div>
  </div>
</template>

<script>
import { h } from "vue";
import TwootItem from "@/components/TwootItem.vue";
import CreateTwootPanel from "@/components/CreateTwootPanel.vue";
import { reactive, getCurrentInstance } from "vue";
import Header from "@/components/TheHeader";
import { useStore } from "vuex";
import axios from "axios";

export default {
  name: "UserProfile",
  setup() {
    const store = useStore();
    const { ctx } = getCurrentInstance();
    // if(userId) fetchUserFormApi(userId)
    const state = reactive({
      isLoading: false,
      followers: 0,
      user: store.state.user,
      Alltwoots: [],
      baseUrl: store.state.apiBaseUrl,
    });

    function getAllTwoots() {
      axios.get(`${state.baseUrl}GetTwoot`).then((res) => {
        state.Alltwoots = res.data;
      });
    }
    var handleGetTwoots = setInterval(getAllTwoots, 500);

    function followUser() {
      state.followers++;
    }

    function toggleStar(id) {
      clearInterval(handleGetTwoots);
      axios.post(`${state.baseUrl}StarTwoot`, { id: id }).then(
        (res) => {
          console.log(res.data);
          if (res.data == "200") {
            console.log("点赞");
            handleGetTwoots = setInterval(getAllTwoots, 100);
          }
        },
        (err) => {
          console.log(err);
        }
      );
    }

    function publishTwoot(twoot) {
      let newId = state.Alltwoots.length + 1;
      let newTwoot = {
        id: newId,
        content: twoot.value.content,
        username: store.state.user.username,
        isStar: false,
      };
      gotoTop();
      // state.user.twoots.unshift(newTwoot);
      axios.post(`${state.baseUrl}CreateTwoot`, newTwoot).then((res) => {
        if (res.data == "200") {
          ctx.common.toast("发表成功", "success");
        }
      });
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

  components: { TwootItem, CreateTwootPanel, Header },

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
  },
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
   
    max-height: 50vh;
    .user-profile__user-panel {
      display: flex;
      flex-direction: column;
      padding: 2vw;
      border-radius: 2vw;
      border: 1px solid #57e6ce;
      transition: all 0.5s ease;
      box-shadow: 2px 2px 2px #095a4c;
      border-radius: 2vw;
      &:hover {
        transform: scale(1.1, 1.1);
      }
      h1 {
        margin: 0 0 10px 0;
        display: flex;
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