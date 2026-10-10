class NumArray:

    def __init__(self, nums: list[int]):
        self.res = []
        total = 0
        for num in nums:
            total += num
            self.res.append(total)
                  

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.res[right]
        return self.res[right] - self.res[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)