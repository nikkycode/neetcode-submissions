class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        test = False
        for numbers in nums:
            if numbers in seen:
                test = True
                continue
            else:
                seen.append(numbers)
        return test
        pass