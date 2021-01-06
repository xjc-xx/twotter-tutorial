<!--
 * @Author: CC-TSR
 * @Date: 2021-01-05 10:54:51
 * @LastEditTime: 2021-01-06 17:12:10
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\src\components\CreateTwootPanel.vue
 * @可以输入预定的版权声明、个性签名、空行等
-->
<template>
  <form
    :class="[
      { '--exceed': newTwootCaracterCount > 120 },
      'create-twoot-form',
    ]"
    @submit.prevent="publishTwoot"
  >
    <label for="newTwoot">
      <strong>New Twoot</strong>
      ({{ newTwootCaracterCount }} <em> /120</em>)
    </label>
    <textarea
      name="twootContent"
      id="newTwoot"
      cols="20"
      rows="4"
      placeholder="发表一些新鲜事..."
      maxlength="150"
      v-model="state.newTwootContent"
    ></textarea>

    <div class="submit-panel">
      <div class="creat-twoot-type-div">
        <label for="newTwootType"><strong>Type: </strong></label>
        <select name="twootType" id="newTwootType" v-model="state.newTwootType">
          <option
            v-for="option in state.twootTypes"
            :key="option.id"
            :value="option.value"
          >
            {{ option.name }}
          </option>
        </select>
      </div>

      <input type="submit" id="submit" name="submit_button" value="Twoot It!" />
    </div>
  </form>
</template>

<script>
import { reactive, computed } from "vue";
export default {
  name: "CreateTwootPanel",
  setup(paops, ctx) {
    const state = reactive({
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
      newTwootContent: "",
      newTwootType: "instant",
    });

    const newTwootCaracterCount = computed(() => state.newTwootContent.length);
    const twoot = computed(() => {
      return {
        content: state.newTwootContent,
        caracterCount: newTwootCaracterCount,
        type: state.newTwootType,
      };
    });

    function publishTwoot() {
      if (!state.newTwootContent) return;
      if (state.newTwootContent > 120) {
        ctx.common.toast("字数太多了，恕我背不动", "warning");
        return;
      }
      ctx.emit("publish", twoot);
      state.newTwootContent = "";
    }

    return {
      state,
      newTwootCaracterCount,
      publishTwoot,
    };
  },
};
</script>

<style lang="scss" scoped>
.create-twoot-form {
  margin-top: 20px;
  padding: 20px 0;
  display: flex;
  flex-direction: column;
  &.--exceed {
    color: red;
    border-color: red;

    input {
      background-color: rgb(255, 23, 77) !important;
      border: none !important;
      color: white !important;
    }
  }

  textarea {
    resize: none;
    border: #2e3838 solid 1px;
    min-height: 15vh;
    margin-top: 5px;
    &:focus {
      border: #22c5aa solid 1px;
      border-radius: 5px;
      outline: none;
    }
  }

  .submit-panel {
    display: flex;
    justify-content: space-between;

    .creat-twoot-type-div {
      margin-top: 20px;

      #newTwootType {
        min-width: 100px;
        margin-left: 10px;
        margin-bottom: 20px;
        &:focus {
          outline: none;
        }
      }
    }

    #submit {
      padding: 5px 20px;
      margin: auto 0;
      border-radius: 5px;
      background-color: #57e6ce;
      color: rgba(43, 51, 51, 0.842);
      font-weight: bold;
      border: none;
      box-shadow: none;
      transition: all 0.8s ease;
      &:hover {
        box-shadow: 2px 2px 2px #203e3f;
        cursor: pointer;
      }
    }
  }
}
</style>