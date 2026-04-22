from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash = {}

        for str in strs:

            key = ''.join(sorted(str))
            
            if hash.get(key) is not None:
                current = hash.get(key)
                current.append(str)
            else:
                hash[key] = [str]

        return [ v for v in hash.values()]
