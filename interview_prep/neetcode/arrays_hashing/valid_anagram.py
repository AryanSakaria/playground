class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict, t_dict = {}, {}
        for k in s:
            if k in s_dict:
                s_dict[k]+=1
            else:
                s_dict[k] = 1
        for k in t:
            if k in t_dict:
                t_dict[k] += 1
            else:
                t_dict[k] = 1
        if len(s_dict)!= len(t_dict):
            return False
        for k in s_dict:
            if k in t_dict:
                if s_dict[k]!=t_dict[k]:
                    return False
            else:
                return False
        return True
