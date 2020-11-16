class NumArray:
    # This method is faster than the basic method, but less space-optimized
    def __init__(self, nums: List[int]):
        self.num_totals = [0]
        running_total = 0
        for num in nums:
            running_total += num
            self.num_totals.append(running_total)

    def sumRange(self, i: int, j: int) -> int:
        return self.num_totals[j+1] - self.num_totals[i]
