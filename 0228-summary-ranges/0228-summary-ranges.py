class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        idx = 0

        if not nums:
            return []

        start = nums[0]
        

        while idx < len(nums) - 1:
            
            if nums[idx] + 1 == nums[idx + 1]:
                # temp.append(nums[idx])
                
                idx = idx + 1
                
            else:
                
                if start != nums[idx]:
                    result.append(f"{start}->{nums[idx]}")
                else:
                    result.append(str(start))

                start = nums[idx + 1]
                idx = idx + 1


        if start != nums[idx]:
            result.append(f"{start}->{nums[idx]}")
        else:
            result.append(str(start))
        
        return result