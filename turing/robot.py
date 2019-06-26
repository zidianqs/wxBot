#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: hollay
# @Date:   2018--18 21:21:
# @Last Modified by:   hollay
# @Last Modified time: 2018--18 21:21:

import requests

API_KEY = '436edefafbcf4431b3bcfe19e000e0f2'
API_SECRET = '5e64f9dcce04d6e9'

API = 'http://openapi.tuling123.com/openapi/api/v2'


req = {
	"reqType":0,
    "perception": {
        "inputText": {
            "text": "附近的酒店"
        }
    },
    "userInfo": {
        "apiKey": API_KEY,
        "userId": API_SECRET
    }
}
resp = requests.post(API, req)
print resp.content


