class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        
        left_max_height = 0
        right_max_height = 0
        total_water = 0

        while l < r:
            if height[l] < height[r]: # 이건 단지 결국에는 투포인터로서 모든 리스트 요소를 다 돌아볼 조건들 중 하나임!
                if left_max_height <= height[l]:
                    left_max_height = height[l]
                else:
                    total_water += (left_max_height - height[l])
                l += 1 
            else:
                if right_max_height <= height[r]:
                    right_max_height = height[r]
                else: # 쉽게 말해, 이동한 애가 원래 mx보다 낮은 애라면...
                    total_water += (right_max_height - height[r]) 
                r -= 1 
        return total_water
