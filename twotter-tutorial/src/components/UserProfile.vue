<!--
 * @Author: CC-TSR
 * @Date: 2021-01-04 11:27:46
 * @LastEditTime: 2021-01-04 18:11:44
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
      <form class="user-profile__create-twoot" @submit.prevent="publishTwoot">
        <label for="newTwoot"><strong>New Twoot</strong></label>
        <textarea
          name="twootContent"
          id="newTwoot"
          cols="20"
          rows="4"
          placeholder="发表一些新鲜事..."
          maxlength="150"
          v-model="newTwootContent"
        ></textarea>

        <div class="user-profile__creat-twoot-type">
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
    <div class="user-profile__twoots-wraper">
      <transition v-for="(twoot, index) in user.twoots" :key="twoot.id" name="fade">
        <twoot-item
          :key="index"
          :username="user.username"
          :twoot="twoot"
          :isStar="user.twoots_star.indexOf(twoot.id) > -1"
          @event__star="toggleStar"
        />
      </transition>
    </div>
  </div>
</template>

<script>
import { h } from "vue";
import TwootItem from "./TwootItem.vue";

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
      let newId = this.user.twoots.length + 1;
      let newTwoot = {
        id: newId,
        content: this.newTwootContent,
      };
      console.log(newTwoot);
      this.user.twoots.unshift(newTwoot);
    },
  },
  mounted() {},
};
</script>

<style scoped>
.user-profile {
  display: grid;
  grid-template-columns: 1fr 3fr;
  width: 100%;
  box-sizing: border-box;
  padding: 50px 5%;
}

.user-profile__user-panel {
  display: flex;
  flex-direction: column;
  margin-right: 50px;
  padding: 20px;
  background-color: white;
  border-radius: 5px;
  border: 1px solid #0fe3e8;
}

.user-profile__admin-badge {
  background-color: purple;
  color: white;
  border-radius: 5px;
  padding: 0 10px;
  margin-right: auto;
}

h1 {
  margin: 0 0 10px 0;
}
.user-profile__twoots-wrapper {
  display: grid;
  grid-gap: 10px;
}
.user-profile__create-twoot {
  margin-top: 5px;
  padding-top: 20px;
  display: flex;
  flex-direction: column;
}
.user-profile__creat-twoot-type {
  margin-top: 20px;
}
#newTwootType {
  min-width: 100px;
  margin-left: 10px;
}
#newTwootType:focus {
  outline: none;
}
textarea {
  resize: none;
  border: #2e3838 solid 1px;
}
textarea:focus {
  border: #22c5aa solid 1px;
  border-radius: 5px;
  outline: none;
}
</style>