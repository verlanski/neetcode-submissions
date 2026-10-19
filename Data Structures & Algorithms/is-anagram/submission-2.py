class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_dict = {}
        s_dict = {}


        if (len(s)) != (len(t)):
            return False

        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1

        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1
        
        for key, value in t_dict.items():
            if key not in s_dict:
                return False
            
            if value != s_dict[key]:
                return False

        return True
        