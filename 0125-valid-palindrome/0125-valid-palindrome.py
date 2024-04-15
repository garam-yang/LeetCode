class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = []
        for char in s:
            if char.isalnum():  # 문자가 알파벳이나 숫자인지 확인
            # point1. method of 'isalnum'
                filtered_chars.append(char.lower())  # 소문자로 변환하여 리스트에 추가
            # point2. method of 'lower' for making small letter
        # 리스트를 문자열로 변환: [] -> "" (join되면서 각 요소들끼리 따닥따닥 붙게 됨.)
        filtered_s = ''.join(filtered_chars)
        # 문자열을 뒤집어서 원래 문자열과 비교
        return filtered_s == filtered_s[::-1]
