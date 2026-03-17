def solution(m, n, puddles):
    answer = 0
        
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    dp[1][1] = 1
    
    # dp : 해당 지점까지 이동 가지 수
    # dp[row][col] = sum(dp[row - 1][col] , dp[row][col - 1])

    for row in range(1 ,n + 1):
        for col in range(1, m + 1):
            
            # 시작점은 통과
            if col == 1 and row == 1:
                continue
            
            # 현재가 물웅덩이면 0
            if [col, row] in puddles:
                dp[row][col] = 0
            else:
                dp[row][col] = dp[row][col - 1] + dp[row - 1][col]
    
    answer = dp[-1][-1] % 1000000007
    
    return answer