#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import functools
from funcs import reversed_cmp 


url = 'https://api.shisanshui.rtxux.xyz/game/open'
headers = {'X-Auth-Token': "a52b832e-a7f9-4061-abcd-79f19db27a02"}
response = requests.post(url,  headers = headers) 
response_dict = response.json()
card = response_dict['data']['card'].split(' ')
print(card)
card_sort1 = sorted(card)
print('花色排序:',card_sort1)
card_sort2 = sorted(card, key=functools.cmp_to_key(reversed_cmp))
print('大小排序:',card_sort2)