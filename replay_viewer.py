import pygame, sys, random
import re
from pygame.locals import *

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FPS = 30
BLANK = None

BLACK   =         (  0,   0,   0)
WHITE   =         (255, 255, 255)
GREEN   =         ( 48, 128,  72)
YELLOW  =         (216, 224,   0)

BGCOLOR = GREEN
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = WHITE
BASICFONTSIZE = 12

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BACK_SURF, BACK_RECT, NEXT_SURF, NEXT_RECT, rotated

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Paper Soccer - Replay Viewer')
    BASICFONT = pygame.font.Font('/usr/share/fonts/truetype/ttf-bitstream-vera/VeraBd.ttf', BASICFONTSIZE)
    
    # Store the option buttons and their rectangles in OPTIONS.
    BACK_SURF,   BACK_RECT = makeText('Wstecz', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 250, WINDOWHEIGHT - 106)
    NEXT_SURF, NEXT_RECT   = makeText('Dalej',  TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 130, WINDOWHEIGHT - 106)

    # Rotate board if needed
    #rotated = True
    rotated = False
    
    if rotated:
        r_prefix = '_rotate'
    else:
        r_prefix = ''

    # Open replay file, parse moves and split to list
    matchfile = open('61972037' + r_prefix + '.txt', 'r')
    matchfile_lines = matchfile.readlines()
    matchfile.close()
    
    moves = ''
            
    for i in range(12,len(matchfile_lines)-1):
        moves += matchfile_lines[i].strip() + ' '
        
    moves_formatted = re.sub(r'\d{1,2}\.', r'', moves)
    moves_array  = moves_formatted.split()
    
    state = 0

    while True:
        
        checkForQuit()
        
        drawBoard(moves_array, state)
        drawMatchInfo(matchfile_lines)
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if BACK_RECT.collidepoint(event.pos):
                    if state > 0:
                        state -= 1
                elif NEXT_RECT.collidepoint(event.pos):
                    if state < len(moves_array)-2: 
                        # -2, because last element is result, not valid move
                        state += 1
                    
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)
        
def makeText(text, color, bgcolor, top, left):
    textSurf = BASICFONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)

def drawBoard(moves_array, state):
    DISPLAYSURF.fill(BGCOLOR)
    
    pygame.draw.line(DISPLAYSURF, WHITE, (34, 68), (136, 68), 3)
    pygame.draw.line(DISPLAYSURF, WHITE, (136, 68), (136, 34), 3)
    pygame.draw.line(DISPLAYSURF, WHITE, (136, 34), (204, 34), 3)
    pygame.draw.line(DISPLAYSURF, WHITE, (204, 34), (204, 68), 3)
    pygame.draw.line(DISPLAYSURF, WHITE, (204, 68), (308, 68), 3)
    pygame.draw.line(DISPLAYSURF, WHITE, (308, 68), (308, 408), 3)
    pygame.draw.line(DISPLAYSURF, WHITE, (308, 408), (204, 408), 3)
    pygame.draw.line(DISPLAYSURF, WHITE, (204, 408), (204, 442), 3)
    pygame.draw.line(DISPLAYSURF, WHITE, (204, 442), (136, 442), 3)
    pygame.draw.line(DISPLAYSURF, WHITE, (136, 442), (136, 408), 3)
    pygame.draw.line(DISPLAYSURF, WHITE, (136, 408), (34, 408), 3)
    pygame.draw.line(DISPLAYSURF, WHITE, (34, 408), (34, 68), 3)
    
    pygame.draw.circle(DISPLAYSURF, WHITE, (170, 68), 0, 0)
    
    for i in range(7):
        for j in range(9):
            pygame.draw.circle(DISPLAYSURF, WHITE, (68+i*34, 102+j*34), 0, 0)
            
    # board's center
    pos_x = 170
    pos_y = 238
    
    for j in range(state+1):
        lines = len(moves_array[j])
        for i in range(lines):
            if int(moves_array[j][i]) == 0:
                new_pos_x, new_pos_y = pos_x, pos_y-34
                if j == state:
                    pygame.draw.line(DISPLAYSURF, YELLOW, (pos_x, pos_y), (new_pos_x, new_pos_y), 2)
                    if i == lines-1:
                        pygame.draw.circle(DISPLAYSURF, YELLOW, (new_pos_x+1, new_pos_y+1), 3, 0)
                else:
                    pygame.draw.line(DISPLAYSURF, WHITE, (pos_x, pos_y), (new_pos_x, new_pos_y), 1)
                pos_x, pos_y = new_pos_x, new_pos_y
            elif int(moves_array[j][i]) == 1:
                new_pos_x, new_pos_y = pos_x+34, pos_y-34
                if j == state:
                    pygame.draw.line(DISPLAYSURF, YELLOW, (pos_x, pos_y), (new_pos_x, new_pos_y), 3)
                    if i == lines-1:
                        pygame.draw.circle(DISPLAYSURF, YELLOW, (new_pos_x, new_pos_y), 3, 0)
                else:
                    pygame.draw.line(DISPLAYSURF, WHITE, (pos_x, pos_y), (new_pos_x, new_pos_y), 1)
                pos_x, pos_y = new_pos_x, new_pos_y
            elif int(moves_array[j][i]) == 2:
                new_pos_x, new_pos_y = pos_x+34, pos_y
                if j == state:
                    pygame.draw.line(DISPLAYSURF, YELLOW, (pos_x, pos_y), (new_pos_x, new_pos_y), 2)
                    if i == lines-1:
                        pygame.draw.circle(DISPLAYSURF, YELLOW, (new_pos_x+1, new_pos_y+1), 3, 0)
                else:
                    pygame.draw.line(DISPLAYSURF, WHITE, (pos_x, pos_y), (new_pos_x, new_pos_y), 1)
                pos_x, pos_y = new_pos_x, new_pos_y
            elif int(moves_array[j][i]) == 3:
                new_pos_x, new_pos_y = pos_x+34, pos_y+34
                if j == state:
                    pygame.draw.line(DISPLAYSURF, YELLOW, (pos_x, pos_y), (new_pos_x, new_pos_y), 3)
                    if i == lines-1:
                        pygame.draw.circle(DISPLAYSURF, YELLOW, (new_pos_x, new_pos_y), 3, 3)
                else:
                    pygame.draw.line(DISPLAYSURF, WHITE, (pos_x, pos_y), (new_pos_x, new_pos_y), 1)
                pos_x, pos_y = new_pos_x, new_pos_y
            elif int(moves_array[j][i]) == 4:
                new_pos_x, new_pos_y = pos_x, pos_y+34
                if j == state:
                    pygame.draw.line(DISPLAYSURF, YELLOW, (pos_x, pos_y), (new_pos_x, new_pos_y), 2)
                    if i == lines-1:
                        pygame.draw.circle(DISPLAYSURF, YELLOW, (new_pos_x+1, new_pos_y+1), 3, 0)
                else:
                    pygame.draw.line(DISPLAYSURF, WHITE, (pos_x, pos_y), (new_pos_x, new_pos_y), 1)
                pos_x, pos_y = new_pos_x, new_pos_y
            elif int(moves_array[j][i]) == 5:
                new_pos_x, new_pos_y = pos_x-34, pos_y+34
                if j == state:
                    pygame.draw.line(DISPLAYSURF, YELLOW, (pos_x, pos_y), (new_pos_x, new_pos_y), 3)
                    if i == lines-1:
                        pygame.draw.circle(DISPLAYSURF, YELLOW, (new_pos_x, new_pos_y), 3, 3)
                else:
                    pygame.draw.line(DISPLAYSURF, WHITE, (pos_x, pos_y), (new_pos_x, new_pos_y), 1)
                pos_x, pos_y = new_pos_x, new_pos_y
            elif int(moves_array[j][i]) == 6:
                new_pos_x, new_pos_y = pos_x-34, pos_y
                if j == state:
                    pygame.draw.line(DISPLAYSURF, YELLOW, (pos_x, pos_y), (new_pos_x, new_pos_y), 2)
                    if i == lines-1:
                        pygame.draw.circle(DISPLAYSURF, YELLOW, (new_pos_x+1, new_pos_y+1), 3, 0)
                else:
                    pygame.draw.line(DISPLAYSURF, WHITE, (pos_x, pos_y), (new_pos_x, new_pos_y), 1)
                pos_x, pos_y = new_pos_x, new_pos_y
            elif int(moves_array[j][i]) == 7:
                new_pos_x, new_pos_y = pos_x-34, pos_y-34
                if j == state:
                    pygame.draw.line(DISPLAYSURF, YELLOW, (pos_x, pos_y), (new_pos_x, new_pos_y), 3)
                    if i == lines-1:
                        pygame.draw.circle(DISPLAYSURF, YELLOW, (new_pos_x, new_pos_y), 3, 3)
                else:
                    pygame.draw.line(DISPLAYSURF, WHITE, (pos_x, pos_y), (new_pos_x, new_pos_y), 1)
                pos_x, pos_y = new_pos_x, new_pos_y
                
                
        textSurf, textRect = makeText('                               ', TEXTCOLOR, BGCOLOR, 10, 41)
        DISPLAYSURF.blit(textSurf, textRect)
        
        if j%2 == 0:
            if rotated:
                textSurf, textRect = makeText('#2   ' + moves_array[j], YELLOW, BGCOLOR, 34, 41)
                DISPLAYSURF.blit(textSurf, textRect)
            else:
                textSurf, textRect = makeText('#1   ' + moves_array[j], YELLOW, BGCOLOR, 34, 41)
                DISPLAYSURF.blit(textSurf, textRect)
        else:
            if rotated:
                textSurf, textRect = makeText('#1   ' + moves_array[j], YELLOW, BGCOLOR, 34, 41)
                DISPLAYSURF.blit(textSurf, textRect)
            else:
                textSurf, textRect = makeText('#2   ' + moves_array[j], YELLOW, BGCOLOR, 34, 41)
                DISPLAYSURF.blit(textSurf, textRect)
                
        textSurf, textRect = makeText('#2', WHITE, BGCOLOR, 220, 41)
        DISPLAYSURF.blit(textSurf, textRect)
        textSurf, textRect = makeText('#1', WHITE, BGCOLOR, 220, 421)
        DISPLAYSURF.blit(textSurf, textRect)

    DISPLAYSURF.blit(BACK_SURF, BACK_RECT)
    DISPLAYSURF.blit(NEXT_SURF, NEXT_RECT)
    
def drawMatchInfo(matchfile_lines):
    date = matchfile_lines[2].strip()
    date_formatted = re.sub(r'\[Date \"(\d{4}).(\d{2}).(\d{2})\"\]', r'\3.\2.\1', date)
    time = matchfile_lines[7].strip()
    time_formatted = re.sub(r'\[Time \"(\d{2}):(\d{2}):(\d{2})\"\]', r'\1:\2:\3', time)
    round_time = matchfile_lines[8].strip()
    round_time_formatted = re.sub(r'\[TimeControl \"(\d{1,3})\"\]', r'\1', round_time)
    textSurf, textRect = makeText(date_formatted + ', ' + time_formatted + ', ' + str(int(round_time_formatted)/60) + 'm', TEXTCOLOR, BGCOLOR, 340, 68)
    DISPLAYSURF.blit(textSurf, textRect)

    if rotated:
        player1 = matchfile_lines[4].strip()
        player1_formatted = re.sub(r'\[White \"(.+?)\"\]', r'\1', player1)
        player2 = matchfile_lines[5].strip()
        player2_formatted = re.sub(r'\[Black \"(.+?)\"\]', r'\1', player2)
        elo1 = matchfile_lines[9].strip()
        elo1_formatted = re.sub(r'\[WhiteElo \"(\d{1,4})\"\]', r'\1', elo1)
        elo2 = matchfile_lines[10].strip()
        elo2_formatted = re.sub(r'\[BlackElo \"(\d{1,4})\"\]', r'\1', elo2)
    else:
        player1 = matchfile_lines[4].strip()
        player1_formatted = re.sub(r'\[Black \"(.+?)\"\]', r'\1', player1)
        player2 = matchfile_lines[5].strip()
        player2_formatted = re.sub(r'\[White \"(.+?)\"\]', r'\1', player2)
        elo1 = matchfile_lines[9].strip()
        elo1_formatted = re.sub(r'\[BlackElo \"(\d{1,4})\"\]', r'\1', elo1)
        elo2 = matchfile_lines[10].strip()
        elo2_formatted = re.sub(r'\[WhiteElo \"(\d{1,4})\"\]', r'\1', elo2)

    if rotated:
        textSurf, textRect = makeText('#1 - ' + player1_formatted + ' - ' + elo1_formatted, TEXTCOLOR, BGCOLOR, 340, 91)
        DISPLAYSURF.blit(textSurf, textRect)
        textSurf, textRect = makeText('#2 - ' + player2_formatted + ' - ' + elo2_formatted, TEXTCOLOR, BGCOLOR, 340, 114)
        DISPLAYSURF.blit(textSurf, textRect)
    else:
        textSurf, textRect = makeText('#1 - ' + player2_formatted + ' - ' + elo2_formatted, TEXTCOLOR, BGCOLOR, 340, 91)
        DISPLAYSURF.blit(textSurf, textRect)
        textSurf, textRect = makeText('#2 - ' + player1_formatted + ' - ' + elo1_formatted, TEXTCOLOR, BGCOLOR, 340, 114)
        DISPLAYSURF.blit(textSurf, textRect)

if __name__ == '__main__':
    main()
