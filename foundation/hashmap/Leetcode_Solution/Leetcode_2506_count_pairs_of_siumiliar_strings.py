# Time Complexity: O(n^2)
class Solution:
    def similarPairs(self, words: List[str]) -> int:


        if len(words) <= 1:
            return 0

        count = 0


        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                a = set(words[i])
                b = set(words[j])
                if a == b:
                    count += 1
        return count