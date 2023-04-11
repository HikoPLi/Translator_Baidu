from urllib.parse import quote
import requests
import random
import hashlib
import json

with open("loginCD.json") as id:
    json4id = json.load(id)

    appid = json4id[0]['appid']
    secretKey = json4id[0]['secretKey']


def get_myurl(words, toLang, fromLang='auto'):
    for word in words:
        salt = random.randint(32768, 65536)
        sign = appid + word + str(salt) + secretKey
        myMd5 = hashlib.md5()
        myMd5.update(sign.encode("utf-8"))
        sign = myMd5.hexdigest()
        """
        签名生成方法如下：
        1、将请求参数中的 APPID(appid), 翻译query(q, 注意为UTF-8编码), 随机数(salt), 以及平台分配的密钥(可在管理控制台查看)
        按照 appid+q+salt+密钥 的顺序拼接得到字符串1。
        2、对字符串1做md5，得到32位小写的sign。
        """
        yield '/api/trans/vip/translate'+'?appid='+appid+'&q='+quote(word)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign


def get_translate_word(url):
    # print('http://api.fanyi.baidu.com' + url)
    try:
        response = requests.get('http://api.fanyi.baidu.com' + url, timeout=5)
        result = response.json()
        outputJSON = str(result['trans_result'])
        outputJSON = outputJSON.replace("src", "Input: ")
        outputJSON = outputJSON.replace("dst", "Output: ")
        outputJSON = outputJSON.replace("]", "")
        outputJSON = outputJSON.replace("[", "")
        outputJSON = outputJSON.replace("}", "")
        outputJSON = outputJSON.replace("{", "")
        print(f"{outputJSON}")
    except Exception as e:
        print(e)
