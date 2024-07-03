class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_dict = {}
        for str_i in strs:
            str_s = ''.join(sorted(str_i))
            if str_s in s_dict:
                s_dict[str_s].append(str_i)
            else:
                s_dict[str_s] = [str_i]
        
        return [s_dict[key] for key in s_dict] 
