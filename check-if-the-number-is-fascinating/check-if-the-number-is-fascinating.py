class Solution:
    def isFascinating(self, n: int) -> bool:
        m = str(n) + str(n*2) + str(n*3)
        return set(m) == {"1", "2", "3", "4", "5", "6", "7", "8", "9"} and set(collections.Counter(m).values()) == {1}