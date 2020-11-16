import pygame
import random
from pygame import mixer
import pickle
# initialize pygame
pygame.init()
# clock
time = 0
clock = pygame.time.Clock()
# window
screen = pygame.display.set_mode((640, 640))
# Title and Icon
pygame.display.set_caption("Tetris Time")
icon = pygame.image.load('images\\O.png')
pygame.display.set_icon(icon)
# images
background = pygame.image.load('images\\Board.png')
tetI = pygame.image.load('images\\I.png')
tetJ = pygame.image.load('images\\J.png')
tetL = pygame.image.load('images\\L.png')
tetO = pygame.image.load('images\\O.png')
tet = pygame.image.load('images\\S.png')
tetT = pygame.image.load('images\\T.png')
tetZ = pygame.image.load('images\\Z.png')
tetIp = pygame.image.load('images\\ip.png')
tetJp = pygame.image.load('images\\jp.png')
tetLp = pygame.image.load('images\\lp.png')
tetOp = pygame.image.load('images\\op.png')
tetSp = pygame.image.load('images\\sp.png')
tetTp = pygame.image.load('images\\tp.png')
tetZp = pygame.image.load('images\\zp.png')
# Text setup
overFont = pygame.font.Font('American Captain.otf', 32)
otherFont = pygame.font.Font('American Captain.otf', 16)
anotherFont = pygame.font.Font('American Captain.otf', 32)
#music setup
music = mixer.music.load('Tetris.mp3')
mixer.music.play(-1)
turn = mixer.Sound('Click.wav')
# Tetriminos tetX = x coordinate tetY = Y coordinate tetS = state(0 = qued, 1 = falling, 2 = fallen) tetC = color tetM = tetrimino part
tetX = []
tetY = []
tetS = []
tetC = []
tetM = []
pieces = []

def spawnp(tettot):
    piece = pieces[0]
    pieces.pop(0)
    pieces.append(random.randint(0, 6))
    if piece == 0:
        # I piece spawn
        for i in range(4):
            tetX.append(480)
            tetY.append(160 + (i * 16))
            tetS.append(1)
            tetC.append(tetIp)
            tettot += 1
            tetM.append(i)
    if piece == 1:
        # J piece spawn
        for i in range(3):
            tetX.append(464 + i * 16)
            tetY.append(160)
            tetS.append(1)
            tetC.append(tetJp)
            tettot += 1
            tetM.append(i)
        tetX.append(464)
        tetY.append(176)
        tetS.append(1)
        tetC.append(tetJp)
        tettot += 1
        tetM.append(3)
    if piece == 2:
        # L piece spawn
        for i in range(3):
            tetX.append(464 + i * 16)
            tetY.append(160)
            tetS.append(1)
            tetC.append(tetLp)
            tettot += 1
            tetM.append(i)
        tetX.append(496)
        tetY.append(176)
        tetS.append(1)
        tetC.append(tetLp)
        tettot += 1
        tetM.append(3)
    if piece == 3:
        # O piece spawn
        for i in range(2):
            tetX.append(464 + i * 16)
            tetY.append(160)
            tetS.append(1)
            tetC.append(tetOp)
            tettot += 1
            tetM.append(i)
        for i in range(2):
            tetX.append(464 + i * 16)
            tetY.append(176)
            tetS.append(1)
            tetC.append(tetOp)
            tettot += 1
            tetM.append(i+2)
    if piece == 4:
        # S piece spawn
        for i in range(2):
            tetX.append(480 + i * 16)
            tetY.append(160)
            tetS.append(1)
            tetC.append(tetSp)
            tettot += 1
            tetM.append(i)
        for i in range(2):
            tetX.append(464 + i * 16)
            tetY.append(176)
            tetS.append(1)
            tetC.append(tetSp)
            tettot += 1
            tetM.append(i+2)
    if piece == 5:
        # T piece spawn
        for i in range(3):
            tetX.append(464 + i * 16)
            tetY.append(176)
            tetS.append(1)
            tetC.append(tetTp)
            tettot += 1
            tetM.append(i)
        tetX.append(480)
        tetY.append(160)
        tetS.append(1)
        tetC.append(tetTp)
        tettot += 1
        tetM.append(3)
    if piece == 6:
        # Z piece spawn
        for i in range(2):
            tetX.append(464 + i * 16)
            tetY.append(160)
            tetS.append(1)
            tetC.append(tetZp)
            tettot += 1
            tetM.append(i)
        for i in range(2):
            tetX.append(480 + i * 16)
            tetY.append(176)
            tetS.append(1)
            tetC.append(tetZp)
            tettot += 1
            tetM.append(i+2)
    return tettot
# creates the piece


def drawp(skin, x, y):
    screen.blit(skin, (x, y))
# draws the existing pieces


def turnr(c, i, m, r):
    if c == tetIp:
        if r == 0:
            if m == 0:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 3:
                tetX[i] -= 32
                tetY[i] -= 32
        elif r == 1:
            if m == 0:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 3:
                tetX[i] += 32
                tetY[i] -= 32
        elif r == 2:
            if m == 0:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 3:
                tetX[i] += 32
                tetY[i] += 32
        elif r == 3:
            if m == 0:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 3:
                tetX[i] -= 32
                tetY[i] += 32
    elif c == tetLp:
        if r == 0:
            if m == 0:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 3:
                tetX[i] -= 32
        elif r == 1:
            if m == 0:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 3:
                tetY[i] -= 32
        elif r == 2:
            if m == 0:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 3:
                tetX[i] += 32
        elif r == 3:
            if m == 0:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 3:
                tetY[i] += 32
    elif c == tetJp:
        if r == 0:
            if m == 0:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 3:
                tetY[i] -= 32
        elif r == 1:
            if m == 0:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 3:
                tetX[i] += 32
        elif r == 2:
            if m == 0:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 3:
                tetY[i] += 32
        elif r == 3:
            if m == 0:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 3:
                tetX[i] -= 32
    elif c == tetSp:
        if r == 0:
            if m == 1:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 3:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 2:
                tetY[i] -= 32
        elif r == 1:
            if m == 1:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 3:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] += 32
        elif r == 2:
            if m == 1:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 3:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 2:
                tetY[i] += 32
        elif r == 3:
            if m == 1:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 3:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] -= 32
    elif c == tetTp:
        if r == 0:
            if m == 0:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 3:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] += 16
        elif r == 1:
            if m == 0:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 3:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] -= 16
        elif r == 2:
            if m == 0:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 3:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] -= 16
        elif r == 3:
            if m == 0:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 3:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] += 16
    elif c == tetZp:
        if r == 0:
            if m == 0:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 3:
                tetX[i] -= 32
        elif r == 1:
            if m == 0:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 3:
                tetY[i] -= 32
        elif r == 2:
            if m == 0:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 3:
                tetX[i] += 32
        elif r == 3:
            if m == 0:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 3:
                tetY[i] += 32
    return 1
# rotate right


def turnl(c, i, m, r):
    if c == tetIp:
        if r == 1:
            if m == 0:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 3:
                tetX[i] += 32
                tetY[i] += 32
        elif r == 2:
            if m == 0:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 3:
                tetX[i] -= 32
                tetY[i] += 32
        elif r == 3:
            if m == 0:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 3:
                tetX[i] -= 32
                tetY[i] -= 32
        elif r == 0:
            if m == 0:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 3:
                tetX[i] += 32
                tetY[i] -= 32
    elif c == tetLp:
        if r == 1:
            if m == 0:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 3:
                tetX[i] += 32
        elif r == 2:
            if m == 0:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 3:
                tetY[i] += 32
        elif r == 3:
            if m == 0:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 3:
                tetX[i] -= 32
        elif r == 0:
            if m == 0:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 3:
                tetY[i] -= 32
    elif c == tetJp:
        if r == 1:
            if m == 0:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 3:
                tetY[i] += 32
        elif r == 2:
            if m == 0:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 3:
                tetX[i] -= 32
        elif r == 3:
            if m == 0:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 3:
                tetY[i] -= 32
        elif r == 0:
            if m == 0:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 3:
                tetX[i] += 32
    elif c == tetSp:
        if r == 1:
            if m == 1:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 3:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 2:
                tetY[i] += 32
        elif r == 2:
            if m == 1:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 3:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] -= 32
        elif r == 3:
            if m == 1:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 3:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 2:
                tetY[i] -= 32
        elif r == 0:
            if m == 1:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 3:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] += 32
    elif c == tetTp:
        if r == 0:
            if m == 3:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 0:
                tetX[i] += 16
                tetY[i] += 16
        elif r == 1:
            if m == 3:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 0:
                tetX[i] -= 16
                tetY[i] += 16
        elif r == 2:
            if m == 3:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 0:
                tetX[i] -= 16
                tetY[i] -= 16
        elif r == 3:
            if m == 3:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 0:
                tetX[i] += 16
                tetY[i] -= 16
    elif c == tetZp:
        if r == 1:
            if m == 0:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 3:
                tetX[i] += 32
        elif r == 2:
            if m == 0:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] += 16
            elif m == 3:
                tetY[i] += 32
        elif r == 3:
            if m == 0:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 2:
                tetX[i] -= 16
                tetY[i] -= 16
            elif m == 3:
                tetX[i] -= 32
        elif r == 0:
            if m == 0:
                tetX[i] += 16
                tetY[i] += 16
            elif m == 2:
                tetX[i] += 16
                tetY[i] -= 16
            elif m == 3:
                tetY[i] -= 32
    return 1
# rotate left


def lineclear(h, tettot):
    for j in range(10):
        for i in range(tettot):
            if tetY[i] == h:
                del tetY[i]
                del tetX[i]
                del tetS[i]
                del tetM[i]
                del tetC[i]
                tettot -= 1
                break
    return tettot
# clears a line


def movedown(h, tettot):
    for i in range(tettot):
        if tetS[i] == 2:
            if tetY[i] < h:
                tetY[i] += 16
# moves all blocks above a cleared line down


def collide(i, y, tettot):
    # for y 0 = other blocks y 1 = floor
    # return 0 = in other block or under board, return 1 = on top of another block, return 2 = in free fall
    if y == 0:
        for ii in range(tettot):
            if (tetY[i] + 16 == tetY[ii] and tetS[ii] == 2) and (tetX[i] == tetX[ii]):
                return 1
            elif (tetY[i] == tetY[ii] and tetS[ii] == 2) and (tetX[i] == tetX[ii]):
                return 0
    elif y == 1:
        if tetY[i] == 464:
            return 1
        elif tetY[i] >= 464:
            return 0
    return 2
# floor and other block fall collision


def waiter(tettot):
    for ii in range(tettot):
        tetS[ii] = 2
# waits the table


def harddrop(tettot):
    brea = True
    fall = False
    while brea:
        for i in range(tettot):
            if tetS[i] == 1:
                if not collide(i, 0, tettot) == 2 or not collide(i, 1, tettot) == 2:
                    fall = False
                    brea = False
                    break
                else:
                    fall = True
        if fall:
            for j in range(tettot):
                if tetS[j] == 1:
                    tetY[j] += 16
# hardrops


def drawNext():
    for i in range(len(pieces)):
        if pieces[i] == 0:
            drawp(tetI, 576, 160 + (i * 80))
        elif pieces[i] == 1:
            drawp(tetJ, 576, 160 + (i * 80))
        elif pieces[i] == 2:
            drawp(tetL, 576, 160 + (i * 80))
        elif pieces[i] == 3:
            drawp(tetO, 576, 160 + (i * 80))
        elif pieces[i] == 4:
            drawp(tet, 576, 160 + (i * 80))
        elif pieces[i] == 5:
            drawp(tetT, 576, 160 + (i * 80))
        elif pieces[i] == 6:
            drawp(tetZ, 576, 160 + (i * 80))
# draws the upcoming pieces


def detright(tettot):
    for i in range(tettot):
        if tetS[i] == 1:
            for ii in range(tettot):
                if (tetX[i] + 16 == tetX[ii] and tetS[ii] == 2) and (tetY[i] == tetY[ii]):
                    return True
    return False
# det right block


def detleft(tettot):
    for i in range(tettot):
        if tetS[i] == 1:
            for ii in range(tettot):
                if (tetX[i] - 16 == tetX[ii] and tetS[ii] == 2) and (tetY[i] == tetY[ii]):
                    return True
    return False
# det left block


def moveright(tettot):
    for i in range(tettot):
        if tetS[i] == 1:
            tetX[i] += 16
# moves the falling piece right


def moveleft(tettot):
    for i in range(tettot):
        if tetS[i] == 1:
            tetX[i] -= 16
# moves the falling piece left


def main():
    # various variable initializations
    for i in range(4):
        pieces.append(random.randint(0,6))
    dt = 0
    moveRight = False
    moveLeft = False
    moveDown = False
    farRight = False
    frc = 0
    farLeft = False
    flc = 0
    needSpawn = True
    r = 0
    rc = 0
    lc = 0
    turnRight = False
    turnLeft = False
    # lineCount int var that isn't used until declared again
    tineCount = 0
    score = 0
    hscore = 0
    lcount = 0
    single = 0
    double = 0
    triple = 0
    tetris = 0
    running = True
    gaming = True
    wait = False
    tetTot = 0
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (400, 160))

        dt += clock.tick(10)
        if gaming:
            # player input
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g:
                        tetTot = spawnp(tetTot)
                    if event.key == pygame.K_d:
                        moveRight = True
                    if event.key == pygame.K_a:
                        moveLeft = True
                    if event.key == pygame.K_s:
                        moveDown = True
                    if event.key == pygame.K_UP:
                        turnRight = True
                    if event.key == pygame.K_DOWN:
                        turnLeft = True
                    if event.key == pygame.K_w:
                        harddrop(tetTot)
                        wait = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        moveRight = False
                    if event.key == pygame.K_a:
                        moveLeft = False
                    if event.key == pygame.K_s:
                        moveDown = False
                if event.type == pygame.QUIT:
                    running = False
            # move/rotate left or right
            if (moveRight and not farRight) and not detright(tetTot):
                moveright(tetTot)
            if (moveLeft and not farLeft) and not detleft(tetTot):
                moveleft(tetTot)
            for i in range(tetTot):
                if tetS[i] == 1:
                    if moveDown and not wait:
                        tetY[i] += 16
                    if turnRight:
                        if detright(tetTot) and detleft(tetTot):
                            turn.play()
                        else:
                            rc += turnr(tetC[i], i, tetM[i], r)
                            turn.play()
                            while detright(tetTot):
                                moveleft(tetTot)
                            while detleft(tetTot):
                                moveright(tetTot)
                    if turnLeft:
                        if detright(tetTot) and detleft(tetTot):
                            turn.play()
                        else:
                            lc += turnl(tetC[i], i, tetM[i], r)
                            turn.play()
                            while detright(tetTot):
                                tetX[i] -= 16
                            while detleft(tetTot):
                                tetX[i] += 16
            # rotation help
            for i in range(1):
                if rc == 4:
                    r += 1
                    rc = 0
                if lc == 4:
                    r -= 1
                    lc = 0
                if r == -1:
                    r = 3
                if r == 4:
                    r = 0
                turnRight = False
                turnLeft = False
            # walls floor and other block interaction
            for i in range(tetTot):
                if tetS[i] == 2 and tetY[i] < 160:
                    gaming = False
                if tetS[i] == 1:
                    # stops at fallen floor
                    check = True
                    h = True
                    while check:
                        for j in range(tetTot):
                            if tetS[j] == 1:
                                if collide(j, 0, tetTot) == 0 or collide(j, 1, tetTot) == 0:
                                    for ii in range(tetTot):
                                        if tetS[ii] == 1:
                                            tetY[ii] -= 16
                                    wait = True
                                    check = True
                                    h = False
                                    break
                        for j in range(tetTot):
                            if tetS[j] == 1:
                                if collide(j, 0, tetTot) == 1 or collide(j, 1, tetTot) == 1:
                                    wait = True
                                    check = False
                                    h = False
                                    break
                        if h:
                            wait = False
                            check = False
                    # left and right wall
                    if tetX[i] >= 560:
                        for ii in range(tetTot):
                            if tetS[ii] == 1:
                                tetX[ii] -= 16
                        farRight = True
                    else:
                        frc += 1
                        if frc >= 4:
                            farRight = False
                    if tetX[i] <= 384:
                        for ii in range(tetTot):
                            if tetS[ii] == 1:
                                tetX[ii] += 16
                        farLeft = True
                    else:
                        flc += 1
                        if flc >= 4:
                            farLeft = False
            # gravity
            gravity = True
            if (dt >= (2000-lcount*20) and dt >= 250) and not moveDown:
                for i in range(tetTot):
                    if tetS[i] == 1 and (not collide(i, 0, tetTot) == 2 or not collide(i, 1, tetTot) == 2):
                        print("ran, wait: " + str(wait))
                        if wait:
                            waiter(tetTot)
                            needSpawn = True
                            wait = False
                        else:
                            wait = True
                            gravity = False
                dt = 0
                if gravity:
                    for j in range(tetTot):
                        if tetS[j] == 1:
                            tetY[j] += 16
            elif dt >= (2000-lcount*20) and dt >= 250:
                dt = 0
                if wait:
                    waiter(tetTot)
                    needSpawn = True
                    wait = False
            # clears a line
            for i in range(20):
                h = i*16+160
                lineCount = 0
                for iii in range(10):
                    l = iii * 16 + 400
                    for ii in range(tetTot):
                        if (tetX[ii] == l and tetY[ii] == h) and tetS[ii] == 2:
                            lineCount += 1
                            if lineCount == 10:
                                tetTot = lineclear(h, tetTot)
                                movedown(h, tetTot)
                                tineCount += 1
                                break
            if tineCount == 1:
                score += 10
                lcount += 1
                single += 1
            elif tineCount == 2:
                score += 25
                lcount += 2
                double += 1
            elif tineCount == 3:
                score += 50
                lcount += 3
                triple += 1
            elif tineCount == 4:
                score += 100
                lcount += 4
                tetris += 1
            tineCount = 0
            # spawns a new block
            if needSpawn:
                tetTot = spawnp(tetTot)
                farLeft = False
                farRight = False
                needSpawn = False
                r = 0
        else:
            if hscore < score:
                hscore = score
                gameoverText = anotherFont.render("    New High Score!", True, (150, 255, 150))
                screen.blit(gameoverText, (32, 320))
                gameoverText = anotherFont.render("Press 'G' to try again!", True, (255, 100, 100))
                screen.blit(gameoverText, (32, 354))
            else:
                gameoverText = anotherFont.render("    Gameover loser!", True, (255, 100, 100))
                screen.blit(gameoverText, (32, 320))
                gameoverText = anotherFont.render("Press 'G' to try again!", True, (255, 100, 100))
                screen.blit(gameoverText, (32, 354))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g:
                        gaming = True
                        tetX.clear()
                        tetY.clear()
                        tetS.clear()
                        tetM.clear()
                        tetC.clear()
                        tetTot = 0
                        needSpawn = True
                        score = 0
                        lcount = 0
                if event.type == pygame.QUIT:
                    running = False
        # draws the blocks
        for i in range(tetTot):
            try:
                drawp(tetC[i], tetX[i], tetY[i])
            except:
                print(tetTot, " ", str(len(tetX)), " ", str(len(tetC)), " ", str(len(tetY)))
        frc = 0  # far right count
        flc = 0  # far left count
        # render score and whatnot
        clearx = 300
        cleary = 228
        overText = overFont.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(overText, (400, 100))
        overText = overFont.render("HOLD", True, (255, 255, 255))
        screen.blit(overText, (316, 120))
        overText = otherFont.render("Lines Cleared: " + str(lcount), True, (200, 200, 200))
        screen.blit(overText, (400, 132))
        overText = otherFont.render("Single Clears: " + str(single), True, (200, 200, 200))
        screen.blit(overText, (clearx, cleary))
        overText = otherFont.render("Double clears: " + str(double), True, (200, 200, 200))
        screen.blit(overText, (clearx, cleary + 16))
        overText = otherFont.render("Triple clears: " + str(triple), True, (200, 200, 200))
        screen.blit(overText, (clearx, cleary + 32))
        overText = otherFont.render("Tetris clears: " + str(tetris), True, (200, 200, 200))
        screen.blit(overText, (clearx, cleary + 48))
        overText = otherFont.render("High Score: " + str(hscore), True, (255, 150, 150))
        screen.blit(overText, (400, 80))
        drawNext()
        pygame.display.update()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


if __name__ == "__main__":
    main()