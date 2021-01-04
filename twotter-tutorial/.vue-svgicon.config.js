/*
 * @Author: CC-TSR
 * @Date: 2021-01-04 15:29:55
 * @LastEditTime: 2021-01-04 15:51:52
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\twotter-tutorial\.vue-svgicon.config.js
 * @可以输入预定的版权声明、个性签名、空行等
 */
const path = require('path')
const svgFilePaths = ["@/assets/icons/svg"].map((v) => path.resolve(v))
const tagName = 'icon'

module.exports = {
    tagName,
    svgFilePath: svgFilePaths,
    svgoConfig: {},
    pathAlias: {
    },
    transformAssetUrls: {},
}