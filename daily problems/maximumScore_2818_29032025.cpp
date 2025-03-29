#include <vector>
#include <stack>
#include <algorithm>
#include <numeric>
#include <unordered_set>

class Solution {
 public:
    int maximumScore(std::vector<int>& nums, int k) {
        const int n = nums.size();
        const int maxNum = *std::max_element(nums.begin(), nums.end());
        const std::vector<int> minPrimeFactors = computeMinPrimeFactors(maxNum + 1);
        const std::vector<int> primeScores = computePrimeScores(nums, minPrimeFactors);
        int result = 1;
        std::vector<int> left(n, -1);
        std::vector<int> right(n, n);
        std::stack<int> stack;

        // Compute left boundaries
        for (int i = n - 1; i >= 0; --i) {
            while (!stack.empty() && primeScores[stack.top()] <= primeScores[i]) {
                left[stack.top()] = i;
                stack.pop();
            }
            stack.push(i);
        }

        // Compute right boundaries
        stack = std::stack<int>();
        for (int i = 0; i < n; ++i) {
            while (!stack.empty() && primeScores[stack.top()] < primeScores[i]) {
                right[stack.top()] = i;
                stack.pop();
            }
            stack.push(i);
        }

        // Sort numbers with their indices
        std::vector<std::pair<int, int>> numAndIndices;
        for (int i = 0; i < n; ++i) {
            numAndIndices.emplace_back(nums[i], i);
        }

        std::sort(numAndIndices.begin(), numAndIndices.end(),
                            [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
                                return a.first == b.first ? a.second < b.second : a.first > b.first;
                            });

        // Calculate the maximum score
        for (const auto& [num, i] : numAndIndices) {
            const long rangeCount = static_cast<long>(i - left[i]) * (right[i] - i);
            const long actualCount = std::min(rangeCount, static_cast<long>(k));
            k -= actualCount;
            result = static_cast<long>(result) * modPow(num, actualCount) % kMod;
        }

        return result;
    }

 private:
    static constexpr int kMod = 1'000'000'007;

    long modPow(long base, long exp) {
        if (exp == 0) return 1;
        if (exp % 2 == 1) return base * modPow(base % kMod, exp - 1) % kMod;
        return modPow(base * base % kMod, exp / 2) % kMod;
    }

    std::vector<int> computeMinPrimeFactors(int n) {
        std::vector<int> minPrimeFactors(n + 1);
        std::iota(minPrimeFactors.begin() + 2, minPrimeFactors.end(), 2);
        for (int i = 2; i * i < n; ++i) {
            if (minPrimeFactors[i] == i) {
                for (int j = i * i; j < n; j += i) {
                    minPrimeFactors[j] = std::min(minPrimeFactors[j], i);
                }
            }
        }
        return minPrimeFactors;
    }

    std::vector<int> computePrimeScores(const std::vector<int>& nums,
                                                                            const std::vector<int>& minPrimeFactors) {
        std::vector<int> primeScores;
        for (const int num : nums) {
            primeScores.push_back(computePrimeScore(num, minPrimeFactors));
        }
        return primeScores;
    }

    int computePrimeScore(int num, const std::vector<int>& minPrimeFactors) {
        std::unordered_set<int> primeFactors;
        while (num > 1) {
            const int divisor = minPrimeFactors[num];
            primeFactors.insert(divisor);
            while (num % divisor == 0) {
                num /= divisor;
            }
        }
        return primeFactors.size();
    }
};