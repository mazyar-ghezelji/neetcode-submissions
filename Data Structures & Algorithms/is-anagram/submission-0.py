class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_hash = {}

    
        for c in s:
            if c in char_hash:
                char_hash[c] += 1
            else:
                char_hash[c] = 1
        
        for c in t:
            if c not in char_hash:
                return False
            else:
                char_hash[c] -= 1
        
        for c in char_hash:
            if char_hash[c] !=0:
                return False
        return True
        