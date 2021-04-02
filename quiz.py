import pygame
import random
#########################################################################
# 기본 초기화(반드시 해야하는 것)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Mong game') # 게임이름

# FPS
clock = pygame.time.Clock()
#############################################################################################################

# 1. 사용자 게임 초기화 ( 배경화면, 게임이미지, 좌표 , 이동속도, 폰트)

background = pygame.image.load('C:/Users/Playdata/Desktop/파이썬활용/retrogame/background.png')

character = pygame.image.load('C:/Users/Playdata/Desktop/파이썬활용/retrogame/character.png')
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height

character_speed = 0.5

# 똥만들기
ddong = pygame.image.load('C:/Users/Playdata/Desktop/파이썬활용/retrogame/enemy.png')
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0,screen_width-ddong_width)
ddong_y_pos = 0

ddong_speed = 10

to_x = 0
to_y = 0
#################################################################


running = True # 게임이 진행중인가
while running:
    dt = clock.tick(60) # 게임화면 초당 프레임수 설정

    # 2. 이벤트 처리(키보드,마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
        
            
    character_x_pos += to_x

    # 3. 게임캐릭터 위치 

    character_x_pos += to_x*dt
    character_y_pos += to_y*dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width- character_width
    
    ddong_y_pos += ddong_speed 

    if ddong_y_pos > screen_height:
        ddong_x_pos = random.randint(0,screen_width)
        ddong_y_pos = 0

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print('충돌했습니다')
        running = False

    # 5. 화면에 그리기
    screen.blit(background,(0,0))

    screen.blit(character,(character_x_pos,character_y_pos)) 

    screen.blit(ddong,(ddong_x_pos,ddong_y_pos))


    pygame.display.update()

# 잠시 대기

pygame.time.delay(2000) # 2초 대기

# 6. pygame 종료
pygame.quit()