class SmallestInfiniteSet:

    def __init__(self):
        self.removed_elements = set()
        self.min = 1

    def popSmallest(self) -> int:
        prev_min = self.min
        self.removed_elements.add(prev_min)
        self.min += 1
        for _ in range(len(self.removed_elements)):
            if not self.min in self.removed_elements:
                break
            self.min += 1
        return prev_min

    def addBack(self, num: int) -> None:
        if num in self.removed_elements:
            self.removed_elements.remove(num)
            self.min = min(self.min, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
