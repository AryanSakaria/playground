class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair_arr = [(position[i], speed[i]) for i in range(len(position))]
        sorted_arr = sorted(pair_arr, reverse = True)

        l,n = 0, len(position)
        ans = 0
        fleet_time = 0
        while l < n:
            pos_l = sorted_arr[l][0]
            spd_l = sorted_arr[l][1]
            curr_time = (target - pos_l)/spd_l
            if curr_time > fleet_time:
                ans +=1 
                fleet_time = curr_time
            l+=1
        return ans
