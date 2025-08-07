class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = {}
        count2 = {}
        
        for i in nums1:
            if i in count1:
                count1[i] += 1
            else:
                count1[i] = 1

        for j in nums2:
            if j in count2:
                count2[j] += 1
            else:
                count2[j] = 1

        result = []

        for x in count1:
            if x in count2:
                min_count = count1[x] if count1[x] < count2[x] else count2[x]
                for _ in range(min_count):
                    result.append(x)

        return result