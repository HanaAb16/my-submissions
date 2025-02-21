# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.pref = []
        self.product = 1 
        self.zero = -1

    def add(self, num: int) -> None:
        self.nums.append(num)
        self.n = len(self.nums)
        if num == 0:
            self.zero = self.n - 1
        else:
            self.product *= num
        self.pref.append(self.product)       

    def getProduct(self, k: int) -> int:
        if self.zero != -1 and  self.zero >= self.n - k:
            return 0
        else:
            if self.n - 1 - k < 0:
                return self.pref[-1]
            return self.pref[-1] // self.pref[self.n - 1 - k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)