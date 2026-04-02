class Solution:
    def isHappy(self, n: int) -> bool:

        history = []
        
        while True:

            sum = 0

            for digit in str(n):
                sum += int(digit) ** 2

            if sum == 1:
                return True

            if sum in history:
                return False

            history.append(sum)
            n = sum   

        