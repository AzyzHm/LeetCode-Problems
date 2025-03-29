#include <vector>
#include <queue>
#include <algorithm>
#include <tuple>
#include <cstring>

class Solution {
 public:
    std::vector<int> maxPoints(std::vector<std::vector<int>>& grid, std::vector<int>& queries) {
        const int m = grid.size();
        const int n = grid[0].size();
        const int dirs[5] = {-1, 0, 1, 0, -1};
        std::vector<int> ans(queries.size());
        std::vector<std::pair<int, int>> indexedQueries;
        std::priority_queue<std::tuple<int, int, int>, std::vector<std::tuple<int, int, int>>, std::greater<>> minHeap;
        bool visited[m][n];

        std::memset(visited, 0, sizeof(visited));
        visited[0][0] = true;
        minHeap.emplace(grid[0][0], 0, 0);

        for (int i = 0; i < queries.size(); ++i) {
            indexedQueries.emplace_back(queries[i], i);
        }

        std::sort(indexedQueries.begin(), indexedQueries.end());

        int accumulate = 0;

        for (const auto& [query, queryIndex] : indexedQueries) {
            while (!minHeap.empty() && std::get<0>(minHeap.top()) < query) {
                const auto [val, i, j] = minHeap.top();
                minHeap.pop();
                ++accumulate;

                for (int k = 0; k < 4; ++k) {
                    const int x = i + dirs[k];
                    const int y = j + dirs[k + 1];
                    if (x >= 0 && x < m && y >= 0 && y < n && !visited[x][y]) {
                        visited[x][y] = true;
                        minHeap.emplace(grid[x][y], x, y);
                    }
                }
            }
            ans[queryIndex] = accumulate;
        }

        return ans;
    }
};
