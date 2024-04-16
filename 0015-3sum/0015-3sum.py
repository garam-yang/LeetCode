class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 배열을 먼저 정렬
        answer = []  # 결과를 담을 리스트
        for i in range(len(nums) - 2):  # 첫 번째 수를 결정하는 반복문
            if nums[i] > 0:
                break  # 첫 번째 수가 양수라면 더 이상 확인할 필요 없음
            if i > 0 and nums[i] == nums[i-1]:
                continue  # 이전과 같은 수를 사용하는 경우 중복 제거
            l = i + 1  # 왼쪽 포인터
            r = len(nums) - 1  # 오른쪽 포인터
            while l < r:  # 두 포인터가 만나지 않을 때까지 반복
                total = nums[i] + nums[l] + nums[r]  # 세 수의 합
                if total < 0:
                    l += 1  # 합이 0보다 작다면 왼쪽 포인터를 오른쪽으로 이동
                elif total > 0:
                    r -= 1  # 합이 0보다 크다면 오른쪽 포인터를 왼쪽으로 이동
                else:
                    triplet = [nums[i], nums[l], nums[r]]  # 세 수의 조합
                    answer.append(triplet)  # 결과 리스트에 추가
                    while l < r and nums[l] == triplet[1]:
                        l += 1  # 왼쪽 포인터가 중복되는 값은 건너뛰기
                    while l < r and nums[r] == triplet[2]:
                        r -= 1  # 오른쪽 포인터가 중복되는 값은 건너뛰기
        return answer  # 모든 가능한 조합을 담은 리스트 반환
