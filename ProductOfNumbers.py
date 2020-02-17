class ProductOfNumbers:

    def __init__(self):
        self.prefix_product = []
        self.zeros_positions = []

    def add(self, num: int) -> None:
        if num == 0:
            self.zeros_positions.append(len(self.prefix_product))
            self.prefix_product.append(1)
        else:
            if len(self.prefix_product) == 0:
                self.prefix_product.append(num)
            else:
                self.prefix_product.append(self.prefix_product[-1] * num)
            
    def getProduct(self, k: int) -> int:
        for i in self.zeros_positions:
            if i >= len(self.prefix_product) - k:
                return 0
        if k >= len(self.prefix_product): 
            return self.prefix_product[-1]
        else:
            return self.prefix_product[-1] // self.prefix_product[-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)