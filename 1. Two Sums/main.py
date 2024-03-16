def main():
    def twoSum( nums, target) -> list[int]:
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            dict[nums[i]] = i
        return []
    print(twoSum([2, 7, 11, 15], 9)) # [0, 1]
    print(twoSum([3, 2, 4], 6)) # [1, 2]
    print(twoSum([3, 3], 6)) # [0, 1]

if __name__ == "__main__":
    main()