import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("My Game")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("img/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("img/character2.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2 # 화면 가로 절반에 위치하게
character_y_pos = screen_height - character_height # 화면 세로 가장 아래

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
chracter_speed = 0.5

# 이벤트 루프
running = True
while running:
    dt = clock.tick(60) # 초당 프레임 수 설정
    # print(f"fps: {clock.get_fps()}\t dt: {dt}")
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            print("끝")
            running = False

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터 왼쪽으로
                to_x -= chracter_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터 오른쪽으로
                to_x += chracter_speed
            elif event.key == pygame.K_UP: # 캐릭터 위로
                to_y -= chracter_speed
            elif event.key == pygame.K_DOWN: # 캐릭터 아래로
                to_y += chracter_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt # 프레임이 낮아지면 ㅅ
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
        
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0)) # 배경 그리기
    # screen.fill((0, 150, 255)) # 색으로 채울 수도 있음

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기
pygame.quit()