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
        The signature generation method is as follows:
        1. Combine the APPID (appid), translation query (q, note the UTF-8 encoding), random number (salt), and the key assigned by the platform (available in the management console) in the request parameters
        The string 1 is obtained by splicing appid+q+salt+key in the order of appid+q+salt+key.
        2. do md5 on string 1 to get 32-bit lowercase sign.
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
