<!--
 * @Author: CC-TSR
 * @Date: 2021-01-04 14:34:11
 * @LastEditTime: 2021-01-05 09:35:37
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
        <transition name="fade">
          <img
            class="likeIcon"
            v-if="isStar"
            src="../assets/icons/svg/love.svg"
            alt=""
            srcset=""
          />
        </transition>
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

<style lang='scss' scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.8s;
}
.fade-enter-from, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
.twoot-item {
  padding: 15px;
  background: white;
  border-radius: 5px;
  border: 1px solid #203e3f;
  box-sizing: border-box;
  cursor: pointer;
  transition: all 0.8s ease;
  margin: 0 20px 10px 0;
  position: relative;
  &:hover {
    transform: scale(1.1, 1.1);
  }

  .twoot-item__user {
    font-weight: bold;
    margin-bottom: 5px;
  }

  .twoot-item__content {
    padding: 0 15px;

    .likeIcon {
      max-height: 15px;
      position: absolute;
      right: 20px;
      bottom: 15px;
    }
  }
}
</style>