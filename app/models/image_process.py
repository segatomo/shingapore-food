# coding: utf-8

import cv2
import requests
from urllib.parse import urljoin
import os

def canny(image):
    return cv2.Canny(image, 100, 200)

def image_classify(img):

    url = 'http://api.foodai.org/v1/classify'
    image_url = 'https://team-a.psi.ac/' 
    image_url = urljoin(image_url, img)
    payload = {
        'image_url' : image_url,
        'api_key' : 'b8eb7ea9422d05fcb1856a05a9f544ae1ebbc9d3',
        'num_tag': 5
    }
    res = requests.get(url, params=payload).json()

    if res['status_msg'] == 'ok':
        foods = []
        scores = []
        for i in range(5):
            foods.append(res['food_results'][i][0])
            scores.append(res['food_results'][i][1])
        result = [foods, scores]
        return result

    else:
        return res['status_msg']
