<!--
 * @Author: CC-TSR
 * @Date: 2021-01-05 18:27:33
 * @LastEditTime: 2021-01-07 15:22:00
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\src\views\Login.vue
 * @可以输入预定的版权声明、个性签名、空行等
-->
<template>
  <div class="login-container">
    <el-form
      class="login-main sub-center-center"
      :model="formData"
      :rules="formRules"
      ref="formData"
      label-position="left"
      label-width="0px"
    >
      <h3 class="title">登录Twotter</h3>
      <el-form-item prop="name">
        <el-input
          type="text"
          v-model="formData.name"
          auto-complete="off"
          placeholder="用户名"
        ></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input
          type="password"
          v-model="formData.password"
          auto-complete="off"
          placeholder="密码"
        ></el-input>
      </el-form-item>
      <el-form-item class="btn-box">
        <el-button type="primary" @click="submitLogin('formData')"
          >登录</el-button
        >
        <el-button @click="regis('formData')">注册</el-button>
      </el-form-item>
    </el-form>
    <register
      v-if="showFlag.add"
      ref="add"
      state="个人注册"
      @addCallBack="callBackAdd"
    />
  </div>
</template>

<script>
import register from "@/components/register.vue";
export default {
  components: { register },
  data() {
    const validate = (rule, value, callback) => {
      const reg = /^\w{3,20}$/g;
      if (!value) {
        callback(new Error("请输入内容"));
      } else if (value.length < 3 || value.length > 15) {
        callback(new Error("内容长度需在 3 到 15 个字符"));
      } else if (!reg.test(value)) {
        callback(new Error("内容需为字母或数字或下划线"));
      } else {
        callback();
      }
    };
    return {
      formData: {
        name: null,
        password: null,
      },
      formRules: {
        name: [{ validator: validate, trigger: "blur" }],
        password: [{ validator: validate, trigger: "blur" }],
      },
      reqFlag: {
        login: true,
      },
      showFlag: {
        add: false,
      },
    };
  },
  methods: {
    submitLogin(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          const url = this.$store.state.apiBaseUrl;
          if (this.reqFlag.login) {
            this.reqFlag.login = false;
            let params = {
              name: this.formData.name,
              password: this.formData.password,
            };
            // 向后端发送请求
            this.$http.post(`${url}Login`, params).then(
              (res) => {
                if (res.data.stateCode == 200) {
                  // 登录成功
                  let data = res.data;
                  //  把该用户的数据保存到localStorage
                  //  localStorage 和 sessionStorage 属性允许在浏览器中存储 key/value 对的数据。
                  //  localStorage 用于长久保存整个网站的数据，保存的数据没有过期时间，直到手动去删除。
                  sessionStorage.setItem("userInfo", JSON.stringify(data));
                  //  调用action, 提交Mutations

                  this.$store.commit("setUser", data);
                  this.common.toast("登陆成功", "success");

                  this.$router.push("/");
                } else {
                  this.common.toast("用户名或密码错误", "error");
                }
                this.reqFlag.login = true;
              },
              (err) => {
                console.log(err);
                this.reqFlag.login = true;
              }
            );
          }
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    regis(formName) {
      this.$refs[formName].resetFields();
      this.showFlag.add = true;
      this.$nextTick(() => {
        this.$refs.add.init();
      });
    },
    callBackAdd(username){
      this.formData.name = username
    }
  },
};
</script>

<style scoped lang="scss">
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  width: 100vw;
  height: 100vh;
  background-image: url("../assets/images/login-bg.jpg");
  background-size: cover;
  overflow: hidden;
  .login-main {
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
    background-clip: padding-box;
    width: 350px;
    padding: 35px 35px 15px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
    h3 {
      text-align: center;
    }
    .btn-box {
      text-align: center;
    }
  }
}
</style>
