# coding: utf-8
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,flash
import numpy as np
import cv2
from models.image_process import canny, image_classify, rec_alcohol
from datetime import datetime
import os
import string
import random

SAVE_DIR = "./images"
if not os.path.isdir(SAVE_DIR):
    os.mkdir(SAVE_DIR)

app = Flask(__name__, static_url_path="")

@app.route('/toppage')
def index1_toppage():
    return render_template('toppage.html')

@app.route('/login')
def index2_toppage():
    return render_template('login.html')

@app.route('/')
def index():
    # return render_template('index.html', images=os.listdir(SAVE_DIR)[::-1])
    return render_template('index.html', images=os.listdir("app/images")[::-1])

@app.route('/images/<path:path>', methods=['GET'])
def send_js(path):
    print(path)
    return send_from_directory(SAVE_DIR, path)

# 参考: https://qiita.com/yuuuu3/items/6e4206fdc8c83747544b
@app.route('/upload', methods=['POST'])
def upload():
    if request.files['image']:
        # 画像として読み込み
        stream = request.files['image'].stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)

        # 保存
        dt_now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_")
        save_path = os.path.join("app/images", dt_now + ".png")
        print(save_path)
        classify_path = os.path.join("/images", dt_now + ".png")
        cv2.imwrite(save_path, img)
        
        food = image_classify(classify_path)['food']
        score = float(image_classify(classify_path)['score'])*100
        # path = dt_now + ".png"
        alcohol = rec_alcohol(food)
        print("save", save_path)

        return render_template('result.html',food=food, score=round(score,2), path=classify_path, alcohol=alcohol)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        if request.form['username']!=app.config['USERNAME']:
            flash('ユーザー名が異なります')
        elif request.form['password']!=app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            return redirect('/toppage')
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
