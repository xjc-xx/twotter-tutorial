<!--
 * @Author: CC-TSR
 * @Date: 2021-01-07 09:40:31
 * @LastEditTime: 2021-01-07 16:31:19
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\src\components\register.vue
 * @可以输入预定的版权声明、个性签名、空行等
-->
<template>
  <el-dialog
    title="新增账户"
    v-model="showFlag"
    custom-class="dialog-small"
    @close="closeDialog"
  >
    <el-form
      ref="formData"
      :model="formData"
      :rules="formRules"
      label-width="80px"
    >
      <el-form-item label="账号" prop="name">
        <el-input v-model="formData.name" placeholder="请输入用户名"></el-input>
        <div v-if="isUsed" class="el-form-item__error">
          此用户名已经被注册过了
        </div>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input
          v-model="formData.password"
          placeholder="请输入密码"
        ></el-input>
      </el-form-item>
      <el-form-item label="头像" prop="headImage">
        <el-upload
          class="avatar-uploader"
          :action="uploadUrl"
          :before-upload="beforeAvatarUpload"
          :limit="1"
          :show-file-list="false"
          :auto-upload="false"
          :on-exceed="handleExceed"
          :on-change="handleChange"
        >
          <img v-if="imageUrl" :src="imageUrl" class="avatar" alt="" />
          <em v-else class="el-icon-plus avatar-uploader-icon" />
        </el-upload>
      </el-form-item>
      <el-form-item class="dialog-footer" align="center">
        <el-button type="primary" @click="onSave('formData')">注册</el-button>
        <el-button @click="onCancel('formData')">取 消</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>

<script>
import { h } from "vue";
export default {
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
      showFlag: false,
      formData: {
        name: null,
        password: null,
      },
      formRules: {
        name: [{ validator: validate, trigger: "blur" }],
        password: [{ validator: validate, trigger: "blur" }],
      },
      reqFlag: {
        add: true,
      },
      file: [],
      isUsed: false,
    };
  },
  computed: {
    uploadUrl() {
      return `${this.$store.state.apiBaseUrl}Upload`;
    },
    imageUrl() {
      console.log(this.file);
      if (this.file[0]) {
        if (this.file[0].raw) return URL.createObjectURL(this.file[0].raw);
        return URL.createObjectURL(this.file[0]);
      }
      return "";
    },
  },
  props: ["state"],
  components: {},
  watch: {
    "formData.name": {
      handler: function () {
        this.isUsed = false;
      },
      deep: true,
    },
  },
  created() {},
  methods: {
    // 初始化
    init() {
      this.$nextTick(() => {
        this.changeShowFlag();
      });
    },
    changeShowFlag() {
      this.showFlag = !this.showFlag;
    },
    // 保存
    onSave(formData) {
      this.$refs[formData].validate((valid) => {
        if (valid) {
          const url = `${this.$store.state.apiBaseUrl}Register`;
          if (this.reqFlag.add) {
            if (this.file.length < 1) {
              this.common.toast("请提供您的头像", "warning");
              return;
            }
            this.reqFlag.add = false;
            let params = {
              username: this.formData.name,
              password: this.formData.password,
              email: "",
              firstName: "甲乙丙丁",
              lastName: "不知名的",
              state: this.state,
            };
            let fd = new FormData();
            if (this.file[0].raw) {
              fd.append("file", this.file[0].raw);
            } else {
              fd.append("file", this.file[0]);
            }

            fd.append("user", JSON.stringify(params));
            this.$http.post(url, fd).then(
              (res) => {
                this.file = [];
                console.log(res.data);
                if (res.data === 200) {
                  this.common.toast("注册成功", "success");
                  this.$emit("addCallBack", this.formData.name);
                  this.onCancel(formData);
                } else {
                  switch (res.data) {
                    case 500:
                      this.common.toast("后端发生未知错误", "error");
                      break;
                    case 501:
                      this.common.toast("后端类型转换时遇到错误", "error");
                      break;
                    case 502:
                      this.isUsed = true;
                      this.$notify({
                        title: "警告",
                        message: h(
                          "i",
                          { style: "color: orange" },
                          `${this.formData.name} 已经被注册过了`
                        ),
                      });
                      break;
                    default:
                      break;
                  }
                }
                this.reqFlag.add = true;
              },
              (err) => {
                this.file = [];
                this.common.toast("注册失败，网络异常", "error");
                console.log(err);
                this.reqFlag.add = true;
              }
            );
          }
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    // 取消
    onCancel(formName) {
      this.changeShowFlag();
      this.file = [];
      this.$refs[formName].resetFields();
    },
    // 关闭弹出框
    closeDialog() {
      this.$refs["formData"].resetFields();
      this.file = [];
    },
    handleChange(file, filelist) {
      this.file = filelist;
    },
    handleExceed(files, filelist) {
      this.file = files;
    },
    beforeAvatarUpload(file) {
      console.log(file.type);

      const isLt2M = file.size / 1024 / 1024 < 5;

      if (!isLt2M) {
        this.common.toast("上传头像图片大小不能超过 5MB!", "error");
      }

      return isLt2M;
    },
  },
};
</script>

<style lang="scss">
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 120px;
  height: 120px;
  line-height: 120px;
  text-align: center;
}
.avatar {
  width: 120px;
  height: 120px;
  display: block;
}
</style>
