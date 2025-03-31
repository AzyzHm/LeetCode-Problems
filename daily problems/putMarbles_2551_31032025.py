from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1:
            return 0
        
        pair_scores = [weights[i] + weights[i + 1] for i in range(n - 1)]
        pair_scores.sort()
        
        max_score = sum(pair_scores[-(k-1):])
        min_score = sum(pair_scores[:k-1])
        
        return max_score - min_score

# Example usage:
print(Solution().putMarbles([1, 3, 5, 1], 2))  # Output: 4
print(Solution().putMarbles([1, 3], 2))        # Output: 0