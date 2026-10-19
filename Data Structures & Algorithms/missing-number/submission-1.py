class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            seen.add(num)

        numbers = (len(nums))
        for i in range(numbers + 1):
            if i not in seen:
                return i
        