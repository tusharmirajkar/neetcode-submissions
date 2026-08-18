class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lA = []
        for i, num in enumerate(nums):
            lA.append([num, i])

        lA.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            cur = lA[i][0] + lA[j][0]
            if cur == target:
                return [min(lA[i][1], lA[j][1]),
                        max(lA[i][1], lA[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []


        