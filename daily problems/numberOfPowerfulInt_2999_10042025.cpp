#include <iostream>
#include <vector>
#include <string>
#include <cstring>

class Solution {
 public:
  long long numberOfPowerfulInt(long long start, long long finish, int limit, std::string s) {
    std::string a = std::to_string(start);
    std::string b = std::to_string(finish);
    std::string aWithLeadingZeros = std::string(b.length() - a.length(), '0') + a;
    std::vector<std::vector<std::vector<long>>> mem(
        b.length(), std::vector<std::vector<long>>(2, std::vector<long>(2, -1)));
    std::string sWithLeadingZeros = std::string(b.length() - s.length(), '0') + s;
    return count(aWithLeadingZeros, b, 0, limit, s, true, true, mem);
  }

 private:
  long count(const std::string& a, const std::string& b, int i, int limit,
             const std::string& s, bool tight1, bool tight2,
             std::vector<std::vector<std::vector<long>>>& mem) {
    if (i + s.length() == b.length()) {
      std::string aMinSuffix = tight1 ? std::string(a.end() - s.length(), a.end())
                                      : std::string(s.length(), '0');
      std::string bMaxSuffix = tight2 ? std::string(b.end() - s.length(), b.end())
                                      : std::string(s.length(), '9');
      long suffix = std::stoll(s);
      return std::stoll(aMinSuffix) <= suffix && suffix <= std::stoll(bMaxSuffix);
    }

    if (mem[i][tight1][tight2] != -1)
      return mem[i][tight1][tight2];

    long res = 0;
    int minDigit = tight1 ? a[i] - '0' : 0;
    int maxDigit = tight2 ? b[i] - '0' : 9;

    for (int d = minDigit; d <= maxDigit; ++d) {
      if (d > limit)
        continue;
      bool nextTight1 = tight1 && (d == minDigit);
      bool nextTight2 = tight2 && (d == maxDigit);
      res += count(a, b, i + 1, limit, s, nextTight1, nextTight2, mem);
    }

    return mem[i][tight1][tight2] = res;
  }
};