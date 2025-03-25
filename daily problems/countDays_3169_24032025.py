class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        
        merged_meetings = []
        for start, end in meetings:
            if not merged_meetings or merged_meetings[-1][1] < start:
                merged_meetings.append([start, end])
            else:
                merged_meetings[-1][1] = max(merged_meetings[-1][1], end)
        
        total_meeting_days = 0
        for start, end in merged_meetings:
            total_meeting_days += end - start + 1

        return days - total_meeting_days

solution = Solution()
print(solution.countDays(6, [[1, 3], [2, 4], [3, 5]]))  # Output: 1
print(solution.countDays(7, [[2, 4], [1, 3], [5, 6]]))  # Output: 1
print(solution.countDays(7, [[2, 4], [1, 3], [5, 7]]))  # Output: 0