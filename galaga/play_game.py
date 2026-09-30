import pygame
import random
from time import sleep

# 게임의 전역변수
BLACK = (0, 0, 0) # tuple
RED = (255, 0, 0) # RGB
pad_width = 480
pad_height = 640

# 전투기의 크기 설정
fighter_width = 36
fighter_height = 38

# 적군 크기 설정
enemy_width = 26
enemy_height = 20

# 적을 맞춘 개수 count를 출력
def draw_score(count: int) -> None:
    global gamepad
    font = pygame.font.SysFont(None, 20)
    text = font.render("Enemy Kills: " + str(count), True, (255, 255, 255))
    gamepad.blit(text, (0, 0))

# 적이 화면 아래로 통과한 숫자 출력
def draw_passed(count: int) -> None:
    global gamepad
    font = pygame.font.SysFont(None, 20)
    text = font.render("Enemy Passed: " + str(count), True, RED)
    gamepad.blit(text, (360, 0))

# 화면 정중앙에 Game Over or Crash! 출력
def display_message(text: str) -> None:
    global gamepad
    text_font = pygame.font.SysFont(None, 20)
    text = text_font.render(text, True, RED)
    textpos = text.get_rect()
    textpos.center = (int(pad_width / 2), int(pad_height / 2))
    gamepad.blit(text, textpos)
    pygame.display.update()
    sleep(2)
    run_game()
    
# 적과 충돌했을 때 메시지
def crash():
    global gamepad
    display_message("Crashed!")

def gameover():
    global gamepad
    display_message("Game Over!")

# 게임에 사용되는 객체 그리기
def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x, y))

# 게임 실행할 메인 함수
def run_game():
    global gamepad, clock, fighter, enemy, bullet

    # 총알에 격추되었을 때
    is_shot = False
    shot_count = 0
    enemy_passed = 0

    # 총알의 좌표를 담을 배열
    bullet_xy = []

    # 적군 초기 위치 랜덤하게 생성
    enemy_x = random.randrange(0, pad_width - enemy_width)
    enemy_y = 0
    enemy_speed = 3

    # 전투기 초기 위치(x, y) 설정
    x = int(pad_width * 0.45)
    y = int(pad_height * 0.9)
    # 전투기 이동 거리
    x_change = 0


    onGame = False
    
    while not onGame:
        for event in pygame.event.get():
            # 마우스로 x 누르면 종료
            if event.type == pygame.QUIT:
                onGame = True
            # 키보드 눌렸을 때 좌우 이동 처리
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= 5
                elif event.key == pygame.K_RIGHT:
                    x_change += 5
                # 왼쪽 ctrl 키가 눌렸을 때
                elif event.key == pygame.K_LCTRL:
                    # 총알은 2발까지만 가능
                    if len(bullet_xy) < 2:
                        # 발사 위치
                        bullet_x = x + (fighter_width / 2)
                        bullet_y = y
                        bullet_xy.append([bullet_x, bullet_y])
            
        # for loop 끝

        # 게임 화면 검은색으로 채우고 60프레임으로 업데이트
        gamepad.fill(BLACK)
        # 전투기 위치 재조정
        x += x_change

        # 왼쪽 끝에 가면 x = 0
        if x < 0:
            x = 0
        # 오른쪽 끝에 갔을 때
        elif x > pad_width - fighter_width:
            x = pad_width - fighter_width

        # 적과 충돌했는지 좌표 비교
        if y < enemy_y + enemy_height:
            cond = (
                (enemy_x > x and enemy_x < x + fighter_width) or 
                (enemy_x + enemy_width > x 
                 and enemy_x + enemy_width < x + fighter_width))
            if cond:
                crash()
                        
            # 키보드에서 손이 떼지면 KEYUP ... 안 움직임.
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        
        # 전투기 그리기
        drawObject(fighter, x, y)

        # 총알 그리기
        # 총알 배열이 비어있지 않을 때만 그림.
        if len(bullet_xy) != 0:
            # 총알은 10씩 위로 올라가게 그림.
            # enumerate()는 배열을 인덱스를 생성해서 순차적으로 돌릴 때
            for i, bxy in enumerate(bullet_xy):
                # 매번 10씩 위로
                bxy[1] -= 10
                # 변경된 y 값을 해당 총알의 y 값에 넣어줌.
                bullet_xy[i][1] = bxy[1]

                # 총알이 적기를 맞췄는지 확인
                if bxy[1] < enemy_y:
                    if bxy[0] > enemy_x and bxy[0] < enemy_x + enemy_width:
                        bullet_xy.remove(bxy)
                        is_shot = True
                        shot_count += 1

                # 총알이 맨 위를 뚫고 나갔을 때 -> 총알 배열에서 삭제
                if bxy[1] <= 0:
                    try:
                        bullet_xy.remove(bxy)
                    except:
                        pass

        if len(bullet_xy) != 0:
            # 총알 그리기
            # bx , by = [x1, x2]
            for bx, by in bullet_xy:
                drawObject(bullet, bx, by)

        # 스코어 출력하기
        draw_score(shot_count)
        
        # 적군 임의의 위치에 생성 후 아래로 움직이도록 설정
        # 적이 움직이게 좌표 설정(+3 -> enemy_speed)
        # 적군의 y 값이 > pad_height이면 다시 맨 위에 랜덤하게 시작
        enemy_y += enemy_speed

        # 맨 밑을 지났는지 확인
        if enemy_y > pad_height:
            enemy_y = 0
            enemy_x = random.randrange(0, pad_width - enemy_width)
            # 통과한 적의 수 늘려줌.
            enemy_passed += 1

        # 3개를 통과시키면 게임 오버
        if enemy_passed == 3:
            gameover()

        # 통과된 적기 수 출력
        draw_passed(enemy_passed)

        # 적이 무기에 맞으면 스피드 올려주기
        if is_shot:
            enemy_speed += 1
            if enemy_speed >= 10:
                enemy_speed = 10
            # 적기 없애기
            enemy_x = random.randrange(0, pad_width - enemy_speed)
            enemy_y = 0
            is_shot = False

        # 적군 그리기
        drawObject(enemy, enemy_x, enemy_y)

        pygame.display.update()
        clock.tick(60)

    # while 루프 종료
    pygame.quit()


# 게임 초기화 함수
def init_game():
    global gamepad, clock, fighter, enemy, bullet
    pygame.init()

    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption("MyGALAGA")

    # 전투기 이미지 가져오기
    fighter = pygame.image.load("fighter.png")

    # 적군 이미지 가져오기
    enemy = pygame.image.load("enemy.png")

    # 총알 이미지 가져오기
    bullet = pygame.image.load("bullet.png")

    clock = pygame.time.Clock() # 초당 30프레임

if __name__ == "__main__":
    init_game()
    run_game()