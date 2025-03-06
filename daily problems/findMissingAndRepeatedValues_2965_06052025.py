class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        # Calculate the maximum value that should be in the grid
        maximum = len(grid[0]) * len(grid)
        
        # Initialize variables to store the repeated and missing values
        repeated = None
        missing = None
        
        # Dictionary to keep track of the occurrences of each number in the grid
        temp = {}
        
        # Iterate through the grid to find the repeated value
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in temp:
                    repeated = grid[i][j]
                else:
                    temp[grid[i][j]] = 1
        
        # Iterate from 1 to maximum to find the missing value
        for i in range(1, maximum + 1):
            if i not in temp:
                missing = i
                break
        
        # Return the repeated and missing values as a list
        return [repeated, missing]

solution = Solution()
grid = [
    [1, 2, 3],
    [4, 6, 6],
    [7, 8, 9]
]
result = solution.findMissingAndRepeatedValues(grid)
print(result)  # Output: [6, 5]

