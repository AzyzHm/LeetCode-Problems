class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import Counter
        
        def backtrack(counter):
            total = 0
            for tile in counter:
                if counter[tile] > 0:
                    total += 1
                    counter[tile] -= 1
                    total += backtrack(counter)
                    counter[tile] += 1
            return total
        
        counter = Counter(tiles)
        return backtrack(counter)

solution = Solution()
print(solution.numTilePossibilities("AAB"))
print(solution.numTilePossibilities("AAABBC"))