from normal import *
import read
from funcs import *
import functools

card = read.getCard()
print(card)
card_sort1 = sorted(card)
print('花色排序:',card_sort1)
card_sort2 = sorted(card, key=functools.cmp_to_key(reversed_cmp))
print('大小升序:',card_sort2)
card_sort3 = card_sort2[: :-1] #表示大小降序
print('大小降序:',card_sort3)
while True:     #找后墩
    if zhadan(card_sort2) != 0:
        houdun = zhadan(card_sort2)
        break
    if hulu(card_sort2) != 0:
        houdun = hulu(card_sort2)
        type = 1
        break
    if tonghua(card_sort1) != 0:
        houdun = tonghua(card_sort1)
        break
    if shunzi(card_sort2) != 0:
        houdun = shunzi(card_sort2)
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

card_sort1 = [card for card in card_sort1 if card not in set(houdun)]   #删去后墩的牌
card_sort2 = [card for card in card_sort2 if card not in set(houdun)]
card_sort3 = [card for card in card_sort3 if card not in set(houdun)]  

while True:     #找前墩
    if zhadan(card_sort2) != 0:
        zhongdun = zhadan(card_sort2)
        break
    if hulu(card_sort2) != 0:
        zhongdun = hulu(card_sort2)
        break
    if tonghua(card_sort1) != 0:
        zhongdun = tonghua(card_sort1)
        break
    if shunzi(card_sort2) != 0:
        zhongdun = shunzi(card_sort2)
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
print("houdun:",houdun)
print("zhongdun:",zhongdun)
print("qiandun:",qiandun)
