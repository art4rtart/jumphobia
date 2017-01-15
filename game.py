# initializing variables

jumping, flying, falling = 0, 0, 15     # 점프, 날라댕기는 상태 변수, 떨어지는 속도
movement = 0 # 날라댕기면서 방향전환하는거

portal_x, portal_y = 0, 0 # 포탈 위치
back_x, back_y = 500, 250 # 배경 초기 위치

max_x = 0 # 맵 최대 x 값
min_x = 0 # 맵 최소 x 값

x = 50         # 캐릭터 위치 x
y = 134        # 캐릭터 위치 y

seta = 90      # 각도

reset = False # 죽으면 게임리셋

temp = 0 # 뭐였더라..


sign_x, sign_y = 0, 0   # 표지판
count = 0 # 카운트인데 뭔지 까먹음
jumped = 0 # 레벨1에서만 쓸듯..

height = 0     # 바닥 높이

change_level = False # 레벨 변경 상태
motion = False      # 레벨 변경후 좌, 우로 서있기

min_wall, max_wall = 0, 0  # 좌우 벽

checkpoint = False # 체크포인트

jump_x, jump_y = 11, 20   # 점핑 길이

key = True


background_x, background_y = 500, 250

move = 0
dir = 1

fall = 1

gak = 280
gck = 70

monster = True  # 몬스터

t1, t2, t3, t4 = False, False, False, False  # 삼각형
godown = False

event = False

title_x, title_y = 500, 270  # 게임타이틀 위치

menu = 0 # ?

gravity = False # 중력
timer = 0 # 중력으로 인해 캐릭터 돌아가는 속도 조절
change_motion = False  # 중력돌아가는 모션