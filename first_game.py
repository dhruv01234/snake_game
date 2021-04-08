import pygame
import random
import os
pygame.init()

# colors
White = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)
yellow = (255,255,0)
# game window
GameWindow = pygame.display.set_mode((1200,600))

# g
pygame.display.set_caption("my first game")


pygame.display.update()



clock = pygame.time.Clock()

font = pygame.font.SysFont(None,55)

def speak(voice):
    from win32com.client import Dispatch
    s = Dispatch("SAPI.SpVoice")
    s.Speak(voice)

def text_screen(text,color,x,y):
    screen_text = font.render(text, True, color)
    GameWindow.blit(screen_text,[x,y])

def plot_snake(GameWindow,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(GameWindow, black, [x,y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        GameWindow.fill(black)
        text_screen("welcome to snake game press enter to start",blue,250,300)
        text_screen("escape to exit",blue,450,350)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit( )
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    # speak("your game starts in 5 seconds")
                    # for i in range(5,0,-1):
                    #     speak(i)
                    gameloop()
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
        pygame.display.update()
        clock.tick(60)

# game loop
def gameloop():

    # game variales
    GameExit = False
    GameOver = False

    snake_x = 45
    snake_y = 45
    snake_size = 10
    velocity_x = 0
    velocity_y = 0

    velocity_var = 0

    food_x = random.randint(10,1190)
    food_y = random.randint(10,550)
    food_size = 10
    fps = 60

    wall_x = 600
    wall_y = 300
    wall_size_x = 10
    wall_size_y = 50    

    wall1_x = 0
    wall1_y = 0

    wall2_x = 675
    wall2_y = 0

    wall3_x = 0
    wall3_y = 590

    wall4_x = 675
    wall4_y = 590

    wall5_x = 0
    wall5_y = 0

    wall6_x = 0
    wall6_y = 375

    wall7_x = 1190
    wall7_y = 0

    wall8_x = 1190
    wall8_y = 375

    wall_sized_x = 525
    wall_sized_y = 10

    wall_sized1_x = 10
    wall_sized1_y = 225

    score = 0
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")

    with open("highscore.txt","r") as f:
        highscore = f.read()

    snake_list = []
    snake_lenght = 1

    while not GameExit:
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                GameExit = True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    
                    velocity_x = 3
                    velocity_y = 0

                if event.key == pygame.K_DOWN:
                
                    velocity_y = 3
                    velocity_x = 0
                    
                if event.key == pygame.K_UP:
                    
                    velocity_y = -3
                    velocity_x = 0
                
                if event.key == pygame.K_LEFT:

                    velocity_x = -3 
                    velocity_y = 0

                if event.key==pygame.K_SPACE:
                    velocity_x = 0
                    velocity_y = 0

                if event.key == pygame.K_q:
                    score += 1
                    if score>int(highscore):
                        highscore = score
                
                if event.key == pygame.K_s:
                    if velocity_x == 0:
                        velocity_y -= 1
                    else:
                        velocity_x -= 1
                    
                if event.key == pygame.K_w:
                    if velocity_x == 0:
                        velocity_y += 1
                    else:
                        velocity_x += 1
                
                if event.key==pygame.K_d:
                    snake_lenght += 1

        snake_x += velocity_x
        snake_y += velocity_y

        if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
            score += 1
            
            food_x = random.randint(10,1190)
            food_y = random.randint(10,550)
            

            snake_lenght += 1
            if score>int(highscore):
                highscore = score
            
        GameWindow.fill(White) #back ground 
        text_screen(f"score = {score}" + f"     highscore = {highscore}",red,5,5)
        head = []
        head.append(snake_x)
        head.append(snake_y)
        snake_list.append(head)

        if len(snake_list)>snake_lenght:
            del snake_list[0]

        if snake_x == wall_x and (snake_y >= 300 and snake_y <= 350):
            speak(f"your game is over and score is {score}")
            welcome()

        if head in snake_list[:-1]:
            speak(f"your game is over and score is {score}")
            welcome()
        
        if snake_x >=0 and snake_x <=525 and snake_y < 10:
            speak(f"your game is over and score is {score}")
            welcome()

        if snake_x >=675 and snake_x <=1200 and snake_y < 10:
            speak(f"your game is over and score is {score}")
            welcome()
        
        if snake_x >=0 and snake_x <=525 and snake_y > 590:
            speak(f"your game is over and score is {score}")
            welcome()

        if snake_x >=675 and snake_x <=1200 and snake_y > 590:
            speak(f"your game is over and score is {score}")
            welcome()

        if snake_y >= 0 and snake_y <= 225 and snake_x < 10:
            speak(f"your game is over and score is {score}")
            welcome()

        if snake_y >= 375 and snake_y <= 600 and snake_x < 10:
            speak(f"your game is over and score is {score}")
            welcome()

        if snake_y >= 0 and snake_y <= 225 and snake_x > 1190:
            speak(f"your game is over and score is {score}")
            welcome()

        if snake_y >= 375 and snake_y <= 600 and snake_x > 1190:
            speak(f"your game is over and score is {score}")
            welcome()

        if snake_x > 525 and snake_x < 665 and snake_y < 0:
            snake_y = snake_y + 600

        if snake_x > 525 and snake_x < 665 and snake_y > 600:
            snake_y = snake_y - 600

        if snake_y > 225 and snake_y < 375 and snake_x < 0:
            snake_x = snake_x + 1200

        if snake_y > 225 and snake_y < 375 and snake_x > 1200:
            snake_x = snake_x - 1200

        with open("highscore.txt","w") as f:
            f.write(str(highscore))
        plot_snake(GameWindow,black,snake_list,snake_size)

        pygame.draw.rect(GameWindow, black, [snake_x, snake_y, snake_size, snake_size])
        pygame.draw.rect(GameWindow, red, [food_x, food_y, food_size, food_size])
        pygame.draw.rect(GameWindow, yellow, [wall_x, wall_y, wall_size_x, wall_size_y])
        pygame.draw.rect(GameWindow, yellow, [wall1_x, wall1_y, wall_sized_x, wall_sized_y])
        pygame.draw.rect(GameWindow, yellow, [wall2_x, wall2_y, wall_sized_x, wall_sized_y])
        pygame.draw.rect(GameWindow, yellow, [wall3_x, wall3_y, wall_sized_x, wall_sized_y])
        pygame.draw.rect(GameWindow, yellow, [wall4_x, wall4_y, wall_sized_x, wall_sized_y])
        pygame.draw.rect(GameWindow, yellow, [wall5_x, wall5_y, wall_sized1_x, wall_sized1_y])
        pygame.draw.rect(GameWindow, yellow, [wall6_x, wall6_y, wall_sized1_x, wall_sized1_y])
        pygame.draw.rect(GameWindow, yellow, [wall7_x, wall7_y, wall_sized1_x, wall_sized1_y])
        pygame.draw.rect(GameWindow, yellow, [wall8_x, wall8_y, wall_sized1_x, wall_sized1_y])
        pygame.display.update() # update the bg
        clock.tick(fps)
    pygame.quit()
    quit() 
welcome()