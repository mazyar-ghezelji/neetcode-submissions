class Solution:
    def checkAnagram(self, str1:str, str2:str) -> bool:
        if len(str1) != len(str2):
            return False
        char_dict = {}
        for s in str1:
            if s in char_dict:
                char_dict[s] += 1
            else:
                char_dict[s] = 1
        for s in str2:
            if s not in char_dict:
                return False
            char_dict[s] -=1
        for s in char_dict:
            if char_dict[s] !=0:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        strs_dict[strs[0]] = [strs[0]]

        for a in range(1,len(strs)):
            added = False
            for b in range(a):
                if self.checkAnagram(strs[a],strs[b]):
                    strs_dict[strs[b]].append(strs[a])
                    added = True
                    break
            if not added:
                strs_dict[strs[a]] = [strs[a]]
        # print
        result = []
        for i in strs_dict:
            result.append(strs_dict[i])
        return result