import pygame
import time
import random

pygame.init()


display_height = 400
display_width = 600


# mau sac
red = (255, 0 ,0)
green = (0, 255, 0)
ground = (255, 255, 179)
black  = (0, 0 ,0)


display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Ran San Moi')

# Setting game
clock = pygame.time.Clock()
snake_Speed = 30
snake_Block = 10
font_size = 20
font_style = pygame.font.SysFont('Verdana', font_size)


def message_func(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, (display_width/8 , display_height/2 -30))


def score_func(score):
    msg = "YOUR SCORE"
    value = font_style.render(msg + ": " + str(score), True, black)
    display.blit(value, [0,0])



def snake_func(snake_Block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_Block, snake_Block])



def gameLooping_func():
    game_end = False
    game_close = False

    x = display_width/2 
    y = display_height/2 

    x_change = 0
    y_change = 0

    #Tao mot list chua cac thanh phan cua con ran
    snake_List = []

    #Do dai ban dau cua con ran la 1
    snake_length = 1

    foodx = round(random.randrange(0, display_width - snake_Block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_Block) / 10.0) * 10.0


    while not game_end:
        while game_close == True:
            display.fill(ground)
            message_func("You lost! Press E to quit or R to play again", red)

            score_func(snake_length - 1)    
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_end = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        game_end = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLooping_func()


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_Block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_Block
                    y_change = 0
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_Block
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_Block

        if x >= display_width or x < 0 or y >= display_height or y <0:
            game_close = True

        x += x_change
        y += y_change

        display.fill(ground)


        #ve do an cho con ran
        pygame.draw.rect(display,red,[foodx,foody,snake_Block,snake_Block])
        

        #Thuc hien them phan than cua con ran vao danh sach
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_List.append(snake_Head)

       
        if len(snake_List) > snake_length:
            del snake_List[0]

        
        #for x1 in snake_List[:-1]:
        #    if x1 == snake_Head:
        #       game_close = True


        snake_func(snake_Block, snake_List)
        score_func(snake_length - 1)
        pygame.display.update()


        if x == foodx and y == foody:
            foodx = round(random.randrange(0, display_width - snake_Block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_Block) / 10.0) * 10.0
            snake_length += 1


        clock.tick(snake_Speed)


    pygame.quit
    quit()


gameLooping_func()