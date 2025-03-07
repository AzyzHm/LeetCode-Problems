from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Helper function to generate prime numbers up to n using the Sieve of Eratosthenes
        def sieve(n):
            is_prime = [True] * (n + 1)
            p = 2
            while p * p <= n:
                if is_prime[p]:
                    for i in range(p * p, n + 1, p):
                        is_prime[i] = False
                p += 1
            primes = []
            for p in range(2, n + 1):
                if is_prime[p]:
                    primes.append(p)
            return primes
        
        # Generate all prime numbers up to right
        primes = sieve(right)
        
        # Filter primes within the range [left, right]
        primes_in_range = [p for p in primes if left <= p <= right]
        
        # Find the closest primes
        if len(primes_in_range) < 2:
            return [-1, -1]
        
        min_diff = float('inf')
        closest_pair = [-1, -1]
        for i in range(1, len(primes_in_range)):
            diff = primes_in_range[i] - primes_in_range[i - 1]
            if diff < min_diff:
                min_diff = diff
                closest_pair = [primes_in_range[i - 1], primes_in_range[i]]
        
        return closest_pair

solution = Solution()
print(solution.closestPrimes(10, 19))  # Output: [11, 13]
print(solution.closestPrimes(4, 6))    # Output: [-1, -1]