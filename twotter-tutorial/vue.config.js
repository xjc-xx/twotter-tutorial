/*
 * @Author: CC-TSR
 * @Date: 2021-01-05 10:22:06
 * @LastEditTime: 2021-01-07 17:58:45
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\vue.config.js
 * @可以输入预定的版权声明、个性签名、空行等
 */
module.exports = {
    css: {
        loaderOptions: {
            sass: {
                additionalData: '@import "@/styles/base.scss";'
            }
        }
    },
    productionSourceMap: false,
    configureWebpack: {
        devtool: undefined
    },
    transpileDependencies: [
        'vue-echarts',
        'resize-detector'
    ],
    devServer: {
        proxy: {
            "/api": {
                target: "https://www.ncovchina.com/data",
                changeOrigin: true,
                pathRewrite: {
                    "^/api": ""
                }
            },
            "/aki": {
                target: "http://api.aifanyi.net/google.php",
                changeOrigin: true,
                pathRewrite: {
                    "^/aki": ""
                }
            }
        },
        host: "0.0.0.0",
        port: 8083,
        clientLogLevel: "info"
    }
}