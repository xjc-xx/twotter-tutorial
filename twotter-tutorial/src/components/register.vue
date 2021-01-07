<!--
 * @Author: CC-TSR
 * @Date: 2021-01-07 09:40:31
 * @LastEditTime: 2021-01-07 11:19:50
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
          :on-success="handleAvatarSuccess"
          :before-upload="beforeAvatarUpload"
          :show-file-list="false"
        >
          <img v-if="imageUrl" :src="imageUrl" class="avatar" alt="" />
          <em v-else class="el-icon-plus avatar-uploader-icon" />
        </el-upload>
      </el-form-item>
      <el-form-item class="dialog-footer" align="center">
        <el-button type="primary" @click="onSave('formData')">保 存</el-button>
        <el-button @click="onCancel('formData')">取 消</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>

<script>
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
      imageUrl: ''
    };
  },
  computed: {
    uploadUrl() {
      return `${this.$store.state.apiBaseUrl}Upload`;
    },
  },
  props: ["state"],
  components: {},
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
            this.reqFlag.add = false;
            let params = {
              username: this.formData.name,
              password: this.formData.password,
              email: "",
              firstName: "甲乙丙丁",
              lastName: "不知名的",
              state: this.state,
            };
            this.$http.post(url, params).then((res) => {
              if (res.code == 1) {
                this.$common.toast("添加成功", "success", false);
                this.$emit("addCallBack");
                this.onCancel(formData);
              }
              this.reqFlag.add = true;
            });
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
      this.$refs[formName].resetFields();
    },
    // 关闭弹出框
    closeDialog() {
      this.$refs["formData"].resetFields();
    },
    handleAvatarSuccess(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === "image/jpeg";
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.common.toast("上传头像图片只能是 JPG 格式!", "error");
      }
      if (!isLt2M) {
        this.common.toast("上传头像图片大小不能超过 2MB!", "error");
      }
      return isJPG && isLt2M;
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
