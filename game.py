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

wall = 0     # 바닥 높이

change_level = False
motion = False

min_wall, max_wall = 0, 0

spike_x, spike_y = 0, 0

checkpoint = False
