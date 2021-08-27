import collections
from collections import deque
import re
# self는 객체 선언시 사용. self를 사용하면 반드시 class가 필요하고 인스턴스를 생성해야함.
# Solution 1. Using List
class Solution1:
    def isPalindrome_list(self, s: str) -> bool:
        strs1 = []
        for char in s:
            if char.isalnum():
                strs1.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs1) > 1:
            if strs1.pop(0) != strs1.pop():
                return False

        return True

# Solution 2. Using Deque
class Solution2:
    def isPalindrome_deq(self, s: str) -> bool:
        strs2: deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs2.append(char.lower())

        while len(strs2) > 1:
            if strs2.popleft() != strs2.pop():
                return False

        return True

# Solution 3. Using Slicing
class Solution3:
    def isPalindrome_slc(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]
        # 슬라이싱을 이용해서 문자열을 뒤집음

sol1 = Solution1()
sol2 = Solution2()
sol3 = Solution3()
s = 'A man, a plan, a canal: Panama'
print('solution1 using list : ', end='')
print(sol1.isPalindrome_list(s))
print('solution2 using deque : ', end='')
print(sol2.isPalindrome_deq(s))
print('solution3 using slicing : ', end='')
print(sol3.isPalindrome_slc(s))
