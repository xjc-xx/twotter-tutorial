/*
 * @Author: CC-TSR
 * @Date: 2021-01-05 10:22:06
 * @LastEditTime: 2021-01-07 12:25:37
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\vue.config.js
 * @可以输入预定的版权声明、个性签名、空行等
 */
module.exports = {
    css: {
        loaderOptions:{
            sass:{
                additionalData: '@import "@/styles/base.scss";'
            }
        }
    },
    productionSourceMap: false,
    configureWebpack: {
        devtool: undefined
    }
}