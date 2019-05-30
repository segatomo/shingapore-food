# coding: utf-8

import cv2
import requests
from urllib.parse import urljoin
import os

def canny(image):
    return cv2.Canny(image, 100, 200)


def image_classify(img):

    url = 'http://api.foodai.org/v1/classify'
    root_url = 'https://team-a.psi.ac/' 
    image_url = urljoin(root_url, img)
    print(image_url)
    payload = {
        'image_url' : image_url,
        'api_key' : 'b8eb7ea9422d05fcb1856a05a9f544ae1ebbc9d3'
    }
    res = requests.get(url, params=payload).json()

    if res['status_msg'] == 'ok':
        
        food = res['food_results'][0][0]
        score = res['food_results'][0][1]
        data = {'food': food, 'score': score}
        return data
    else:
        return {'food': 'error', 'score': res['status_msg']}


def rec_alcohol(food):
    """
    food: str
    """
    alcohol = {}
    foods_1 = ['Bak Kut Teh', 'Pig s Organ_Soup', 'Chicken Rice', 'Duck Rice', 'Claypot Rice', 'Bak Chang', 'Har Cheong Gai', 'Otak-otak', 'Bak Chor Mee', 'Porridge', 'Fish Head Bee_Hoon', 'Chwee Jia Bao', 'Kway Chap', 'Wanton Mee', 'Ayam Penyet', 'Siu Yuk', 'Char Siew Rice', 'Begedil', 'Chicken Curry', 'Yong Tau Foo']
    foods_2 = ['Drunken Prawn', 'Xiao Long Bao', 'Tau suan', 'Youtiao', 'Kong Bak Pau', 'Fish Head Steamboat', 'Keropok', 'Ayam Buah Keluak', 'Longan', 'Chilli Crab', 'Muah Chee', 'Assam Pedas', 'Hum Chim Peng', 'Tauhu Goreng', 'Onde Onde', 'Nasi Briyani', 'Appam', 'Prawn Mee', 'Popiah'] 
    foods_3 = ['Lontong', 'Fish Ball', 'Soto Ayam', 'Pulut hitam', 'Dosa', 'Lemon Barley Drink', 'lei cha fan', 'Cereal Prawns', 'Tau Hwa', 'Ketupat', 'Ban Mian', 'Durian', 'Ice Kacang', 'Chapati', 'Fried Sweet Potato_Balls', 'Tandoori', 'Sambal Sotong', 'Cendol', 'Jackfruit', 'Curry Puff']
    foods_4 = ['Mee Rebus', 'Nasi Lemak', 'Kueh Pie Tee', 'Lor Mee', 'Pork floss', 'Roti Prata', 'Soft Boiled Egg', 'Chin Chow Drink', 'Lychee', 'Teh Tarik', 'Fish Head Curry', 'Min Chiang Kueh', 'Char Kway Teow', 'Satay', 'Sambal Kangkong', 'Sugar Cane Juice', 'Laksa', 'Tutu Kueh', 'Mangosteen', 'Black Pepper Crab']
    if food in foods_1:
        alcohol['name'] = 'シンガポールスリング'
        alcohol['text'] = 'シンガポールスリングは、イギリスの小説家サマセット・モームが“東洋の神秘”とたたえた、世界一美しいと言われるシンガポールの夕焼けを表現したカクテルです。そこまで、美しい神秘的な景色をイメージして作られた「シンガポールスリング」。ロマンティックな夏に飲みたい1杯です。シンガポールスリングは1915年、シンガポールのラッフルズホテルで考案さました。トロピカルカクテルの傑作といわれています。ジンベースのお酒でパイナップルなどの南国のフルーツと一緒にカクテルにしたもので、飲みやすい味になっています。しかしアルコール度数は高めになっているので飲みすぎには注意してくださいね。'
    elif food in foods_2:
        alcohol['name'] = 'タイガービール'
        alcohol['text'] = 'フルーティさがあって飲みやすい味わいが好印象。ビール独特の苦味も残っており、万人受けするであろうビール。タイガーっぽい力強さの意味は理解に苦しむが、すごく飲みやすいビールなのでオススメです。ザ・さっぱりビールで喉ごし抜群でゴクゴク飲んでしまいます。しかしコクを求めることはできないので、ゆっくり味わって飲むようなビールではありません。東南アジアでよく見かける氷を入れてビールを飲むスタイルに完璧にマッチしたビールです（当然もっと味は薄くなります）。氷を入れたビールと辛い料理を食べるのにマッチしていると思います。'
    elif food in foods_3:
        alcohol['name'] = 'ラッフルズ'
        alcohol['text'] = 'ラッフルズは、は喉ごしが軽くスッと飲めると印象です。ビールの苦味が苦手で普段はあまりビールを飲まないという方も比較的飲みやすいでしょう。観光の合間のランチなどで軽く一杯というときにおすすめです。シンガポールらしい名前もいいですね。'
    elif food in foods_4:
        alcohol['name'] = 'マティーニ'
        alcohol['text'] = 'マティーニほど数々の逸話に彩られたカクテルはほかにありません。「カクテルの中の傑作」「カクテルの帝王」と称されるカクテル。映画『７年目の浮気』ではマリリン・モンローが、『００７』ではジェームス・ボンドが好んで飲んだカクテルです。レシピは時代と共に甘口から辛口へと変化し、スイートベルモットを使っていたのが、今ではドライベルモットを使うのが普通になっています。超辛口好みの、かのチャーチルは、ドライベルモットの瓶を眺めながらジンのストレートを飲んでいたそうであります。ハーブのような香りが強く、辛口なカクテルです。'
    else:
        alcohol['name'] = 'オリンピック'
        alcohol['text'] = '1900年にパリで開催された第2回オリンピックを記念して作られたカクテルがあります。そのまま「オリンピック」という名前のオシャレなカクテルは、ヨーロッパ随一の高級ホテル「オテル・リッツ」のバーで生まれました。オリンピックが開催される毎に新しいカクテルが考案されますが、この「オリンピック」は100年たった今も、昔と同じ作り方で愛されている唯一のもの。コニャックベースでオレンジリキュールとフレッシュオレンジジュースが女性好みのすっきり美味しいカクテルです。 '
    
    return alcohol
