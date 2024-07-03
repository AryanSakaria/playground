class Solution:
    def encode(self, strs):
        enc_str = ','.join([str(len(str_)) for str_ in strs])
        enc_str = str(len(enc_str)) + '!' + enc_str
        for str_ in strs:
            enc_str += str_
        print(enc_str)
        return enc_str

    def decode(self, s):
        for i, c in enumerate(s):
            if c == '!':
                start_index = i
                break
        ans = []
        print()
        print("start index ", start_index)
        num_dec = int(s[:start_index])
        print(num_dec)
        if num_dec == 0:
            return ans
        start_index+=1
        enc_str = s[start_index : start_index  + num_dec]
        rem_s = s[start_index + num_dec:]
        start_r = 0
        for len_str in enc_str.split(','):
            ans.append(rem_s[start_r:start_r + int(len_str)])
            start_r += int(len_str)
        return ans

if __name__ == '__main__':
    sol_obj = Solution()
    strs = ["we","say",":","yes","!@#$%^&*()"]
    print(sol_obj.decode(sol_obj.encode(strs)))