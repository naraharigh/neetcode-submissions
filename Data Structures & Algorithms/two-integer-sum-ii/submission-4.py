class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        res = []
        def dfs(i, o, target):
            # Replace recursion with a while loop to avoid RecursionError
            while o < len(numbers):
                current_sum = numbers[i] + numbers[o]
                if current_sum == target:
                    res.append(i + 1)
                    res.append(o + 1)
                    return
                elif current_sum > target:
                    # Since array is sorted, if sum is too large, stop checking this i
                    break
                o += 1

        for i in range(len(numbers)):
            dfs(i, i + 1, target)
            if res:
                return res