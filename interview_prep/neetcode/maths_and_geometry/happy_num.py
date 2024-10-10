class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum(num):
            return sum([int(i)*int(i) for i in [*str(num)]])
        a = get_sum(n)
        slow = a
        fast = get_sum(a)
        if slow == 1:
            return True
        while slow!=fast:
            if fast == 1:
                return True
            slow = get_sum(slow)
            fast = get_sum(get_sum(fast))
        return False