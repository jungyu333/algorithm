class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        def helper(s, t ,hash):
            for char_s, char_t in zip(s, t):
            
                if char_s != char_t:
                    if char_s not in hash:
                        hash[char_s] = char_t
                    elif hash.get(char_s) != char_t:
                        return False
                else:
                    if char_s not in hash:
                        hash[char_s] = char_t
                    else:
                        if hash[char_s] != char_t:
                            return False
                        
            
            return True

        result = helper(s,t,{})
        reverse_result = helper(t,s,{})

        return result and reverse_result