class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        
        # Step 1: Compute LCS using DP
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Step 2: Construct the SCS from LCS
        i, j = m, n
        scs = []
        
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:  # Common character, part of LCS
                scs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:  # Move towards max LCS value
                scs.append(str1[i - 1])
                i -= 1
            else:
                scs.append(str2[j - 1])
                j -= 1
        
        # Add remaining characters from str1 and str2
        while i > 0:
            scs.append(str1[i - 1])
            i -= 1
        while j > 0:
            scs.append(str2[j - 1])
            j -= 1
        
        return "".join(reversed(scs))

# Example Usage:
solution = Solution()
print(solution.shortestCommonSupersequence("abac", "cab"))  # Output: "cabac"
print(solution.shortestCommonSupersequence("geek", "eke"))  # Output: "geeke"
print(solution.shortestCommonSupersequence("abc", "ac"))    # Output: "abc"