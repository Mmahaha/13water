#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json


def getCard():
    url = 'https://api.shisanshui.rtxux.xyz/game/open'
    headers = {'X-Auth-Token': "8f0a52a2-540b-4d29-a035-746f71a7c1c3"}
    response = requests.post(url,  headers = headers) 
    response_dict = response.json()
    card = response_dict['data']['card'].split(' ')
    return card
