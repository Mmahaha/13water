def flag(x):
    if (x[1] == 'A'):
        return 14
    elif (x[1] == '1'):
        return 10
    elif (x[1] == 'J'):
        return 11
    elif (x[1] == 'Q'):
        return 12
    elif (x[1] == 'K'):
        return 13
    else:
        return ord(x[1]) - 48


def tonghua(cards):  # 传入按花色排序的牌
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for card in cards:
        if '#' in card:
            count1 += 1
        elif '$' in card:
            count2 += 1
        elif '&' in card:
            count3 += 1
        elif '*' in card:
            count4 += 1

    if (count1 >= 5):
        return cards[0:5];
    elif (count2 >= 5):
        return cards[count1:count1 + 5];
    elif (count3 >= 5):
        return cards[count1 + count2:count1 + count2 + 5];
    elif (count4 >= 5):
        return cards[-5:];
    else:
        return 0


def shunzi(cards):  # 传入按大小排序的牌
    a = cards[0:1]
    find_flag = 0
    for i in range(len(cards) - 1):
        if find_flag == 1 and flag(cards[i + 1]) != flag(cards[i]) + 1 and flag(cards[i + 1]) != flag(cards[i]):
            break
        elif flag(cards[i + 1]) == flag(cards[i]) + 1:
            a.append(cards[i + 1])
            if len(a) == 5:
                find_flag = 1
            if len(a) == 6:
                del a[0]
        elif flag(cards[i]) == flag(cards[i + 1]):
            continue
        else:
            a = cards[i + 1:i + 2]
    if len(a) == 5:
        return a
    else:
        return 0


def zhadan(cards):  # 传入按大小排序的牌
    a = cards[0:1]
    for i in range(len(cards) - 1):
        if flag(cards[i + 1]) == flag(cards[i]):
            a.append(cards[i + 1])
            if len(a) == 4:
                break
        else:
            a = cards[i + 1:i + 2]
    if len(a) == 4:
        cards_dela = [card for card in cards if card not in set(a)][::-1]
        single = cards_dela[0:1]
        for i in range(len(cards_dela)-1):
            if flag(cards_dela[i]) != flag(cards_dela[i + 1]) and flag(cards_dela[i]) != flag(cards_dela[i - 1]):
                single = cards_dela[i:i + 1]
                break
        return a + single
    else:
        return 0

def zhao_san(cards):
    s = cards[0:1]
    for i in range(len(cards) - 1):
        if flag(cards[i + 1]) == flag(cards[i]):
            s.append(cards[i + 1])
            if len(s) == 3:
                break
        else:
            s = cards[i + 1:i + 2]
    return s

def hulu(cards):  # 传入按大小降序序的牌
    s = zhao_san(cards)
    if len(s) != 3:
        return 0
    cards_dels = [card for card in cards if card not in set(s)][::-1]  # 删去葫芦后剩下的牌并返回升序的牌
    d = cards_dels[0:1]     # 开始找最小对子
    for i in range(len(cards_dels) - 1):
        if flag(cards_dels[i + 1]) == flag(cards_dels[i]):
            d.append(cards_dels[i + 1])
            if len(d) == 2 and i != len(cards_dels) - 2 and flag(cards_dels[i + 1]) != flag(cards_dels[i + 2]) and flag(cards_dels[i - 1]) != flag(
                    cards_dels[i]):     # 确保对子不会与其他牌凑成葫芦
                break
            else:
                d = cards_dels[i + 1:i + 2]
        else:
            d = cards_dels[i + 1:i + 2]

    if len(d) != 2:
        return 0
    else:
        return s + d


def santiao(cards):
    s = zhao_san(cards)
    if len(s) == 3:
        cards_dels = [card for card in cards if card not in set(s)][::-1]
        return s + cards_dels[0:2]
    else:
        return 0
    

def liangdui(cards):
    d = cards[0:1]
    for i in range(len(cards) - 1):
        if flag(cards[i + 1]) == flag(cards[i]):
            d.append(cards[i + 1])
            if len(d) == 2:
                break
        else:
            d = cards[i + 1:i + 2]
    if len(d) != 2:
        return 0
    cards_deld = [card for card in cards if card not in set(d)][::-1]
    d2 = cards_deld[0:1]
    for i in range(len(cards_deld) - 1):
        if flag(cards_deld[i + 1]) == flag(cards_deld[i]):
            d2.append(cards_deld[i + 1])
            if len(d2) == 2:
                break
        else:
            d2 = cards_deld[i + 1:i + 2]
    if len(d2) != 2:
        return 0
    cards_deldd = [card for card in cards_deld if card not in set(d2)]
    dan = cards_deldd[0:1]
    for i in range(len(cards_deldd)-1):
        if flag(cards_deldd[i]) != flag(cards_deldd[i+1]) and flag(cards_deldd[i]) != flag(cards_deldd[i-1]):
            dan = cards_deldd[i: i+1]
            break
    return d + d2 + dan


def duizi(cards):
    d = cards[0:1]
    for i in range(len(cards) - 1):
        if flag(cards[i + 1]) == flag(cards[i]):
            d.append(cards[i + 1])
            if len(d) == 2:
                break
        else:
            d = cards[i + 1:i + 2]
    if len(d) != 2:
        return 0
    cards_deld = [card for card in cards if card not in set(d)]
    return d + cards_deld[-3:]
