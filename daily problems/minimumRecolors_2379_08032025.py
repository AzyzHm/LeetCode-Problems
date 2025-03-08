class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        minimum = float('Inf')
        a = 0
        b = k
        while b <= len(blocks):
            for i in range(a,b):
                if blocks[i] == 'W':
                    count += 1
                else:
                    continue
            minimum = min(count,minimum)
            a += 1
            b += 1
            count = 0
        return minimum
    
solution = Solution()
print(solution.minimumRecolors("WBBWWBBWBW", 7)) # Output : 3
print(solution.minimumRecolors("WBWBBBW", 2)) # Output : 0

            