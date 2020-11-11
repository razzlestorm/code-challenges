def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    if len(nums) > 0:
        mid = len(nums)//2
        t = TreeNode(nums[mid])
        right = nums[mid+1:]
        left = nums[:mid]
        t.right = self.sortedArrayToBST(right)
        t.left = self.sortedArrayToBST(left)
        return t
