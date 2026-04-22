from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash = defaultdict(list)

        for str in strs:
            key = ''.join(sorted(str))
        
            hash[key].append(str)


        return [ v for v in hash.values()]
