class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        splited = s.split(' ')

        p_to_s = {}
        s_to_p = {}
        
        if len(pattern) != len(splited):
            return False

        for p, s in zip(pattern, splited):
            
            if p in p_to_s:
                if p_to_s.get(p) != s:
                    return False
            else:
                p_to_s[p] = s
            
            if s in s_to_p:
                if s_to_p.get(s) != p:
                    return False
            else:
                s_to_p[s] = p


        return True
