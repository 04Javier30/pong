import pygame, sys
from pygame import *
from pygame import font
from pygame.display import update
from paddel import Paddle
from ball import *
from time import perf_counter

pygame.init()

black = (0,0,0)
white = (255,255,255)
size = (800, 600)
game_display = pygame.display.set_mode(size)
pygame.display.set_caption('pong')

paddle1 = Paddle(white, 10, 130)
paddle1.rect.x = 5
paddle1.rect.y = 250

paddle2 = Paddle(white, 10, 130)
paddle2.rect.x = 785
paddle2.rect.y = 250

ball = Ball(white, 20, 20)
ball.rect.x = 400
ball.rect.y = 200

sprites_list = pygame.sprite.Group()

sprites_list.add(paddle1)
sprites_list.add(paddle2)
sprites_list.add(ball)

score1 = 0
score2 = 0

vaL1 = val1
vaL2 = val2

scoring_sound = pygame.mixer.Sound("pong/music/scoring.mp3")
poping_sound = pygame.mixer.Sound("pong/music/poping.wav")

clock = pygame.time.Clock()

game_on = True

while True:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                pygame.quit()
                sys.exit()
        
    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_w]:
        paddle1.paddles_moving_up(6)
    if keys[pygame.K_s]:
        paddle1.paddles_moving_down(6)
    if keys[pygame.K_UP]:
        paddle2.paddles_moving_up(6)
    if keys[pygame.K_DOWN]:
        paddle2.paddles_moving_down(6)
        
    sprites_list.update()
    
    if game_on == True:    
        if ball.rect.x >= 780:
            score1 += 1
            scoring_sound.play()
            ball.velocity[0] = -ball.velocity[0]
            ball.rect.x = 400
            ball.rect.y = 300
            
        if ball.rect.x <= 2:
            score2 += 1
            scoring_sound.play()
            ball.velocity[0] = -ball.velocity[0]
            ball.rect.x = 400
            ball.rect.y = 300
            
        if ball.rect.y > 578:
            ball.velocity[1] = -ball.velocity[1]
            
        if ball.rect.y < 2:
            ball.velocity[1] = -ball.velocity[1]
            
    if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
        ball.bouncing()
        poping_sound.play()
        
    game_display.fill(black)
        
    pygame.draw.line(game_display, white, [400,0], [400,600], 10)
        
    sprites_list.draw(game_display)
        
    font = pygame.font.Font(None, 100)
    text = font.render(str(score1), 1, white)
    game_display.blit(text,(305,10))
    text = font.render(str(score2), 1, white)
    game_display.blit(text,(450,10))
    
    if score1 == 5 or score2 == 5:
        game_on = False
        if game_on == False:
            colourFont = (255,0,0)
            fuenteGameOver =  pygame.font.SysFont("Arial",100)
            textoGameOver = fuenteGameOver.render("GameOver", 0, colourFont)
            game_display.blit(textoGameOver, (30, 250))
            ball.rect.x = 400
            ball.rect.y = 300
            #corregir la parte justamente debajo
            paddle1.paddles_moving_up(0)
            paddle1.paddles_moving_down(0)
            paddle2.paddles_moving_up(0)
            paddle2.paddles_moving_down(0)
        
    pygame.display.update()
        
    pygame.display.flip()
        
    clock.tick(60)
    
pygame.quit()