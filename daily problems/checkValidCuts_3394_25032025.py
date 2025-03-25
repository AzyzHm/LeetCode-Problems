class Solution:
    def checkValidCuts(self, n, rectangles):
        def countMerged(intervals):
            intervals.sort()
            count = 0
            prev_end = 0
            for start, end in intervals:
                if start < prev_end:
                    prev_end = max(prev_end, end)
                else:
                    prev_end = end
                    count += 1
            return count

        x_intervals = [(rect[0], rect[2]) for rect in rectangles]
        y_intervals = [(rect[1], rect[3]) for rect in rectangles]

        return max(countMerged(x_intervals), countMerged(y_intervals)) >= 3
