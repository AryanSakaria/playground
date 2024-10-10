class Solution:
    def multiply(self, num1: str, num2: str) -> str:  
        def conv(s):
            return ord(s) - ord('0')
        
        digit = [0] * (len(num1)*len(num2)+1)

        for i, s_1 in enumerate(reversed(num1)):
            for j, s_2 in enumerate(reversed(num2)):
                digit[i+j] += conv(s_1) * conv(s_2)
        carry = 0
        for i in range(len(digit)):
            cur_digit = digit[i] + carry
            digit[i] = cur_digit % 10
            carry = cur_digit // 10

        for i in range(len(digit)):
            if digit[len(digit) - 1 - i]!=0:
                break
        
        return "".join([str(k) for k in reversed(digit)][i:])