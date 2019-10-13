from funcs import flag
def tonghua(cards): #传入按花色排序的牌
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for card in cards:
        if '#' in card:
            count1+=1
        elif '$' in card:
            count2+=1
        elif '&' in card:
            count3+=1
        elif '*' in card:
            count4+=1
    
    if(count1>=5):
        return cards[0:5];
    elif(count2>=5):
        return cards[count1:count1+5];
    elif(count3>=5):
        return cards[count1+count2:count1+count2+5];
    elif(count4>=5):
        return cards[-5:];
    else:
        return 0

def shunzi(cards):   #传入按大小排序的牌
    a = cards[0:1]
    find_flag = 0
    for i in range(len(cards)-1):
        if find_flag == 1 and flag(cards[i+1])!=flag(cards[i])+1 and flag(cards[i+1])!=flag(cards[i]):
            break
        elif flag(cards[i+1]) == flag(cards[i])+1:
            a.append(cards[i+1])
            if len(a)==5:
                find_flag = 1
            if len(a)==6:
                del a[0]
        elif flag(cards[i]) == flag(cards[i+1]):
            continue
        else:
            a = cards[i+1:i+2]
    if len(a)==5:
        return a
    else:
        return 0

def zhadan(cards):  #传入按大小排序的牌
    a = cards[0:1]
    for i in range(len(cards)-1):
        if flag(cards[i+1]) == flag(cards[i]):
            a.append(cards[i+1])
            if len(a)==4:
                break
        else:
            a = cards[i+1:i+2]
    if len(a)==4:
        return a
    else:
        return 0

def hulu(cards): #传入按大小排序的牌
    s = cards[0:1]
    for i in range(len(cards)-1):
        if flag(cards[i+1]) == flag(cards[i]):
            s.append(cards[i+1])
            if len(s)==3:
                break
        else:
            s = cards[i+1:i+2]
    if len(s)!=3:
        return 0
    cards_dels = [card for card in cards if card not in set(s)] #删去葫芦后剩下的牌
    d = cards_dels[0:1]
    for i in range(len(cards_dels)-1):
        if flag(cards_dels[i+1]) == flag(cards_dels[i]):
            d.append(cards[i+1])
            if len(d)==2:
                break
        else:
            d = cards_dels[i+1:i+2]

    if len(d)!=2:
        return 0
    else:
        return s+d


def santiao(cards):
    s = cards[0:1]
    for i in range(len(cards)-1):
        if flag(cards[i+1]) == flag(cards[i]):
            s.append(cards[i+1])
            if len(s)==3:
                break
        else:
            s = cards[i+1:i+2]
    if len(s)==3:
        cards_dels = [card for card in cards if card not in set(s)]
        return s+cards_dels[0:2]
    else:
        return 0
    
def liangdui(cards):
    d = cards[0:1]
    for i in range(len(cards)-1):
        if flag(cards[i+1]) == flag(cards[i]):
            d.append(cards[i+1])
            if len(d)==2:
                break
        else:
            d = cards[i+1:i+2]
    if len(d)!=2:
        return 0
    cards_deld = [card for card in cards if card not in set(d)]
    d2 = cards_deld[0:1]
    for i in range(len(cards_deld)-1):
        if flag(cards_deld[i+1]) == flag(cards_deld[i]):
            d2.append(cards_deld[i+1])
            if len(d2)==2:
                break
        else:
            d2 = cards_deld[i+1:i+2]
    if len(d2)!=2:
        return 0
    cards_deldd = [card for card in cards_deld if card not in set(d2)]
    
    return d+d2+cards_deldd[0:1]

def duizi(cards):
    d = cards[0:1]
    for i in range(len(cards)-1):
        if flag(cards[i+1]) == flag(cards[i]):
            d.append(cards[i+1])
            if len(d)==2:
                break
        else:
            d = cards[i+1:i+2]
    if len(d)!=2:
        return 0
    cards_deld = [card for card in cards if card not in set(d)]
    return d+cards_deld[0:3]



cards = ['*2', '#3', '&4', '$4', '#5', '*5', '$6', '&6', '&6', '*8', '*9', '$J', '$Q']  #test样例
print(hulu(cards))