from typing import List

# solution 1. swap with two pointers
class Solution1:
    def reverseString1(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# solution 2. Pythonic way
class Solution2:
    def reverseString2(self, s: List[str]) -> None:
        s.reverse()


# s = s[::-1] : 리트코드에서는 공간 복잡도를 O(1)로 제한하면서 변수 할당 처리에 제약
# s[:] = s[::-1] : 이와 같은 트릭 사용