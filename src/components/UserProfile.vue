<!--
 * @Author: CC-TSR
 * @Date: 2021-01-04 11:27:46
 * @LastEditTime: 2021-01-05 10:05:29
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\twotter-tutorial\src\components\UserProfile.vue
 * @可以输入预定的版权声明、个性签名、空行等
-->
<template>
  <div class="user-profile">
    <div class="user-profile__user-panel">
      <h1 class="user-profile__username">
        @{{ user.username }}-{{ fullName }}
      </h1>
      <div v-if="user.isAdmin" class="user-profile__admin-badge">admin</div>
      <div><strong id="followerCount">Followers: </strong>{{ followers }}</div>
      <form
        :class="[
          { '--exceed': newTwootCaracterCount > 180 },
          'user-profile__create-twoot-form',
        ]"
        @submit.prevent="publishTwoot"
      >
        <label for="newTwoot">
          <strong>New Twoot</strong>
          ({{ newTwootCaracterCount }} <em> /180</em>)
        </label>
        <textarea
          name="twootContent"
          id="newTwoot"
          cols="20"
          rows="4"
          placeholder="发表一些新鲜事..."
          maxlength="200"
          v-model="newTwootContent"
        ></textarea>

        <div class="user-profile__creat-twoot-type-div">
          <label for="newTwootType"><strong>Type: </strong></label>
          <select name="twootType" id="newTwootType" v-model="newTwootType">
            <option
              v-for="option in twootTypes"
              :key="option.id"
              :value="option.value"
            >
              {{ option.name }}
            </option>
          </select>
        </div>
        <input type="submit" id="submit" name="submit_button" value="提交" />
      </form>
    </div>
    <transition-group name="fade" tag="div" class="user-profile__twoots-wraper">
      <twoot-item
        v-for="twoot in user.twoots"
        :key="twoot.id"
        :username="user.username"
        :twoot="twoot"
        :isStar="user.twoots_star.indexOf(twoot.id) > -1"
        @event__star="toggleStar"
      />
    </transition-group>
  </div>
</template>

<script>
import { h } from "vue";
import TwootItem from "./TwootItem.vue";
import common from '../assets/js/common'

export default {
  name: "UserProfile",
  data() {
    return {
      newTwootContent: "",
      newTwootType: "instant",
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
      twootTypes: [
        {
          value: "draft",
          name: "Draft",
          id: 0,
        },
        {
          value: "instant",
          name: "instant",
          id: 1,
        },
      ],
    };
  },
  components: { TwootItem },
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
  computed: {
    fullName() {
      return ` ${this.user.lastName} ${this.user.firstName}`;
    },
    newTwootCaracterCount() {
      return this.newTwootContent.length;
    },
  },
  methods: {
    followUser() {
      this.followers++;
    },
    toggleStar(id) {
      console.log(this.user.twoots_star);
      this.user.twoots_star.indexOf(id) > -1
        ? this.user.twoots_star.splice(this.user.twoots_star.indexOf(id), 1)
        : this.user.twoots_star.push(id);
    },
    publishTwoot() {
      if (!this.newTwootContent) return;
      if(this.newTwootCaracterCount > 180){
          common.toast("字数太多了，恕我背不动",'warning')
          return
      }
      let newId = this.user.twoots.length + 1;
      let newTwoot = {
        id: newId,
        content: this.newTwootContent,
      };
      this.newTwootContent = "";
      this.user.twoots.unshift(newTwoot);
    },
  },
  mounted() {},
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
  padding: 50px 5%;
  height: 100vh;
  .user-profile__user-panel {
    display: flex;
    flex-direction: column;
    margin-right: 50px;
    padding: 20px;
    background-color: white;
    border-radius: 5px;
    border: 1px solid #0fe3e8;

    h1 {
      margin: 0 0 10px 0;
    }
    .user-profile__admin-badge {
      background-color: purple;
      color: white;
      border-radius: 5px;
      padding: 0 10px;
      margin-right: auto;
    }

    .user-profile__create-twoot-form {
      margin-top: 5px;
      padding-top: 20px;
      display: flex;
      flex-direction: column;
      &.--exceed {
        color: red;
        border-color: red;
        
        input {
            background-color: rgb(255, 23, 77);
            border: none;
            color: white;
        }
      }

      .user-profile__creat-twoot-type-div {
        margin-top: 20px;
      }

      #newTwootType {
        min-width: 100px;
        margin-left: 10px;
        margin-bottom: 20px;
      }
      #newTwootType:focus {
        outline: none;
      }
      textarea {
        resize: none;
        border: #2e3838 solid 1px;
        min-height: 28vh;
        margin-top: 5px;
      }
      textarea:focus {
        border: #22c5aa solid 1px;
        border-radius: 5px;
        outline: none;
      }
    }
  }
  .user-profile__twoots-wrapper {
    display: grid;
    grid-gap: 10px;
  }
}
</style>