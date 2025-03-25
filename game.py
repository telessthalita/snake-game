import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
purple = (50, 153, 213)
light_purple = (192, 176, 224)
dark_purple = (89, 56, 125)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

snake_block = 10
initial_speed = 15
font_style = pygame.font.SysFont(None, 50)

def message(msg, color, position):
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center=position)
    dis.blit(mesg, text_rect)

def gameLoop():
    game_over = False
    game_close = False
    speed = initial_speed
    best_score = 0
    
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    score = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            dis.fill(purple)
            message("Você Perdeu!", red, (dis_width / 2, dis_height / 3))
            message("Pressione Q para sair ou C para jogar novamente", white, (dis_width / 2, dis_height / 2.5))
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        for y in range(dis_height):
            color = pygame.Color(int(light_purple[0] + (dark_purple[0] - light_purple[0]) * y / dis_height),
                                  int(light_purple[1] + (dark_purple[1] - light_purple[1]) * y / dis_height),
                                  int(light_purple[2] + (dark_purple[2] - light_purple[2]) * y / dis_height))
            pygame.draw.line(dis, color, (0, y), (dis_width, y))

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for segment in snake_List:
            pygame.draw.rect(dis, black, [segment[0], segment[1], snake_block, snake_block])


        message(f"Pontuação: {score} | Melhor: {best_score}", white, (dis_width / 2, 30))
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 1
            speed += 0.5
            best_score = max(best_score, score)

        clock.tick(speed)

    pygame.quit()
    quit()

gameLoop()