'''
Author: CC-TSR
Date: 2021-01-04 21:13:10
LastEditTime: 2021-01-07 11:51:04
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
from werkzeug.utils import secure_filename

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
app = Flask(__name__)
app.debug = False
app.secret_key = "super secret key"
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


@app.route('/Register', methods=['Post'])
def Register():
    inputUserInfo = request.get_json()
    inputUserInfo["isAdmin"] = True
    print(inputUserInfo)
    return ""


@app.route('/Upload', methods=['Post'])
def Upload():

    if request.method == 'POST':
        # check if the post request has the file part
        if ('file' not in request.files):
            print(" 大苏打")
            flash('No file part')
            return '400'
        file = request.files['file']
        flash('No file part')
        print(file.filename)
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return '400'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return '200'
        return "400"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ['.jpg']


@app.route('/assets')
def url_for_img():
    print(url_for('static', filename='cc_tsr.jpg'))


if __name__ == '__main__':
    app.run(host='192.168.1.113', port=9999)
