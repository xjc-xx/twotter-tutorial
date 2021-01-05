/*
 * @Author: CC-TSR
 * @Date: 2021-01-05 18:27:33
 * @LastEditTime: 2021-01-05 20:30:00
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\twotter-tutorial\src\assets\users.js
 * @可以输入预定的版权声明、个性签名、空行等
 */
const users = {
    "1": {
        "id": 1,
        "username": "cc_tsr",
        "firstName": "渐成",
        "lastName": "谢",
        "email": "xiejiancheng1999@qq.com",
        "isAdmin": true,
        "twoots": [{
                "id": 1,
                "content": "Twotter is Amazing"
            },
            {
                "id": 2,
                "content": "Vue is Awaresome"
            }
        ],
        "twoots_star": []
    },
    "2": {
        "id": 2,
        "username": "Vue3_Robot",
        "firstName": "腌",
        "lastName": "萝卜",
        "email": null,
        "isAdmin": false,
        "twoots": null,
        "twoots_star": []
    }
}
export default users