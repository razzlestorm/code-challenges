class Solution:
    def __init__(self):
        self.memo = {}
    def climbStairs(self, n: int) -> int:
        # output = number of unique ways to reach n (order does matter)
        # input = number int
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n in self.memo:
            return self.memo[n]

        else:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.memo[n]
