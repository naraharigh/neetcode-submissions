class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        print(merged)
        for current in intervals[1:]:
            last_merged = merged[-1]
            print(last_merged)
            if current[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current[1])
            else:  
                merged.append(current)
            
        return merged  