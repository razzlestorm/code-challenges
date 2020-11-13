
def missingNumber(self, nums: List[int]) -> int:
    num_set = set(nums)
    for ii in range(0, len(nums)+1):
        if ii not in num_set:
            return ii
