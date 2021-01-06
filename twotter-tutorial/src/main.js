/*
 * @Author: CC-TSR
 * @Date: 2020-12-28 16:07:36
 * @LastEditTime: 2021-01-06 11:38:01
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\twotter-tutorial\src\main.js
 * @可以输入预定的版权声明、个性签名、空行等
 */
import { createApp } from 'vue'
import App from './App.vue'

import ElementPlus from 'element-plus';
import 'element-plus/lib/theme-chalk/index.css';
import common from './assets/js/common'
import router from './router'
import store from './store'
import vAxios from 'v-axios';
// 不引入这个将自动注入axios
import axios from 'axios';

const app = createApp(App).use(store).use(router)
app.use(ElementPlus)
app.use(vAxios, axios);
app.config.globalProperties.common = common

app.mount('#app')
