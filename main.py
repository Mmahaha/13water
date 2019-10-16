#!/usr/bin/python
# -*- coding: utf-8 -*-
from api import *
from funcs import *


p1 = Player('d744543', 'qweasdzxc')
p1.login()
for i in range(1000000):
    card = p1.getCard()
    print(card)
    ans = findAns(card)
    print(ans)
    p1.game_submit(ans)
