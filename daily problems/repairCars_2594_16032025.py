class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        def canRepairInTime(time: int) -> bool:
            total_cars = 0
            for rank in ranks:
                total_cars += int((time // rank) ** 0.5)
                if total_cars >= cars:
                    return True
            return total_cars >= cars

        left, right = 1, min(ranks) * cars * cars
        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid
            else:
                left = mid + 1
        return left
    
print(Solution().repairCars([4, 2, 3, 1], 10))  # Output: 16