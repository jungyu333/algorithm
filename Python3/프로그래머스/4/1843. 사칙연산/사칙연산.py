def solution(arr):
    answer = -1
    
    nums = []
    operator = []
    
    for i in range(len(arr)):
        if i % 2 == 0:
            nums.append(arr[i])
        else:
            operator.append(arr[i])
    
    max_dp = [[0] * len(nums) for _ in range(len(nums))]
    min_dp = [[0] * len(nums) for _ in range(len(nums))]
    
    for length in range(len(nums)):
        for i in range(len(nums) - length):
            j = i + length
            
            # 길이 0 구간
            if i == j :
                max_dp[i][j] = min_dp[i][j] = int(nums[i])
                
            else:
                max_dp[i][j] = -float('inf')
                min_dp[i][j] = float('inf')
                
                for k in range(i, j):
                    op = operator[k]
                    
                    left_max = max_dp[i][k]
                    left_min = min_dp[i][k]
                    
                    right_max = max_dp[k+1][j]
                    right_min = min_dp[k+1][j]
                    
                    if op == '+':
                        max_dp[i][j] = max(max_dp[i][j], left_max + right_max)
                        min_dp[i][j] = min(min_dp[i][j], left_min + right_min)

                    else:  # '-'
                        max_dp[i][j] = max(max_dp[i][j], left_max - right_min)
                        min_dp[i][j] = min(min_dp[i][j], left_min - right_max)
                    
    
    
    return max_dp[0][len(nums)-1]