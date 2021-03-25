import pygame, sys
import itertools
import matplotlib.pyplot as plt
from Ham import *
# from WSPTui import *
# from SPTui import * 
from pygame.locals import *
import ctypes 
from tkinter import *
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Phần mềm điều độ')
X = 1152
Y = 700
screen = pygame.display.set_mode((X, Y),0,32)

# màu sắc và font chữ
GREY = (120, 120 ,120)
WHITE = (255, 255, 255)
GREEN = (3, 252, 161)
BLUE = (3, 161, 252)
PINK = (255, 112, 181)
BLACK = (0, 0, 0)
BG = (253,243,244)
RED = (255,99,71)
# chỉnh font cho chữ trong ô
font = pygame.font.SysFont(None, 63)
fontto = pygame.font.Font('Raleway-Medium-vi.ttf', 43)
fontnho = pygame.font.Font('Raleway-Medium-vi.ttf', 20)
# tạo 1 hàm để đánh chữ, muốn dùng chữ thì dùng hàm này
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
# Tạo 1 hàm để thêm ảnh cho nhanh
def draw_image(link,surface,x,y):
    image = pygame.image.load(link)
    surface.blit(image, (x, y))
click = False
 
def main_menu():
    while True:
 
        screen.fill(BG)
        draw_text('Màn hình chính', fontnho, BLACK, screen, 20, 20)

        draw_image('Group_8.png',screen,205,117)
        draw_image('Group_1.png',screen,205,287)
        draw_image('Group_1.png',screen,503,287)
        draw_image('Group_1.png',screen,801,287)
        draw_image('Group_1.png',screen,503,458)
        draw_image('Group_1.png',screen,801,458)
        draw_image('Group_1.png',screen,205,458)


        draw_text('LỰA CHỌN LUẬT PHÂN VIỆC', fontto, WHITE, screen, 293, 144)    
        draw_text(("SPT"), fontto, WHITE, screen, 237, 316)
        draw_text(("SPT_d"), fontto, WHITE, screen, 515, 316)
        draw_text(("ERD"), fontto, WHITE, screen, 834, 316)
        draw_text(("WSPT"), fontto, WHITE, screen, 216, 487)
        draw_text(("EDD"), fontto, WHITE, screen, 536, 487)
        draw_text(("LPT"), fontto, WHITE, screen, 834, 487)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
            # Nếu click chuột trong khoảng này thì chạy thuật tonas SPT
                if (pygame.mouse.get_pos()[0] -256)**2 + (pygame.mouse.get_pos()[1] -341)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -299)**2 + (pygame.mouse.get_pos()[1] -341)**2 <= (60)**2 :
                    game_SPT()

                if (pygame.mouse.get_pos()[0] -546)**2 + (pygame.mouse.get_pos()[1] -341)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -605)**2 + (pygame.mouse.get_pos()[1] -341)**2 <= (60)**2 :   
                    game_SPT_d()

                if (pygame.mouse.get_pos()[0] -844)**2 + (pygame.mouse.get_pos()[1] -341)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -895)**2 + (pygame.mouse.get_pos()[1] -341)**2 <= (60)**2 :
                    game_ERD()

                if (pygame.mouse.get_pos()[0] -256)**2 + (pygame.mouse.get_pos()[1] -514)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -299)**2 + (pygame.mouse.get_pos()[1] -512)**2 <= (60)**2 :
                    game_WSPT()

                if (pygame.mouse.get_pos()[0] -546)**2 + (pygame.mouse.get_pos()[1] -512)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -605)**2 + (pygame.mouse.get_pos()[1] -512)**2 <= (60)**2 :
                    game_EDD()

                if (pygame.mouse.get_pos()[0] -844)**2 + (pygame.mouse.get_pos()[1] -512)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -895)**2 + (pygame.mouse.get_pos()[1] -512)**2 <= (60)**2 :
                    game_LPT()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        click = False
        pygame.display.update()
        mainClock.tick(60)
 
def game_SPT():
    # Điều chỉnh đầu vào hình ô vuông
    #100, 100 (2 vrí đầu là x,y ) 
    # Cái cuối là chiều rộng
    input_box = pygame.Rect(450 ,50, 140, 50)
    input_box2 = pygame.Rect(450, 150, 140, 50)    
    color_inactive = (255,159,156)
    color_active = (255,8,0)
    color = color_inactive
    color2 = color_inactive
    active = False
    active2 = False
    text = ''
    text2 = ''
    done = False
    running = True

    while running:
        screen.fill(BG)
        

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box2.collidepoint(event.pos):
                        active2 = not active2
                    else:
                        active2 = False
                    color2 = color_active if active2 else color_inactive

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        elif event.key == pygame.K_DELETE:
                            text = ''
                        else:
                            text += event.unicode
                    if active2:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text2 = text2[:-1]
                        else:
                            text2 += event.unicode

                    def chaySPT():
                        n = int(text)
                        hoanvi = list(itertools.permutations(range(1,n+1)))

                        pj = text2
                        pj = pj.split(' ')
                        pj = [int(i) for i in pj]
                        #Thuật toán xử lý WSPT
                        BoSo, Min_c = thuat_toan_SPT(n,pj)

                        tieude = "Hàm mục tiêu là: %d"%(Min_c)
                        # Hàm hiển thị sơ đồ gantt
                        try:
                            gantt(BoSo,pj,Min_c)
                        except:
                            pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >525 and pygame.mouse.get_pos()[1] >400:
                        if pygame.mouse.get_pos()[0] <625 and pygame.mouse.get_pos()[1] <450:
                            chaySPT()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        chaySPT()
        except:
            Mbox("Ôi không", 'Nhập sai đầu vào rồi', 5)
        screen.fill(BG)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(400, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        txt_surface2 = font.render(text2, True, color2)
        width2 = max(400, txt_surface2.get_width()+10)
        input_box2.w = width2
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        pygame.draw.rect(screen, color2, input_box2, 2)

        #Vẽ HCN

        # Viết tiêu đề

        draw_text('SPT', fontnho,RED, screen, 25, 10)
        draw_text(("Nhập số lượng công việc: "), fontnho, BLACK, screen, 25, 50)
        draw_text(("Nhập thời gian hoàn thành từng công việc"), fontnho, BLACK, screen, 25, 150)
        draw_text(("(cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 170)

        pygame.draw.rect(screen, PINK, (525,400,100,50))


        
        pygame.display.update()
        mainClock.tick(60)
 
def game_WSPT():
    # Điều chỉnh đầu vào hình ô vuông
    #100, 100 (2 vrí đầu là x,y ) 
    # Cái cuối là chiều rộng
    input_box = pygame.Rect(450 ,50, 140, 50)
    input_box2 = pygame.Rect(450, 150, 140, 50)
    input_box3 = pygame.Rect(450, 250, 140, 50)    
    color_inactive = (255,159,156)
    color_active = (255,8,0)
    color = color_inactive
    color2 = color_inactive
    color3 = color_inactive
    active = False
    active2 = False
    active3 = False
    text = ''
    text2 = ''
    text3 = ''
    done = False
    running = True

    while running:
        screen.fill(BG)
        

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box2.collidepoint(event.pos):
                        active2 = not active2
                    else:
                        active2 = False
                    color2 = color_active if active2 else color_inactive

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box3.collidepoint(event.pos):
                        active3 = not active3
                    else:
                        active3 = False
                    color3 = color_active if active3 else color_inactive

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        elif event.key == pygame.K_DELETE:
                            text = ''
                        else:
                            text += event.unicode
                    if active2:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text2 = text2[:-1]
                        else:
                            text2 += event.unicode
                    if active3:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text3 = text3[:-1]
                        else:
                            text3 += event.unicode

                    def chayWSPT():
                        n = int(text)
                        hoanvi = list(itertools.permutations(range(1,n+1)))

                        pj = text2
                        pj = pj.split(' ')
                        pj = [int(i) for i in pj]
                        wj = text3
                        wj = wj.split(' ')
                        wj = [int(i) for i in wj]
                        #Thuật toán xử lý WSPT
                        BoSo, Min_c = thuat_toan_WSPT(n,pj,wj)

                        tieude = "Hàm mục tiêu là: %d"%(Min_c)
                        # Hàm hiển thị sơ đồ gantt
                        try:
                            gantt(BoSo,pj,Min_c)
                        except:
                            pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >525 and pygame.mouse.get_pos()[1] >400:
                        if pygame.mouse.get_pos()[0] <625 and pygame.mouse.get_pos()[1] <450:
                            chayWSPT()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        chayWSPT()
        except:
            Mbox("Ôi không", 'Nhập sai đầu vào rồi', 5)
        screen.fill(BG)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(400, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        txt_surface2 = font.render(text2, True, color2)
        width2 = max(400, txt_surface2.get_width()+10)
        input_box2.w = width2
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        pygame.draw.rect(screen, color2, input_box2, 2)

        txt_surface3 = font.render(text3, True, color3)
        width3 = max(400, txt_surface3.get_width()+10)
        input_box3.w = width3
        screen.blit(txt_surface3, (input_box3.x+5, input_box3.y+5))
        pygame.draw.rect(screen, color3, input_box3, 2)

        # Viết tiêu đề

        draw_text('ERD', fontnho,RED, screen, 25, 10)
        draw_text(("Nhập số lượng công việc: "), fontnho, BLACK, screen, 25, 50)
        draw_text(("Nhập thời gian hoàn thành từng công việc"), fontnho, BLACK, screen, 25, 150)
        draw_text(("(cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 170)

        draw_text(("Nhập ngày tới hạn từng công việc"), fontnho, BLACK, screen, 25, 250)
        draw_text(("(cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 270)

        pygame.draw.rect(screen, PINK, (525,400,100,50))


        
        pygame.display.update()
        mainClock.tick(60)

def game_ERD():
    # Điều chỉnh đầu vào hình ô vuông
    #100, 100 (2 vrí đầu là x,y ) 
    # Cái cuối là chiều rộng
    input_box = pygame.Rect(450 ,50, 140, 50)
    input_box2 = pygame.Rect(450, 150, 140, 50)
    input_box3 = pygame.Rect(450, 250, 140, 50)    
    color_inactive = (255,159,156)
    color_active = (255,8,0)
    color = color_inactive
    color2 = color_inactive
    color3 = color_inactive
    active = False
    active2 = False
    active3 = False
    text = ''
    text2 = ''
    text3 = ''
    done = False
    running = True

    while running:
        screen.fill(BG)
        

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box2.collidepoint(event.pos):
                        active2 = not active2
                    else:
                        active2 = False
                    color2 = color_active if active2 else color_inactive

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box3.collidepoint(event.pos):
                        active3 = not active3
                    else:
                        active3 = False
                    color3 = color_active if active3 else color_inactive

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        elif event.key == pygame.K_DELETE:
                            text = ''
                        else:
                            text += event.unicode
                    if active2:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text2 = text2[:-1]
                        else:
                            text2 += event.unicode
                    if active3:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text3 = text3[:-1]
                        else:
                            text3 += event.unicode

                    def chayERD():
                        n = int(text)

                        pj = text2
                        pj = pj.split(' ')
                        pj = [int(i) for i in pj]
                        dj = text3
                        dj = dj.split(' ')
                        dj = [int(i) for i in dj]
                        #Thuật toán xử lý WSPT
                        thuat_toan_ERD(n,pj,dj)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >525 and pygame.mouse.get_pos()[1] >400:
                        if pygame.mouse.get_pos()[0] <625 and pygame.mouse.get_pos()[1] <450:
                            chayERD()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        chayERD()
        except:
            Mbox("Ôi không", 'Nhập sai đầu vào rồi', 5)
        screen.fill(BG)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(400, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        txt_surface2 = font.render(text2, True, color2)
        width2 = max(400, txt_surface2.get_width()+10)
        input_box2.w = width2
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        pygame.draw.rect(screen, color2, input_box2, 2)

        txt_surface3 = font.render(text3, True, color3)
        width3 = max(400, txt_surface3.get_width()+10)
        input_box3.w = width3
        screen.blit(txt_surface3, (input_box3.x+5, input_box3.y+5))
        pygame.draw.rect(screen, color3, input_box3, 2)

        # Viết tiêu đề

        draw_text('ERD', fontnho,RED, screen, 25, 10)
        draw_text(("Nhập số lượng công việc: "), fontnho, BLACK, screen, 25, 50)
        draw_text(("Nhập thời gian hoàn thành từng công việc"), fontnho, BLACK, screen, 25, 150)
        draw_text(("(cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 170)

        draw_text(("Nhập trọng số từng công việc"), fontnho, BLACK, screen, 25, 250)
        draw_text(("(cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 270)

        pygame.draw.rect(screen, PINK, (525,400,100,50))


        
        pygame.display.update()
        mainClock.tick(60)

def game_SPT_d():
    # Điều chỉnh đầu vào hình ô vuông
    #100, 100 (2 vrí đầu là x,y ) 
    # Cái cuối là chiều rộng
    input_box = pygame.Rect(450 ,50, 140, 50)
    input_box2 = pygame.Rect(450, 150, 140, 50)
    input_box3 = pygame.Rect(450, 250, 140, 50)    
    color_inactive = (255,159,156)
    color_active = (255,8,0)
    color = color_inactive
    color2 = color_inactive
    color3 = color_inactive
    active = False
    active2 = False
    active3 = False
    text = ''
    text2 = ''
    text3 = ''
    done = False
    running = True

    while running:
        screen.fill(BG)
        

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box2.collidepoint(event.pos):
                        active2 = not active2
                    else:
                        active2 = False
                    color2 = color_active if active2 else color_inactive

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box3.collidepoint(event.pos):
                        active3 = not active3
                    else:
                        active3 = False
                    color3 = color_active if active3 else color_inactive

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        elif event.key == pygame.K_DELETE:
                            text = ''
                        else:
                            text += event.unicode
                    if active2:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text2 = text2[:-1]
                        else:
                            text2 += event.unicode
                    if active3:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text3 = text3[:-1]
                        else:
                            text3 += event.unicode

                    def chaySPT_d():
                        n = int(text)

                        pj = text2
                        pj = pj.split(' ')
                        pj = [int(i) for i in pj]
                        dj = text3
                        dj = dj.split(' ')
                        dj = [int(i) for i in dj]
                        #Thuật toán xử lý WSPT
                        thuat_toan_SPT_d(n,pj,dj)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >525 and pygame.mouse.get_pos()[1] >400:
                        if pygame.mouse.get_pos()[0] <625 and pygame.mouse.get_pos()[1] <450:
                            chaySPT_d()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        chaySPT_d()
        except:
            Mbox("Ôi không", 'Nhập sai đầu vào rồi', 5)
        screen.fill(BG)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(400, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        txt_surface2 = font.render(text2, True, color2)
        width2 = max(400, txt_surface2.get_width()+10)
        input_box2.w = width2
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        pygame.draw.rect(screen, color2, input_box2, 2)

        txt_surface3 = font.render(text3, True, color3)
        width3 = max(400, txt_surface3.get_width()+10)
        input_box3.w = width3
        screen.blit(txt_surface3, (input_box3.x+5, input_box3.y+5))
        pygame.draw.rect(screen, color3, input_box3, 2)

        # Viết tiêu đề

        draw_text('SPT_d', fontnho,RED, screen, 25, 10)
        draw_text(("Nhập số lượng công việc: "), fontnho, BLACK, screen, 25, 50)
        draw_text(("Nhập thời gian hoàn thành từng công việc"), fontnho, BLACK, screen, 25, 150)
        draw_text(("(cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 170)

        draw_text(("Nhập trọng số từng công việc"), fontnho, BLACK, screen, 25, 250)
        draw_text(("(cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 270)

        pygame.draw.rect(screen, PINK, (525,400,100,50))


        
        pygame.display.update()
        mainClock.tick(60)

def game_EDD():
    # Điều chỉnh đầu vào hình ô vuông
    #100, 100 (2 vrí đầu là x,y ) 
    # Cái cuối là chiều rộng
    input_box = pygame.Rect(450 ,50, 140, 50)
    input_box2 = pygame.Rect(450, 150, 140, 50)
    input_box3 = pygame.Rect(450, 250, 140, 50)    
    color_inactive = (255,159,156)
    color_active = (255,8,0)
    color = color_inactive
    color2 = color_inactive
    color3 = color_inactive
    active = False
    active2 = False
    active3 = False
    text = ''
    text2 = ''
    text3 = ''
    done = False
    running = True

    while running:
        screen.fill(BG)
        

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box2.collidepoint(event.pos):
                        active2 = not active2
                    else:
                        active2 = False
                    color2 = color_active if active2 else color_inactive

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box3.collidepoint(event.pos):
                        active3 = not active3
                    else:
                        active3 = False
                    color3 = color_active if active3 else color_inactive

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        elif event.key == pygame.K_DELETE:
                            text = ''
                        else:
                            text += event.unicode
                    if active2:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text2 = text2[:-1]
                        else:
                            text2 += event.unicode
                    if active3:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text3 = text3[:-1]
                        else:
                            text3 += event.unicode

                    def chayEDD():
                        n = int(text)

                        pj = text2
                        pj = pj.split(' ')
                        pj = [int(i) for i in pj]
                        dj = text3
                        dj = dj.split(' ')
                        dj = [int(i) for i in dj]
                        #Thuật toán xử lý WSPT
                        thuat_toan_EDD(n,pj,dj)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >525 and pygame.mouse.get_pos()[1] >400:
                        if pygame.mouse.get_pos()[0] <625 and pygame.mouse.get_pos()[1] <450:
                            chayEDD()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        chayEDD()
        except:
            Mbox("Ôi không", 'Nhập sai đầu vào rồi', 5)
        screen.fill(BG)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(400, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        txt_surface2 = font.render(text2, True, color2)
        width2 = max(400, txt_surface2.get_width()+10)
        input_box2.w = width2
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        pygame.draw.rect(screen, color2, input_box2, 2)

        txt_surface3 = font.render(text3, True, color3)
        width3 = max(400, txt_surface3.get_width()+10)
        input_box3.w = width3
        screen.blit(txt_surface3, (input_box3.x+5, input_box3.y+5))
        pygame.draw.rect(screen, color3, input_box3, 2)

        # Viết tiêu đề

        draw_text('EDD', fontnho,RED, screen, 25, 10)
        draw_text(("Nhập số lượng công việc: "), fontnho, BLACK, screen, 25, 50)
        draw_text(("Nhập thời gian hoàn thành từng công việc"), fontnho, BLACK, screen, 25, 150)
        draw_text(("(cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 170)

        draw_text(("Nhập trọng số từng công việc"), fontnho, BLACK, screen, 25, 250)
        draw_text(("(cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 270)

        pygame.draw.rect(screen, PINK, (525,400,100,50))


        
        pygame.display.update()
        mainClock.tick(60)

def game_LPT():
    # Điều chỉnh đầu vào hình ô vuông
    #100, 100 (2 vrí đầu là x,y ) 
    # Cái cuối là chiều rộng
    input_box = pygame.Rect(450 ,50, 140, 50)
    input_box2 = pygame.Rect(450, 150, 140, 50)
    input_box3 = pygame.Rect(450, 250, 140, 50)    
    color_inactive = (255,159,156)
    color_active = (255,8,0)
    color = color_inactive
    color2 = color_inactive
    color3 = color_inactive
    active = False
    active2 = False
    active3 = False
    text = ''
    text2 = ''
    text3 = ''
    done = False
    running = True

    while running:
        screen.fill(BG)
        

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box2.collidepoint(event.pos):
                        active2 = not active2
                    else:
                        active2 = False
                    color2 = color_active if active2 else color_inactive

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box3.collidepoint(event.pos):
                        active3 = not active3
                    else:
                        active3 = False
                    color3 = color_active if active3 else color_inactive

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        elif event.key == pygame.K_DELETE:
                            text = ''
                        else:
                            text += event.unicode
                    if active2:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text2 = text2[:-1]
                        else:
                            text2 += event.unicode
                    if active3:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text3 = text3[:-1]
                        else:
                            text3 += event.unicode

                    def chayLPT():
                        n = int(text)

                        pj = text2
                        pj = pj.split(' ')
                        pj = [int(i) for i in pj]
                        dj = text3
                        dj = dj.split(' ')
                        dj = [int(i) for i in dj]
                        #Thuật toán xử lý WSPT
                        thuat_toan_LPT(n,pj,dj)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >525 and pygame.mouse.get_pos()[1] >400:
                        if pygame.mouse.get_pos()[0] <625 and pygame.mouse.get_pos()[1] <450:
                            chayLPT()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        chayLPT()
        except:
            Mbox("Ôi không", 'Nhập sai đầu vào rồi', 5)
        screen.fill(BG)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(400, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        txt_surface2 = font.render(text2, True, color2)
        width2 = max(400, txt_surface2.get_width()+10)
        input_box2.w = width2
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        pygame.draw.rect(screen, color2, input_box2, 2)

        txt_surface3 = font.render(text3, True, color3)
        width3 = max(400, txt_surface3.get_width()+10)
        input_box3.w = width3
        screen.blit(txt_surface3, (input_box3.x+5, input_box3.y+5))
        pygame.draw.rect(screen, color3, input_box3, 2)

        # Viết tiêu đề

        draw_text('LPT', fontnho,RED, screen, 25, 10)
        draw_text(("Nhập số lượng công việc: "), fontnho, BLACK, screen, 25, 50)
        draw_text(("Nhập thời gian hoàn thành từng công việc"), fontnho, BLACK, screen, 25, 150)
        draw_text(("(cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 170)

        draw_text(("Nhập trọng số từng công việc"), fontnho, BLACK, screen, 25, 250)
        draw_text(("(cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 270)

        pygame.draw.rect(screen, PINK, (525,400,100,50))


        
        pygame.display.update()
        mainClock.tick(60)

main_menu()