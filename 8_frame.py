import pygame
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



#################################################################


running = True # 게임이 진행중인가
while running:
    dt = clock.tick(60) # 게임화면 초당 프레임수 설정

    # 2. 이벤트 처리(키보드,마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    # 3. 게임캐릭터 위치 

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    

    # 4. 충돌 처리
   

    # 5. 화면에 그리기 

# 잠시 대기

pygame.time.delay(2000) # 2초 대기

# 6. pygame 종료
pygame.quit()