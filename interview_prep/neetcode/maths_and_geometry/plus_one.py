class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        bit = digits[i] + 1
        carry = int(bit/10)
        digits[i] = (digits[i] + 1)%10
        i -= 1
        while carry:
            if i < 0:
                digits.insert(0, carry)
                return digits
            carry = int((digits[i] + 1)/10)
            digits[i] = (digits[i] + 1)%10
            i -= 1 
        return digits