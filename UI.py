# -*- coding=utf-8 -*-
import pygame
import string
from my_widget import *
from sys import exit #向sys模块借一个exit函数用来退出程序
from funcs import * # 含有组牌函数
from api import *

WHITE = (255, 255, 255)
GREEN = ( 0, 128, 128)
BLUE = ( 0, 0, 128)
BLACK = (0, 0, 0)

rank_data =[
  {
    "player_id": 1,
    "score": 173,
    "name": "test1"
  },
  {
    "player_id": 4,
    "score": 150,
    "name": "test4"
  },
  {
    "player_id": 5,
    "score": 0,
    "name": "test8"
  },
  {
    "player_id": 6,
    "score": 0,
    "name": "test7"
  },
  {
    "player_id": 2,
    "score": -7,
    "name": "test2"
  },
  {
    "player_id": 3,
    "score": -316,
    "name": "test3"
  }
    ]
suites = {
        '$': 'spade',
        '&': 'heart',
        '*': 'club',
        '#': 'diamond'
    }# $ 黑桃 spade,红桃 heart,* 梅花 club,# 方块 diamond
faces = {
        'A': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10':'10',
        'J': '11',
        'Q': '12',
        'K': '13'
    }
"""主函数"""
def main():
    """初始化"""
    pygame.init() #初始化pygame,为使用硬件做准备
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((896, 414), 0, 32)#创建了一个窗口
    screen.fill((226, 226, 226)) #颜色填充
    pygame.display.set_caption("十三水") #设置窗口标题
    text_box_username = TextBox(176, 30, 656, 131)
    text_box_password = TextBox(176, 30, 656, 207)
    card_dirt = {}
    card = "&A &2 &3 *4 *5 *6 *7 *8 #9 #10 #J #Q #K"
    card_list = card.split(" ")
    rank_data = []
    history_data = []
    text_list_rank = TextList(rank_data, 174, 185, 5, 3, [130, 200, 124], 49, 1)
    text_list_history = TextList(history_data, 69, 187, 5, 3, [131, 382, 131], 57, 2)
    text_box_username = TextBox(176, 30, 656, 131)
    text_box_password = TextBox(176, 30, 656, 207)
    """图像加载转换"""
    # 加载背景图
    img_background_screen_lobby = pygame.image.load('img/background/background_screen_lobby.png').convert()
    img_background_screen_rank = pygame.image.load('img/background/background_screen_rank.png').convert_alpha()
    img_background_screen_history = pygame.image.load('img/background/background_screen_history.png').convert_alpha()
    img_background_screen_history_detail = pygame.image.load('img/background/background_screen_history_detail.png').convert_alpha()
    img_background_screen_game = pygame.image.load('img/background/background_screen_game.jpg').convert()

    # 加载扑克牌
    for suite in suites:
        for face in faces:
            key = suite + face
            res = 'img/card/' + suites[suite] + '_' + faces[face] + '.png'
            img = pygame.image.load(res).convert()
            card_dirt[key] = img


    """按钮初始化"""
    button_to_login = Button('img/button/to_login.png',694, 270)
    button_to_register = Button('img/button/to_register.png', 704, 346)
    button_to_logout = Button('img/button/to_logout.png', 783, 27)
    button_to_open_game = Button('img/button/to_open_game.png', 679, 273)
    button_to_screen_login = Button('img/button/to_screen_login.png', 688, 114)   
    button_to_screen_register = Button('img/button/to_screen_register.png', 688, 252) 
    button_to_screen_lobby = Button('img/button/to_screen_lobby.png', 373, 348)
    button_to_screen_history = Button('img/button/to_screen_history.png', 660, 27)
    button_to_screen_rank = Button('img/button/to_screen_rank.png', 537, 27)
    button_back_to_screen_lobby = Button('img/button/back_to_screen_lobby.png',0,0)
    button_back_to_screen_choose = Button('img/button/back_to_screen_choose.png', 0, 0)
    button_to_previous_page = Button('img/button/to_previous_page.jpg', 0, 180)
    button_to_next_page = Button('img/button/to_next_page.jpg',832, 180)

    """将使用到的组件绑定到对应的页"""
    page = [[] for _ in range(9)]
    # screen_choose是一进入游戏，决定是登录还是注册的界面
    page[1].append(button_to_screen_login)
    page[1].append(button_to_screen_register)
    # screen_register
    page[2].append(button_back_to_screen_choose) 
    page[2].append(button_to_register)
    page[2].append(text_box_username)
    page[2].append(text_box_password)
    # screen_login
    page[3].append(button_back_to_screen_choose) 
    page[3].append(button_to_login)
    page[3].append(text_box_username)
    page[3].append(text_box_password)
    # screen_lobby
    page[4].append(button_to_logout)
    page[4].append(button_to_open_game)
    page[4].append(button_to_screen_rank)
    page[4].append(button_to_screen_history)
    # screen_game
    page[5].append(button_back_to_screen_lobby)
    # screen_rank
    page[6].append(button_back_to_screen_lobby)
    page[6].append(button_to_previous_page)
    page[6].append(button_to_next_page)
    page[6].append(text_list_rank)

    # screen_history
    page[7].append(button_back_to_screen_lobby)
    page[7].append(button_to_previous_page)
    page[7].append(button_to_next_page)
    page[7].append(text_list_history)

    # screen_history_detail
    page[8].append(button_back_to_screen_lobby)
    # page[8].append(button_b3)
    # page[8].append(button_n3)
 
    current_page = 1
    pygame.display.flip()
    p1 = Player('d744543', 'qweasdzxc')

    """游戏主循环"""
    while True:
        """从消息队列中获取事件并对事件进行处理"""
        for event in pygame.event.get():
            """接收到退出事件后退出程序"""
            if event.type == pygame.QUIT:
                p1.logout()
                exit()
            """监控键盘活动"""
            """使文本框中可以键入文字"""
            if event.type == pygame.KEYDOWN:
                if current_page == 2 or 3:
                    mouse = pygame.mouse.get_pos()
                    if(text_box_username.pressed(mouse)):
                        text_box_username.key_down(event)
                    if(text_box_password.pressed(mouse)):
                        text_box_password.key_down(event)
            """监控鼠标的点击活动"""
            # 当按下鼠标时，获取坐标
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos() 
                """页面跳转逻辑""" # 大量使用elif，避免连续判断
                # screen choose
                if current_page == 1:
                    if button_to_screen_register.pressed(mouse):
                        current_page = 2
                    if button_to_screen_login.pressed(mouse):
                        current_page = 3

                # screen_register
                elif current_page == 2:
                    if button_back_to_screen_choose.pressed(mouse):
                        current_page = 1
                    if button_to_register.pressed(mouse):
                        p1.register(text_box_username.get_text(), text_box_password.get_text())
                        if p1.check_register_status():
                            current_page = 3

                # screen_login
                elif current_page == 3:
                    if button_back_to_screen_choose.pressed(mouse):
                        current_page = 1
                    if button_to_login.pressed(mouse):
                        p1 = Player(text_box_username.get_text(), text_box_password.get_text()) #定义玩家对象
                        p1.login()
                        if p1.check_login_status():
                            current_page = 4
                
                # screen_lobby
                elif current_page == 4:
                    if button_to_logout.pressed(mouse):
                        current_page = 1
                    if button_to_open_game.pressed(mouse):
                        card = p1.getCard() # getcard函数就是游戏开局标志
                        p1.push = False #不要提交手牌
                        current_page = 5
                    if button_to_screen_rank.pressed(mouse):
                        current_page = 6
                        rank_data = p1.get_rank()
                        text_list_rank.update(0, rank_data)
                    if button_to_screen_history.pressed(mouse):
                        current_page = 7
                        history_data = p1.get_history(0, 20, p1.user_id)
                        text_list_history.update(0, history_data)

                # screen_game
                elif current_page == 5:
                    if button_back_to_screen_lobby.pressed(mouse):
                        current_page = 4

                # screen_rank
                elif current_page == 6:
                    if button_back_to_screen_lobby.pressed(mouse):
                        current_page = 4
                    if button_to_previous_page.pressed(mouse):
                        if text_list_rank.p != 0:
                            text_list_rank.update(text_list_rank.p - 1)
                    if button_to_next_page.pressed(mouse):
                        if((text_list_rank.p + 1) * 5 <= len(rank_data) - 1 ):
                            text_list_rank.update(text_list_rank.p + 1)

                 # screen_history
                elif current_page == 7:
                    if button_back_to_screen_lobby.pressed(mouse):
                        current_page = 4
                    if button_to_previous_page.pressed(mouse):
                        if text_list_history.p != 0:
                            text_list_history.update(text_list_history.p - 1)
                    if button_to_next_page.pressed(mouse):
                      if((text_list_history.p + 1) * 5 <= len(history_data) - 1 ):
                        text_list_history.update(text_list_history.p + 1)
                """
                #  screen_history_detail
                elif current_page == 8:
                    if button_back_to_screen_lobby.pressed(mouse):
                        current_page = 4
                #   if button_to_next_page.pressed(mouse):
                #         pass
                #   if button_to_previous_page.pressed(mouse):
                #         pass
                """
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        """在第n页，显示该页的所有组件"""
        # display update
        if current_page == 1:
            screen.blit(img_background_screen_lobby, (0, 0))
            for w in page[1]:
                w.draw(screen)
            # 懒得写文本：“账号”“密码”

        elif current_page == 2:
            screen.blit(img_background_screen_lobby, (0, 0))
            for w in page[2]:
                w.draw(screen)
            # 懒得写文本：“账号”“密码” 

        elif current_page == 3:
            screen.blit(img_background_screen_lobby, (0, 0))
            for w in page[3]:
                w.draw(screen)

        elif current_page == 4:
            screen.blit(img_background_screen_lobby, (0, 0))
            for w in page[4]:
                w.draw(screen)
        
        elif current_page == 5:
            screen.blit(img_background_screen_game, (0, 0))
            for w in page[5]:
                w.draw(screen)
            draw_card(screen, 200,125, card_list, card_dirt)

        elif current_page == 6:
            screen.blit(img_background_screen_lobby, (0, 0))
            screen.blit(img_background_screen_rank, (76, 23))
            for w in page[6]:
                w.draw(screen)
        
        elif current_page == 7:
            screen.blit(img_background_screen_lobby, (0, 0))
            screen.blit(img_background_screen_history, (76, 23))
            for w in page[7]:
                w.draw(screen)
        
        elif current_page == 8:
            screen.blit(img_background_screen_lobby, (0, 0))
            screen.blit(img_background_screen_history, (76, 23))
            for w in page[8]:
                w.draw(screen)

        # x, y = pygame.mouse.get_pos() #获得鼠标位置
        # x-= img_mouse.get_width() / 2
        # y-= img_mouse.get_height() / 2 #计算光标的左上角位置
        #把光标画上去
        # screen.blit(img_mouse, (x, y))
        pygame.display.update()
        if(current_page ==5 and p1.push == False):
                ans = findAns(card) #组牌
                p1.game_submit(ans)
                p1.push = True        
        pygame.time.delay(33)
        pygame.display.flip()
        clock.tick(20)

if __name__ == '__main__':
    main()