/*
 * @Author: CC-TSR
 * @Date: 2021-01-04 10:52:42
 * @LastEditTime: 2021-01-04 11:13:33
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\twotter-tutorial\src\assets\js\common.js
 * @可以输入预定的版权声明、个性签名、空行等
 */
import { ElMessage } from 'element-plus'

export default {
    toast (str, type, showClose, onCloseFn) {
		let time = 1000
		if (showClose) {
			time = 3000
		}
		ElMessage({
			showClose: showClose,
			message: str,
			type: type,
			duration: time,
			onClose: onCloseFn
		})
	}
}