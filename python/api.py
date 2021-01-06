'''
Author: CC-TSR
Date: 2021-01-04 21:13:10
LastEditTime: 2021-01-06 13:13:59
LastEditors: xiejiancheng1999@qq.com
Description: 
FilePath: \python\api.py
可以输入预定的版权声明、个性签名、空行等
'''
import random
import os
import json
from flask import Flask, request
from flask_cors import CORS

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
app = Flask(__name__)
app.debug = False
CORS(app, supports_credentials=True)


@app.route('/CreateTwoot', methods=['POST'])
def CreateTwoot():
    listAll = json.loads(GetTwoot())
    twoot = request.get_json()
    listAll.insert(0, twoot)
    with open('./twoots.json', 'w') as f:
        json.dump(listAll, f)
        return "200"


@app.route('/GetTwoot', methods=['GET'])
def GetTwoot():
    with open('./twoots.json', 'r') as f:
        data = json.load(f)
        return json.dumps(data, ensure_ascii=False, indent=4)


@app.route('/Login', methods=['Get', 'Post'])
def Login():
    user = request.get_json()
    print(user['name'])
    with open('./users.json', 'r', encoding='utf-8') as f:
        users = json.load(f)
        if(user["name"] in users.keys()):
            if(users[user["name"]]["password"] == user["password"]):
                del users[user["name"]]['password']
                users[user["name"]]['stateCode'] = 200
                print("验证成功")
                return json.dumps(users[user["name"]], ensure_ascii=False, indent=4)
        return json.dumps({'stateCode': "400"}, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    app.run(host='192.168.1.66', port=9999)
