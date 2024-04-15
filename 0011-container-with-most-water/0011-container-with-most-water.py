class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        mx = 0
        while i < j:
            k = min(height[i], height[j])
            amount = (j-i)*k
            mx = max(mx, amount)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return mx
        
