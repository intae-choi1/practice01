import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("My Game")

# 배경 이미지 불러오기
background = pygame.image.load("img/background.png")

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            print("끝")
            running = False

    screen.blit(background, (0, 0)) # 배경 그리기
    # screen.fill((0, 150, 255)) # 색으로 채울 수도 있음
    pygame.display.update() # 게임화면을 다시 그리기
pygame.quit()