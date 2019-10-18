#!/usr/bin/python
# -*- coding: utf-8 -*-
from normal import *




def findAns(card):
    card_sort1 = sorted(card)
    card_sort2 = sorted(card, key=functools.cmp_to_key(reversed_cmp))
    card_sort3 = card_sort2[::-1]  # 表示大小降序
    while True:  # 找后墩
        if tonghuashun(card_sort1) != 0:
            houdun = tonghuashun(card_sort1)
            break
        if zhadan(card_sort3) != 0:
            houdun = zhadan(card_sort3)
            break
        if hulu(card_sort3) != 0:
            houdun = hulu(card_sort3)
            break
        if tonghua(card_sort1) != 0:
            houdun = tonghua(card_sort1)
            break
        if shunzi(card_sort3) != 0:
            houdun = shunzi(card_sort3)
            break
        if santiao(card_sort3) != 0:
            houdun = santiao(card_sort3)
            break
        if liangdui(card_sort3) != 0:
            houdun = liangdui(card_sort3)
            break
        if duizi(card_sort3) != 0:
            houdun = duizi(card_sort3)
            break
        houdun = card_sort3[0:5]
        break

    card_sort1 = [card for card in card_sort1 if card not in set(houdun)]  # 删去后墩的牌
    card_sort2 = [card for card in card_sort2 if card not in set(houdun)]
    card_sort3 = [card for card in card_sort3 if card not in set(houdun)]
    while True:  # 找中墩
        if tonghuashun(card_sort1) != 0:
            zhongdun = tonghuashun(card_sort1)
            break
        if zhadan(card_sort3) != 0:
            zhongdun = zhadan(card_sort3)
            break
        if hulu(card_sort3) != 0:
            zhongdun = hulu(card_sort3)
            break
        if tonghua(card_sort1) != 0:
            zhongdun = tonghua(card_sort1)
            break
        if shunzi(card_sort3) != 0:
            zhongdun = shunzi(card_sort3)
            break
        if santiao(card_sort3) != 0:
            zhongdun = santiao(card_sort3)
            break
        if liangdui(card_sort3) != 0:
            zhongdun = liangdui(card_sort3)
            break
        if duizi(card_sort3) != 0:
            zhongdun = duizi(card_sort3)
            break
        zhongdun = card_sort3[0:5]
        break


    qiandun = [card for card in card_sort2 if card not in set(zhongdun)]

    qd = ' '.join(qiandun)
    zd = ' '.join(zhongdun)
    hd = ' '.join(houdun)
    ans = []
    ans.append(qd)
    ans.append(zd)
    ans.append(hd)
    return ans