N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < M

def is_LEE(r, c, dr, dc):
    
    cnt = 0
    token = ''
    nr, nc = r, c
    while in_range(nr, nc) and (arr[nr][nc] == 'L' or arr[nr][nc] == 'E'):
        cnt += 1
        token += arr[nr][nc]

        nr += dr
        nc += dc

        if cnt == 3:
            break

    return token == 'LEE'   

def solve():
    result = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] != 'L':
                continue
            for dr, dc in DIRS:
                if is_LEE(r, c, dr, dc):
                    result += 1
    return result

print(solve())
