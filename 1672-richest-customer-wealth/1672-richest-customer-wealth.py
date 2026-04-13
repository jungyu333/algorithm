class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        wealth = list(map(sum, accounts))
            
        return max(wealth)