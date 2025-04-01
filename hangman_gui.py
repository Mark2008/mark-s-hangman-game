import pygame
import random
import string
import time

pygame.init()
scr = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True

hangmans = []
for i in range(9):
    hangmans.append(pygame.image.load('assets/hangman'+str(i)+'.png'))
font = pygame.font.Font('assets/Bungee/Bungee-Regular.ttf', size=24)

BLACK = (0,0,0)


# game
file = open('listofprogramminglanguage.txt', 'r')
wordlist = list(map(lambda x: x.rstrip(), file))
file.close()

selected = random.choice(wordlist).lower()
guess = ['_' for _ in range(len(selected))]
life = 8
history = list()

charset = string.ascii_lowercase
clear = False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed()
    for k in charset:
        if key[pygame.key.key_code(k)]:
            if k in history: continue
            history.append(k)
            
            if k in selected:
                for i in range(len(guess)):
                    if selected[i] == k:
                        guess[i] = k

                flag = True
                for i in range(len(selected)):
                    if guess[i] != selected[i]:
                        flag = False
                        break

                if flag:
                    clear = True
            else:
                life -= 1
    

    scr.fill((255,255,255))
    scr.blit(hangmans[life], (0,0))

    scr.blit(font.render('Legend hangman game', True, BLACK), (20,20))

    for idx, character in enumerate(guess):
        scr.blit(font.render(character, True, BLACK), (20+30*idx, 400))

    for idx, character in enumerate(history):
        scr.blit(font.render(character, True, BLACK), (20+30*idx, 430))

    if life <= 0:
        scr.blit(font.render('game over!', True, BLACK),(350,100))
        scr.blit(font.render(f'it was {selected}', True, (100,100,100)), (350, 130))
        pygame.display.update()
        time.sleep(3)
        running = False

    if clear:
        scr.blit(font.render('game clear!', True, BLACK), (350,100))
        pygame.display.update()
        time.sleep(3)
        running = False


    dt = clock.tick(50)
    pygame.display.update()

pygame.quit()