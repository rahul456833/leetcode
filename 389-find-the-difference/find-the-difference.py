class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        table = {}

        for i in s:
            table[i] = table.get(i, 0) + 1

        for i in t:
            if i not in table or table[i] == 0:
                return i
            table[i] -= 1