class Solution:
    def reverseBits(self, n: int) -> int:
        mask = 0xffffffff
        num = n & mask
        rev = 0
        i = 0 
        while i < 32:
            rev = (rev << 1) + num%2
            num = num >> 1
            i += 1
        return rev