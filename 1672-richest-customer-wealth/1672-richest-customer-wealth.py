class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        wealth_list = []

        for account in accounts:
            wealth = sum(account)
            wealth_list.append(wealth)
        
        return max(wealth_list)
            
        