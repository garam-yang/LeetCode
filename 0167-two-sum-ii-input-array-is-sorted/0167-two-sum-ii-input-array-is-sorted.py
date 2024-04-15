class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # At first, two pointer is user for making 'O(n^2)' to 'O(N)'
        i, j =0, len(numbers)-1 # This is line for setting 'two pointer'

        # only using 'while loof' of O(N) is much better than using 'plusing conditional statesment'
        # we just need to moving two pointers until finding target.
        while numbers[i] + numbers[j] != target:
            s = numbers[i] + numbers[j]        
            if s > target:
                j -= 1
            else:
                i += 1 
                
        return [i + 1 , j + 1]