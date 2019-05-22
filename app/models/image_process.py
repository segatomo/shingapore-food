"""
import cv2

def canny(image):
    return cv2.Canny(image, 100, 200)
"""

import requests
import base64
import json

GOOGLE_CLOUD_VISION_API_URL = 'https://vision.googleapis.com/v1/images:annotate?key='
API_KEY = 'AIzaSyA-4U0EWn5_9_7Xy7bpIzUH0OaLrjNsHus'

# APIを呼び、認識結果を返す
def request_cloud_vison_api(img):
    img = base64.b64encode(img)
    api_url = GOOGLE_CLOUD_VISION_API_URL + API_KEY
    req_body = json.dumps({
        'requests': [{
            'image': {
                'content': img.decode('utf-8') # jsonに変換するためにstring型に変換する
            },
            'features': [{
                'type': 'LABEL_DETECTION', # ラベル検出
                'maxResults': 5,
            }]
        }]
    })
    res = requests.post(api_url, data=req_body)
    result = res.json()["responses"][0]["labelAnnotations"]

    descpirtion = []
    score = []
    for i in range(5):
        descpirtion.append(result[i]["description"]) 
        score.append(result[i]["score"])

    return descpirtion, score
"""
# 画像読み込み
def img_to_base64(filepath):
    with open(filepath, 'rb') as img:
        img_byte = img.read()
    return base64.b64encode(img_byte)

# 文字認識させたい画像を./img.pngとする
# img_base64 = img_to_base64('./img.png')
result = request_cloud_vison_api(img)

#認識した文字の位置など、すべての情報を出力
#print("{}".format(json.dumps(result, indent=4)))
"""
