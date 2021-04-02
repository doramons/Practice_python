import pygame

pygame.init() #초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Mong game') # 게임이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/Playdata/Desktop/파이썬활용/retrogame/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/Playdata/Desktop/파이썬활용/retrogame/character.png")
character_size = character.get_rect().size # 이미지의 크기 구하기
character_width = character_size[0] # 캐릭터 가로크기
character_height = character_size[1] # 캐릭터 세로크기
character_x_pos = (screen_width - character_width)/2 # 화면 가로 절반 크기
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당

to_x = 0
to_y = 0

# 이동 속도
character_speed = 5

# 이벤트 루프
running = True # 게임이 진행중인가
while running:
    dt = clock.tick(30) # 게임화면 초당 프레임수 설정
    
    for event in pygame.event.get(): # 어떤 이벤트가 발생하는지
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는지
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # 캐릭터가 화면밖에 나가지 않도록 설정
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width -character_width:
        character_x_pos = screen_width -character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height -character_height:
        character_y_pos = screen_height -character_height

    # screen.fill((0,0,255)) # 색으로 채워넣을 수도 있음
    screen.blit(background,(0,0)) # 배경그리기

    screen.blit(character, (character_x_pos,character_y_pos)) # 캐릭터 그리기

    pygame.display.update() #게임화면을 다시 그리기

    

# pygame 종료
pygame.quit()