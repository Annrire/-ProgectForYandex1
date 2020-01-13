import pygame
import csv
from moviepy.editor import VideoFileClip 
pygame.init()

clip = VideoFileClip('66918_movie.mp4')
clip_resized = clip.resize((1024, 768))
clip_resized.preview()

class Board:
    # создание поля
    def __init__(self, width, height, cell_size = 30, left = 10, top = 10):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        # значения по умолчанию
        self.left = top
        self.top = left
        self.cell_size = cell_size

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
    
    def render(self, sc):
        global listt
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(sc, (0, 0, 0), (self.left + i * self.cell_size, self.top + j * self.cell_size, self.cell_size, self.cell_size), 1)
                listt.append([i, j])

def score1():
    y11 = 184 #x11 = 324 and x22 = 740
    font = pygame.font.Font(None, 50)
    text = font.render(scores[0][0], 1, (0, 0, 0))
    sc.blit(text, [324, y11])
    font = pygame.font.Font(None, 50)
    text1 = font.render(str(scores[0][1]), 1, (0, 0, 0))     
    sc.blit(text1, [740, y11])
def score2():
    y11 = 184 + 62 #x11 = 324 and x22 = 740
    font = pygame.font.Font(None, 50)
    text = font.render(scores[1][0], 1, (0, 0, 0))
    sc.blit(text, [324, y11])
    font = pygame.font.Font(None, 50)
    text1 = font.render(str(scores[1][1]), 1, (0, 0, 0))     
    sc.blit(text1, [740, y11])
def score3():
    y11 = 184 + 62 * 2 #x11 = 324 and x22 = 740
    font = pygame.font.Font(None, 50)
    text = font.render(scores[2][0], 1, (0, 0, 0))
    sc.blit(text, [324, y11])
    font = pygame.font.Font(None, 50)
    text1 = font.render(str(scores[2][1]), 1, (0, 0, 0))     
    sc.blit(text1, [740, y11]) 
def score4():
    y11 = 184 + 62 * 3 #x11 = 324 and x22 = 740
    font = pygame.font.Font(None, 50)
    text = font.render(scores[3][0], 1, (0, 0, 0))
    sc.blit(text, [324, y11])
    font = pygame.font.Font(None, 50)
    text1 = font.render(str(scores[3][1]), 1, (0, 0, 0))     
    sc.blit(text1, [740, y11])
def score5():
    y11 = 184 + 62 * 4 #x11 = 324 and x22 = 740
    font = pygame.font.Font(None, 50)
    text = font.render(scores[4][0], 1, (0, 0, 0))
    sc.blit(text, [324, y11])
    font = pygame.font.Font(None, 50)
    text1 = font.render(str(scores[4][1]), 1, (0, 0, 0))     
    sc.blit(text1, [740, y11])
def score6():
    y11 = 184 + 62 * 5 #x11 = 324 and x22 = 740
    font = pygame.font.Font(None, 50)
    text = font.render(scores[5][0], 1, (0, 0, 0))
    sc.blit(text, [324, y11])
    font = pygame.font.Font(None, 50)
    text1 = font.render(str(scores[5][1]), 1, (0, 0, 0))     
    sc.blit(text1, [740, y11])
def score7():
    y11 = 184 + 62 * 6 #x11 = 324 and x22 = 740
    font = pygame.font.Font(None, 50)
    text = font.render(scores[6][0], 1, (0, 0, 0))
    sc.blit(text, [324, y11])
    font = pygame.font.Font(None, 50)
    text1 = font.render(str(scores[6][1]), 1, (0, 0, 0))     
    sc.blit(text1, [740, y11]) 
def score8():
    y11 = 184 + 62 * 7 #x11 = 324 and x22 = 740
    font = pygame.font.Font(None, 50)
    text = font.render(scores[7][0], 1, (0, 0, 0))
    sc.blit(text, [324, y11])
    font = pygame.font.Font(None, 50)
    text1 = font.render(str(scores[7][1]), 1, (0, 0, 0))     
    sc.blit(text1, [740, y11]) 


pygame.display.set_caption('Добро пожаловать в игру!') 
sc = pygame.display.set_mode((1024, 768))
sc.fill((255, 0, 0))
background_position = [0, 0]
background_image = pygame.image.load("начало.gif").convert()
sc.blit(background_image, background_position)
y1 = 0
x1 = 0
shag = 0
y11 = 0
step = 0
pygame.display.update()
running = True
start = False
record = False
game = True
startgame = False
dora1 = False
vash_chet = False
caracter = 1
schet = 0
kolgames = []
rightans = []
name = False
start_game = False 
dora2 = False
scores = []
font1 = pygame.font.Font(None, 150)
input_box = pygame.Rect(100, 300, 400, 100)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text1 = ''
names = []


path = "records1.csv"
with open(path) as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for index, row in enumerate(reader):
        if len(row) != 0:
            scores.append(row)


while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                running = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos        
                start = True
                image = pygame.image.load("arrow.png").convert_alpha()
                sc.blit(background_image, background_position)
                pygame.mouse.set_visible(False)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x1, y1 = event.pos
        background_position = [0, 0]
        background_image = pygame.image.load("начало.gif").convert()
        sc.blit(background_image, background_position)
        if x1 <= 750 and x1 >= 281:
            if y1 <= 451 and y1 >= 330:
                record = True 
                running = False
            if y1 <= 577 and y1 >= 459:
                running = False
                game = False
            if y1 <= 314 and y1 >= 199:
                running = False
                startgame = True
        if start:        
            dr1 = image.get_rect(bottomright=(x + 44, y + 40))
            sc.blit(image, dr1)
        
        pygame.display.flip()
 
 
    while record: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                record = False 
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos        
                start = True
                image = pygame.image.load("arrow.png").convert_alpha()
                sc.blit(background_image, background_position)
                pygame.mouse.set_visible(False)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x1, y1 = event.pos
                    # +62 по y1
        if x1 >= 425 and x1 <= 556 and y1 <= 700 and y1 >= 666:
            running = True        
            record = False 
        background_position = [0, 0]
        background_image = pygame.image.load("рекорды.gif").convert()
        sc.blit(background_image, background_position)
        scores.sort(key=lambda x: x[1], reverse=True)        
        for i in range(1):
            if len(scores) == 1:
                score1()
            if len(scores) == 2:
                score1()
                score2()
            if len(scores) == 3:
                score1()
                score2()
                score3()
            if len(scores) == 4:
                score1()
                score2()
                score3()
                score4()
            if len(scores) == 5:
                score1()
                score2()
                score3()
                score4()
                score5()
            if len(scores) == 6:
                score1()
                score2()
                score3()
                score4()
                score5()
                score6()
            if len(scores) == 7:
                score1()
                score2()
                score3()
                score4()
                score5()
                score6()
                score7()
            if len(scores) >= 8:
                score1()
                score2()
                score3()
                score4()
                score5()
                score6()
                score7()
                score8()
        if start:
            dr1 = image.get_rect(bottomright=(x + 44, y + 40))
            sc.blit(image, dr1)
            
        pygame.display.flip()
        
        
    while startgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                startgame = False 
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos        
                start = True
                image = pygame.image.load("arrow.png").convert_alpha()
                sc.blit(background_image, background_position)
                pygame.mouse.set_visible(False)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x1, y1 = event.pos
        background_position = [0, 0]
        background_image = pygame.image.load("choose.gif").convert()
        sc.blit(background_image, background_position)
        if x1 >= 703 and x1 <= 893 and y1 >= 338 and y1 <= 414:
            caracter += 1
            x1 = 0
        if x1 >= 131 and x1 <= 324 and y1 >= 342 and y1 <= 422:
            caracter -= 1
            x1 = 0
        if x1 >= 376 and x1 <= 678 and y1 >= 645 and y1 <= 698:
            start_game = True
            startgame = False
        if caracter % 3 == 1:
            caracter_surf = pygame.image.load("dora.gif").convert()
            sc.blit(caracter_surf, (364, 210))
        if caracter % 3 == 2:
            caracter_surf = pygame.image.load("monkey.gif").convert()
            sc.blit(caracter_surf, (340, 210))
        if caracter % 3 == 0:
            caracter_surf = pygame.image.load("fox.gif").convert()
            sc.blit(caracter_surf, (364, 290))
        if start:
            dr1 = image.get_rect(bottomright=(x + 44, y + 40))
            sc.blit(image, dr1)
            # выбрать: х от 376 до 678, у от 645 до 698
        pygame.display.flip()
        
        
    while start_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                start_game = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos        
                start = True
                image = pygame.image.load("arrow.png").convert_alpha()
                sc.blit(background_image, background_position)
                pygame.mouse.set_visible(False)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x1, y1 = event.pos
                    
                    print(x1, 'ььь', y1)
                    
        background_position = [0, 0]
        background_image = pygame.image.load("back2.jpg").convert()
        sc.blit(background_image, background_position)
        exit_surf = pygame.image.load("exit.gif").convert()
        sc.blit(exit_surf, (760, 673))
        tap1_surf = pygame.image.load("tap1.gif").convert()
        sc.blit(tap1_surf, (117, 461))    
        tap2_surf = pygame.image.load("tap2.gif").convert()
        sc.blit(tap2_surf, (403, 461))    
        tap3_surf = pygame.image.load("tap3.gif").convert()
        sc.blit(tap3_surf, (687, 456))
        
        if len(str(schet)) == 1:
            font = pygame.font.Font(None, 130)
            text = font.render(str(schet), True, (0, 0, 0))
            sc.blit(text, [765, 134])
        if len(str(schet)) == 2:
            font = pygame.font.Font(None, 130)
            text = font.render(str(schet), True, (0, 0, 0))
            sc.blit(text, [740, 134])   
        if len(str(schet)) == 3:
            font = pygame.font.Font(None, 130)
            text = font.render(str(schet), True, (0, 0, 0))
            sc.blit(text, [710, 134])        
        if caracter % 3 == 1:
            if x1 >= 177 and x1 <= 226 and y1 >= 481 and y1 <= 623:
                if not 'dora1' in kolgames:
                    start_game = False 
                    dora1 = True
            if x1 >= 442 and x1 <= 541 and y1 >= 490 and y1 <= 610:
                if 'dora1' in kolgames and not 'dora2' in kolgames:
                    start_game = False 
                    dora2 = True
        if x1 >= 778 and x1 <= 918 and y1 >= 683 and y1 <= 756:
            # соxранить результaт
            if len(kolgames) == 0:
                kolgames.append('d')
                kolgames.append('d')
                kolgames.append('d')
            if len(kolgames) == 1:
                kolgames.append('d')
                kolgames.append('d')
            if len(kolgames) == 2:
                kolgames.append('d')
            vash_chet = True
            start_game = False
        if caracter % 3 == 1:
            caracter_surf = pygame.image.load("dora.gif").convert()
            sc.blit(caracter_surf, (60, 20))
        if caracter % 3 == 2:
            caracter_surf = pygame.image.load("monkey.gif").convert()
            sc.blit(caracter_surf, (30, 40))
        if caracter % 3 == 0:
            caracter_surf = pygame.image.load("fox.gif").convert()
            sc.blit(caracter_surf, (30, 110))
        if start:
            dr1 = image.get_rect(bottomright=(x + 44, y + 40))
            sc.blit(image, dr1)
        pygame.display.flip()
        
        
    while dora1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                dora1 = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos        
                start = True
                image = pygame.image.load("arrow.png").convert_alpha()
                sc.blit(background_image, background_position)
                pygame.mouse.set_visible(False)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x1, y1 = event.pos
                    if x1 >= 127 and x1 <= 366 and y1 >= 516 and y1 <= 636:
                        step += 1
                    if x1 >= 395 and x1 <= 632 and y1 >= 515 and y1 <= 636:
                        step += 1
                    if x1 >= 662 and x1 <= 902 and y1 >= 515 and y1 <= 636:
                        step += 1
                    if x1 >= 738 and x1 <= 944 and y1 >= 652 and y1 <= 693:
                        step += 1
        if step == 0:
            background_position = [0, 0]
            background_image = pygame.image.load("dora11.gif").convert()
            sc.blit(background_image, background_position)
            shag = 1
        if step == 2:
            background_position = [0, 0]
            background_image = pygame.image.load("dora12.gif").convert()
            sc.blit(background_image, background_position) 
            shag = 2
        if step == 4:
            background_position = [0, 0]
            background_image = pygame.image.load("dora13.gif").convert()
            sc.blit(background_image, background_position)
            shag = 3
        if step == 6:
            background_p = [0, 0]
            background_image = pygame.image.load("dora14.gif").convert()
            sc.blit(background_image, background_position)   
            shag = 4
        if step == 8:
            background_position = [0, 0]
            background_image = pygame.image.load("dora15.gif").convert()
            sc.blit(background_image, background_position)
            shag = 5
        if step % 2 == 1:
            font = pygame.font.Font(None, 100)
            text = font.render('далее', True, (0, 0, 0))
            sc.blit(text, [730, 630])
            if shag == 1 or shag == 3 or shag == 5:
                if x1 >= 127 and x1 <= 366 and y1 >= 516 and y1 <= 636:
                    if not 'dora11' in rightans and shag == 1:
                        rightans.append('dora11')
                        rightans.append('dora11')
                    if not 'dora13' in rightans and shag == 3:
                        rightans.append('dora13')
                        rightans.append('dora13')
                    if not 'dora15' in rightans and shag == 5:
                        rightans.append('dora15')
                        rightans.append('dora15')
                    background_p = [x1 - 60, y1 - 110]
                    background_i = pygame.image.load("Check.gif").convert()
                    sc.blit(background_i, background_p)
                if x1 >= 395 and x1 <= 632 and y1 >= 515 and y1 <= 636:
                    background_p = [x1 - 45, y1 - 50]
                    background_i = pygame.image.load("none.gif").convert()
                    sc.blit(background_i, background_p) 
                if x1 >= 662 and x1 <= 902 and y1 >= 515 and y1 <= 636:
                    background_p = [x1 - 45, y1 - 50]
                    background_i = pygame.image.load("none.gif").convert()
                    sc.blit(background_i, background_p)                     
            if shag == 4:
                if x1 >= 395 and x1 <= 632 and y1 >= 515 and y1 <= 636:
                    if not 'dora14' in rightans:
                        rightans.append('dora14')
                        rightans.append('dora14')
                    background_p = [x1 - 60, y1 - 110]
                    background_i = pygame.image.load("Check.gif").convert()
                    sc.blit(background_i, background_p)
                if x1 >= 127 and x1 <= 366 and y1 >= 516 and y1 <= 636:
                    background_p = [x1 - 45, y1 - 50]
                    background_i = pygame.image.load("none.gif").convert()
                    sc.blit(background_i, background_p)         
                if x1 >= 662 and x1 <= 902 and y1 >= 515 and y1 <= 636:
                    background_p = [x1 - 45, y1 - 50]
                    background_i = pygame.image.load("none.gif").convert()
                    sc.blit(background_i, background_p)                          
            if shag == 2:
                if x1 >= 662 and x1 <= 902 and y1 >= 515 and y1 <= 636:
                    if not 'dora12' in rightans:
                        rightans.append('dora12')
                        rightans.append('dora12')
                    background_p = [x1 - 60, y1 - 110]
                    background_i = pygame.image.load("Check.gif").convert()
                    sc.blit(background_i, background_p)
                if x1 >= 127 and x1 <= 366 and y1 >= 516 and y1 <= 636:
                    background_p = [x1 - 45, y1 - 50]
                    background_i = pygame.image.load("none.gif").convert()
                    sc.blit(background_i, background_p) 
                if x1 >= 395 and x1 <= 632 and y1 >= 515 and y1 <= 636:
                    background_p = [x1 - 45, y1 - 50]
                    background_i = pygame.image.load("none.gif").convert()
                    sc.blit(background_i, background_p)      
        if not 'dora1' in kolgames:
            kolgames.append('dora1')
        if step == 10:
            dora1 = False
            vash_chet = True
        if start:
            dr1 = image.get_rect(bottomright=(x + 44, y + 40))
            sc.blit(image, dr1)
        pygame.display.flip()
        
    
    while dora2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                dora2 = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos        
                start = True
                image = pygame.image.load("arrow.png").convert_alpha()
                sc.blit(background_image, background_position)
                pygame.mouse.set_visible(False)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x1, y1 = event.pos
                    print(x1, 'qqq', y1)
        b1 = 8
        b2 = 8
        board = Board(b1, b2)
        a1 = 500
        a2 = 224
        a3 = 41
        board.set_view(a1, a2, a3)
        listt = []
        running1 = True    
        background_position = [0, 0]
        background_image = pygame.image.load("dora2.gif").convert()
        sc.blit(background_image, background_position)
        board.render(sc)
        
        if not 'dora2' in kolgames:
            kolgames.append('dora2')        
        if x1 >= 698 and x1 <= 915 and y1 >= 621 and y1 <= 667:
            dora2 = False
            vash_chet = True        
        if start:
            dr1 = image.get_rect(bottomright=(x + 44, y + 40))
            sc.blit(image, dr1)
        pygame.display.flip()
        
        
    while vash_chet:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                vash_chet = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos        
                start = True
                image = pygame.image.load("arrow.png").convert_alpha()
                sc.blit(background_image, background_position)
                pygame.mouse.set_visible(False)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x1, y1 = event.pos
        schet = len(rightans) * 10           
        background_position = [0, 0]
        background_image = pygame.image.load("vash_chet.jpg").convert()
        sc.blit(background_image, background_position)
        
        if x1 >= 409 and x1 <= 616 and y1 >= 603 and y1 <= 650:
            vash_chet = False
            if len(kolgames) != 3:
                start_game = True
            else:
                name = True
        if schet == 0:
            font = pygame.font.Font(None, 400)
            text = font.render(str(schet), True, (0, 0, 0))
            sc.blit(text, [435, 327])
        if schet <= 90 and schet != 0:
            font = pygame.font.Font(None, 400)
            text = font.render(str(schet), True, (0, 0, 0))
            sc.blit(text, [380, 327])   
        if schet <= 300 and schet >= 100:
            font = pygame.font.Font(None, 400)
            text = font.render(str(schet), True, (0, 0, 0))  
            sc.blit(text, [300, 327])   
        if start:
            dr1 = image.get_rect(bottomright=(x + 44, y + 40))
            sc.blit(image, dr1)
        pygame.display.flip()
        
        
    while name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                name = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos        
                start = True
                image = pygame.image.load("arrow.png").convert_alpha()
                sc.blit(background_image, background_position)
                pygame.mouse.set_visible(False)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x1, y1 = event.pos   
                    print(x1, y1)
    # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
        # Toggle the active variable.
                    active = not active
                else:
                    active = False
    #  Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        text1 = text1[:-1]
                    else:
                        text1 += event.unicode    
        
        if not text1 in names:
            names.append(text1)
        background_position = [0, 0]
        background_image = pygame.image.load("name.gif").convert()
        sc.blit(background_image, background_position)
        txt_surface = font1.render(text1, True, color)
        width = max(800, txt_surface.get_width()+10)
        input_box.w = width
        sc.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(sc, color, input_box, 2)        
        if len(text1) != 0:
            if x1 >= 181 and x1 <= 859 and y1 >= 640 and y1 <= 689:
                if not text1 in names:
                    names.append(text1)
                game = False
                name = False
        if start:
            dr1 = image.get_rect(bottomright=(x + 44, y + 40))
            sc.blit(image, dr1)
        pygame.display.flip()
        
        
pygame.quit()

list1 = text1
list2 = len(rightans) * 10
data = []
data.append([list1, list2])
if text1 != '':
    with open(path, "a") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)