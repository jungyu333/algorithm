n = int(input())
adjacent = list(map(int, input().split())) if n >= 2 else []

# Please write your code here.

result_list = []

for a in range(1, n + 1):                 # 수정 1: 첫 원소는 1~N
    prev_a = a
    temp = [prev_a]
    seen = {prev_a}                       # 수정 2: 중복 검사용 set

    for s in adjacent:
        next_a = s - prev_a
        if next_a <= 0 or next_a > n or next_a in seen:   # 수정 2: 범위 + 중복 검사
            temp = []
            break
        temp.append(next_a)
        seen.add(next_a)
        prev_a = next_a

    if len(temp) == n:                    # 수정 3: N=1도 통과하도록
        result_list.append(temp)

result = sorted(result_list)[0]           # 수정 4: 사전순 최소

result = " ".join(map(str, result))

print(result)