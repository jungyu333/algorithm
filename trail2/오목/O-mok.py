board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.

N = 19

DIRS = [(0, 1), (1, 0), (1, 1), (-1, 1)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def is_win(r, c, dr, dc):
    """(r, c)에서 (dr, dc) 방향으로 정확히 5목인지 확인"""
    color = board[r][c]

    # 1) 시작점 앞 칸이 같은 색이면 여기가 시작점이 아님 (6목 방지 + 중복 방지)
    pr, pc = r - dr, c - dc
    if in_range(pr, pc) and board[pr][pc] == color:
        return False

    # 2) 진행 방향으로 같은 색 개수 세기
    cnt = 0
    nr, nc = r, c
    while in_range(nr, nc) and board[nr][nc] == color:
        cnt += 1
        nr += dr
        nc += dc

    return cnt == 5   # 6목 이상은 False


def solve():
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                continue
            for dr, dc in DIRS:
                if is_win(r, c, dr, dc):
                    mr, mc = r + 2 * dr, c + 2 * dc   # 5개 중 가운데
                    return board[r][c], mr + 1, mc + 1
    return None

res = solve()
if res:
    print(res[0])
    print(res[1], res[2])
else:
    print(0)