class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        cnt_dict = {}        
        for i in hand:
            cnt_dict[i] = 1 + cnt_dict.get(i, 0)
            
        hand = list(sorted(set(hand)))
        print(hand)
        for i in hand:
            if cnt_dict[i] == 0:
                continue
            i_cnt = cnt_dict[i]
            for k in range(1,groupSize):
                k_num = i + k
                if not k_num in cnt_dict:
                    return False
                if cnt_dict[k_num] < cnt_dict[i]:
                    return False
                cnt_dict[k_num] -= i_cnt
            cnt_dict[i] = 0
        
        for cnt in cnt_dict:
            if cnt_dict[cnt] > 0:
                return False
        return True
