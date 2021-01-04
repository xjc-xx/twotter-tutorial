<!--
 * @Author: CC-TSR
 * @Date: 2021-01-04 14:34:11
 * @LastEditTime: 2021-01-04 18:04:05
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\twotter-tutorial\src\components\TwootItem.vue
 * @可以输入预定的版权声明、个性签名、空行等
-->
<template>

  <div class="twoot-item" @click="star(twoot.id)" :key="twoot.id">
    <div class="user-profile__twoot">
      <div class="twoot-item__user">@{{ username }}</div>
      <div class="twoot-item__content">
        {{ twoot.content }}
        <img
          class="likeIcon"
          v-if="isStar"
          src="../assets/icons/svg/love.svg"
          alt=""
          srcset=""
        />
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: "TwootItem",
  props: {
    username: {
      type: String,
      required: true,
    },
    twoot: {
      type: Object,
      required: true,
    },
    isStar: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  methods: {
    star(id) {
      this.$emit("event__star", id);
    },
  },
};
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 2s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
.twoot-item {
  padding: 15px;
  background: white;
  border-radius: 5px;
  border: 1px solid #203e3f;
  box-sizing: border-box;
  cursor: pointer;
  
  margin: 0 20px 10px 0;
  position: relative;
}

.twoot-item__user {
  font-weight: bold;
  margin-bottom: 5px;
}
.likeIcon {
  max-height: 15px;
  position: absolute;
  right: 20px;
}
</style>