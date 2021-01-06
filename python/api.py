'''
Author: CC-TSR
Date: 2021-01-04 21:13:10
LastEditTime: 2021-01-06 18:30:54
LastEditors: xiejiancheng1999@qq.com
Description: 
FilePath: \python\api.py
可以输入预定的版权声明、个性签名、空行等
'''
import random
import os
import json
from flask import Flask, request, url_for
from flask_cors import CORS

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
app = Flask(__name__)
app.debug = False
CORS(app, supports_credentials=True)
twootsUrl = "./twoots.json"


@app.route('/CreateTwoot', methods=['POST'])
def CreateTwoot():
    listAll = json.loads(GetTwoot())
    twoot = request.get_json()
    listAll.insert(0, twoot)
    with open(twootsUrl, 'w') as f:
        json.dump(listAll, f)
        return "200"


@app.route('/StarTwoot', methods=['Post'])
def StarTwoot():
    a = [{"a": 2}]
    with open(twootsUrl, 'w+', encoding='utf-8') as twootHandle:
        json.dump(a, twootHandle)

@app.route('/GetTwoot', methods=['GET'])
def GetTwoot():
    with open(twootsUrl, 'r') as f:
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


def star(twoot, twootId):
    if(twoot['id'] == twootId):
        if(twoot['isStar']):
            twoot['isStar'] = False
        else:
            twoot['isStar'] = True
    return twoot


@app.route('/assets')
def url_for_img():
    print(url_for('static', filename='cc_tsr.jpg'))


if __name__ == '__main__':
    app.run(host='192.168.1.113', port=9999)
