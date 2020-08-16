import pygame,sys
import random

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Hangman")
secret_words_list = ["KNOWLEDGE","EDUCATION", "ENCYCLOPEDIA","MAN","TIGER","HEN","HEALTH","RECOMMENDATION","WEALTH","FLIGHT","CONSIDERATION","LANGUAGE","WONDERFUL","SUCCESSFULL"]  # only uppercaase here]
indexused_in_secret_words_list = []
indexused_in_secret_words_list.append(random.randrange(0, len(secret_words_list), 1))
secret = secret_words_list[indexused_in_secret_words_list[0]]


class word(object):
    y = 530
    x = 60
    word_index = []
    gamewin_counter = 0

    def __init__(self, start_i):
        self.startx = word.x + start_i * 35
        self.starty = word.y
        self.endx = self.startx + 28
        self.endy = word.y

    def drawletter_space(self, indexno):
        pygame.draw.line(win, (255, 255, 255), (self.startx, self.starty), (self.endx, self.endy), 3)
        # drawing letters if they are initial random letters
        if indexno in word.word_index:
            text = font.render(secret[indexno], 1, (255, 0, 0))
            win.blit(text, (self.startx + 8, self.starty - 20))
            word.gamewin_counter += 1
            return  # to stop blue letter being drawn over red
        # drawing user input letters or characters
        elif secret[indexno] in userinputchars:
            text = font.render(secret[indexno], 1, (0, 0, 255))
            win.blit(text, (self.startx + 8, self.starty - 20))
            word.gamewin_counter += 1

    @classmethod
    def randomindex(cls):
        n = len(secret)
        if 3 <= n < 5:
            y = 1
        elif 5 <= n < 9:
            y = 2
        elif n >= 9:
            y = 3
        while True:
            temp = random.randrange(0, n, 1)
            if temp not in cls.word_index:
                cls.word_index.append(temp)

            if len(cls.word_index) == y:
                break



class Text(object):
    def __init__(self, displaytext, x, y, COLOR):
        self.displaytext = displaytext
        self.x = x
        self.y = y
        self.COLOR = COLOR

    def drawtext(self,value):
        text = font.render(self.displaytext+str(value), 1, self.COLOR)
        win.blit(text, (self.x, self.y))


def drawman(lives):
    global running
    x = 500
    y = 80
    pygame.draw.line(win, (0, 250, 0), (x - 100 - 50, y + 300), (x - 100 + 50, y + 300), 3)
    pygame.draw.line(win, (0, 250, 0), (x - 100, y - 60), (x - 100, y + 300), 3)
    pygame.draw.line(win, (0, 250, 0), (x - 100, y - 60), (x, y - 60), 3)
    pygame.draw.line(win, (0, 250, 0), (x, y - 60), (x, y - 40), 3)
    if lives == 6:
        return
    pygame.draw.circle(win, (0, 250, 0), (x, y), 40, 3)
    if lives == 5:
        return
    pygame.draw.line(win, (0, 250, 0), (x, y + 40), (x, y + 200), 3)
    if lives == 4:
        return
    pygame.draw.line(win, (0, 250, 0), (x, y + 80), (x - 50, y + 110), 3)
    if lives == 3:
        return
    pygame.draw.line(win, (0, 250, 0), (x, y + 80), (x + 50, y + 110), 3)
    if lives == 2:
        return
    pygame.draw.line(win, (0, 250, 0), (x, y + 200), (x - 50, y + 230), 3)
    if lives == 1:
        return

    # if lives == 0
    pygame.draw.line(win, (0, 250, 0), (x, y + 200), (x + 50, y + 230), 3)
    pygame.display.update()

    pygame.time.delay(1000)
    win.fill((0, 0, 0))
    text = font.render(f'GAME OVER        Your score: {score}', 1, (255, 0, 0))
    win.blit(text, (300 - text.get_width() // 2, 300))
    pygame.display.update()
    i = 1000
    for i in range(i):
        pygame.time.delay(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        running = False


def newgame():
    global userinputchars
    global letters_space
    global secret
    userinputchars = []
    letters_space = []
    word.word_index = []
    word.gamewin_counter = 0

    # changing secret word:
    while True:
        x = random.randrange(0, len(secret_words_list), 1)
        if x not in indexused_in_secret_words_list:
            indexused_in_secret_words_list.append(x)
            secret = secret_words_list[x]
            break
        if len(indexused_in_secret_words_list) == len(secret_words_list):
            print("GAME WON!!!")
            pygame.quit()
            sys.exit()
    word.randomindex()  # keep it below assigning secret value as this method uses that secret value



# main while loop variables
running = True
font = pygame.font.SysFont('comicsans', 30, True, True)
letters_space = []
userinputchars = []
lives = 6
word.randomindex()  # may be in while loop
score = 0
clock = pygame.time.Clock()
score_text = Text(f'Score: ',10,10,(200,180,20))
lives_text = Text(f'Lives: ',150,10,(100,100,240))

check_list = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h,
              pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p,
              pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x,
              pygame.K_y, pygame.K_z]

while running:
    pygame.mouse.set_visible(1)
    clock.tick(30)
    win.fill((0, 0, 0))
    score_text.drawtext(score)
    lives_text.drawtext(lives)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in check_list:
                number = check_list.index(event.key) + 65  # to change to ascii value
                if chr(number) not in secret:
                    lives -= 1
                    score -= 2
                else:
                    userinputchars.append(chr(number))

    for i in range(len(secret)):
        letters_space.append(word(i))
    word.gamewin_counter = 0
    for i in range(len(secret)):
        letters_space[i].drawletter_space(i)

    drawman(lives)
    pygame.display.update()
    pygame.time.delay(200)
    if word.gamewin_counter == len(secret):
        newgame()
        score += 10
pygame.quit()
