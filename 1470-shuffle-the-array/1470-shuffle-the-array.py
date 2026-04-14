class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        answer = []
        num_1 = nums[:n]
        num_2 = nums[n:]

        for x, y in zip(num_1, num_2):
            answer.append(x)
            answer.append(y)

        return answer