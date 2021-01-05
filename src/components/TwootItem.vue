<!--
 * @Author: CC-TSR
 * @Date: 2021-01-04 14:34:11
 * @LastEditTime: 2021-01-05 17:27:30
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\src\components\TwootItem.vue
 * @可以输入预定的版权声明、个性签名、空行等
-->
<template>
  <div class="twoot-item" @click="star(twoot.id)" :key="twoot.id">
    <div class="user-profile__twoot">
      <div class="twoot-item__user">@{{ username }}</div>
      <div class="twoot-item__content">
        {{ twoot.content }}
        <em :class="['nomal-em', { em_isLike: !isStar }]">like this? <img class="Icon" src="../assets/icons/svg/love.svg" alt="" /></em
        >
        <transition name="fade">
          <img
            class="likeIcon Icon"
            v-show="isStar"
            src="../assets/icons/svg/like.svg"
            alt=""
          />
        </transition>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TwootItem",
  setup(props, ctx) {
    function star(id) {
      ctx.emit("event__star", id);
    }
    return {
      star,
    };
  },
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
  box-shadow: 2px 2px 2px 2px #203e3f;
  cursor: pointer;
  transition: all 0.8s ease;
  margin: 0 20px 10px 0;
  position: relative;
  &:hover {
    transform: scale(1.1, 1.1);
    .em_isLike {
      opacity: 1 !important;
    }
  }

  .twoot-item__user {
    font-weight: bold;
    margin-bottom: 5px;
  }

  .twoot-item__content {
    display: flex;
    justify-content: space-between;
    padding: 0 15px;
    .nomal-em {
      opacity: 0;
      color: rgb(236, 58, 161);
      &.em_isLike {
        transition: opacity 1.5s ease;
        opacity: 0;
      }
    }
    .Icon {
      max-height: 15px;
    }
    .likeIcon {
      position: absolute;
      right: 20px;
      bottom: 15px;
    }
  }
}
</style>