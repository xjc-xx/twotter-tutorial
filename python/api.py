'''
Author: CC-TSR
Date: 2021-01-04 21:13:10
LastEditTime: 2021-01-07 15:58:08
LastEditors: xiejiancheng1999@qq.com
Description: 
FilePath: \python\api.py
可以输入预定的版权声明、个性签名、空行等
'''
import random
import os
import json
from flask import Flask, request, flash, url_for
from flask_cors import CORS

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
app = Flask(__name__)
app.debug = False
app.secret_key = "super secret key"
CORS(app, supports_credentials=True)

twootsUrl = "./twoots.json"
userInfoUrl = './users.json'


def star(twoot, twootId):
    if(twoot['id'] == twootId):
        if(twoot['isStar']):
            twoot['isStar'] = False
        else:
            twoot['isStar'] = True
    return twoot


def addUser(userInfo):
    with open(userInfoUrl, 'r', encoding='utf-8') as f:
        users = json.load(f)
    userInfo['id'] = len(users) + 1
    if userInfo['username'] in users.keys():
        return '502'
    users[userInfo['username']] = userInfo
    with open(userInfoUrl, 'w', encoding='utf-8') as f:
        json.dump(users, f)
        return "200"


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
    twootIdDic = request.get_json()
    twootId = twootIdDic['id']
    with open(twootsUrl, 'r+') as twootHandle:
        print("-------------")
        twoots = json.load(twootHandle)
        for twoot in twoots:
            if(twoot['id'] == twootId):
                twoot['isStar'] = bool(1-twoot['isStar'])
                break
        twootHandle.seek(0)
        twootHandle.truncate()
        json.dump(twoots, twootHandle)
        return "200"


@app.route('/GetTwoot', methods=['GET'])
def GetTwoot():
    with open(twootsUrl, 'r') as f:
        data = json.load(f)
        return json.dumps(data, ensure_ascii=False, indent=4)


@app.route('/Login', methods=['Get', 'Post'])
def Login():
    user = request.get_json()
    print(user['name'])
    with open(userInfoUrl, 'r', encoding='utf-8') as f:
        users = json.load(f)
        if(user["name"] in users.keys()):
            if(users[user["name"]]["password"] == user["password"]):
                del users[user["name"]]['password']
                users[user["name"]]['stateCode'] = 200
                print("验证成功")
                return json.dumps(users[user["name"]], ensure_ascii=False, indent=4)
        return json.dumps({'stateCode': "400"}, ensure_ascii=False, indent=4)


@app.route('/Register', methods=['Post'])
def Register():
    try:
        inputUserInfo = request.form
        userInfo = inputUserInfo.get('user')
        try:
            userInfo = json.loads(userInfo)
        except:
            print("转换JSON失败")
            return '501'
        userInfo['twoots'] = ''
        userInfo['twoots_star'] = []
        del userInfo['state']
        userInfo["isAdmin"] = True
        if ('file' not in request.files):
            userInfo["userHeadImage"] = ''
        else:
            face = request.files.get('file')
            filename = userInfo["username"] + '.jpg'
            # inputUserInfo.get('imgName').split('.')[1]
            filePath = os.path.join('./static', filename)
            userInfo["userHeadImage"] = filePath
        print(userInfo)
        code = addUser(userInfo)
        if(code == "200"):
            print("用户注册成功")
            face.save(filePath)
        return code
    except:
        print("添加失败")
        return '500'


@app.route('/Upload', methods=['Post'])
def Upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if ('file' not in request.files):
            flash('No file part')
            return '400'
        file = request.files['file']
        flash('No file part')
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return '400'
        #if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            #file.save(os.path.join('./static', filename))
            return '200'
        return "400"


@app.route('/assets')
def url_for_img():
    print(url_for('static', filename='cc_tsr.jpg'))


if __name__ == '__main__':
    app.run(host='192.168.1.113', port=9999)
