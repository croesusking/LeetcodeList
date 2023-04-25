class SmallestInfiniteSet:
    #LC2336 - Smallest Number in Infinite Set
    st = set(())
    def __init__(self):
        for i in range(1, 1001):
            self.st.add(i)

    def popSmallest(self) -> int:
        mn = min(self.st)
        self.st.remove(mn)
        return mn

    def addBack(self, num: int) -> None:
        self.st.add(num)