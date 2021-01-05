<template>
  <div class="login-container">
    <el-form class="login-main sub-center-center" :model="formData" :rules="formRules" ref="formData" label-position="left" label-width="0px">
      <h3 class="title">登录Twotter</h3>
      <el-form-item prop="name">
        <el-input type="text" v-model="formData.name" auto-complete="off" placeholder="账号"></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input type="password" v-model="formData.password" auto-complete="off" placeholder="密码"></el-input>
      </el-form-item>
      <el-form-item class="btn-box">
        <el-button type="primary" @click="submitLogin('formData')">登录</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { userLogin } from '@/config/interface'
export default {
  data () {
    const validate = (rule, value, callback) => {
      const reg = /^[0-9a-zA-Z]*$/g
      if (!value) {
        callback(new Error('请输入内容'))
      } else if (value.length < 3 || value.length > 15) {
        callback(new Error('内容长度需在 3 到 15 个字符'))
      } else if (!reg.test(value)) {
        callback(new Error('内容需为字母或数字'))
      } else {
        callback()
      }
    }
    return {
      formData: {
        name: null,
        password: null
      },
      formRules: {
        name: [
          { validator: validate, trigger: 'blur' }
        ],
        password: [
          { validator: validate, trigger: 'blur' }
        ]
      },
      reqFlag: {
        login: true
      },
      showFlag: {
        add: false
      }
    }
  },
  methods: {
    submitLogin (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          const url = userLogin
          if (this.reqFlag.login) {
            this.reqFlag.login = false
            let params = {
              name: this.formData.name,
              password: this.$md5(this.formData.password)
            }
            // 向后端发送请求
            this.$http(url, params)
            .then(res => {
              if (res.code == 1) {
                // 登录成功
                let data = res.data
                //  把该用户的数据保存到localStorage
                //  localStorage 和 sessionStorage 属性允许在浏览器中存储 key/value 对的数据。
                //  localStorage 用于长久保存整个网站的数据，保存的数据没有过期时间，直到手动去删除。
                localStorage.setItem('userInfo', JSON.stringify(data))
                //  调用action, 提交Mutations
                this.$store.dispatch('saveUserInfo', data)
                this.$common.toast('登陆成功', 'success', false)
                this.$router.push({
                  path: '/home/user',
                  query: {}
                })
              }
              this.reqFlag.login = true
            })
          }
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
      this.showFlag.add = true
      this.$nextTick(() => {
        this.$refs.add.init()
      })
    }
  }
}
</script>

<style scoped lang="scss">
.login-container{position: relative; width: 100vw; height: 100vh;background-image:url('../assets/images/login_bg.png'); background-size: cover; overflow: hidden;
  .login-main{ -webkit-border-radius: 5px; -moz-border-radius: 5px; border-radius: 5px; background-clip: padding-box; width: 350px; padding: 35px 35px 15px; background: #fff; border: 1px solid #eaeaea; box-shadow: 0 0 25px #cac6c6;
    h3{text-align: center;}
    .btn-box{text-align: center;}
  }
}
</style>
