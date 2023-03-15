class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ref_1 = dict()
        ref_2 = dict()

        results = []

        for num in nums1:
            ref_1[num] = ref_1.get(num, 0) + 1
        
        for num in nums2:
            ref_2[num] = ref_2.get(num, 0) + 1
        
        for key in ref_1.keys():
            if key in ref_2.keys():
                result = min(ref_1[key], ref_2[key])

                while result > 0:

                    results.append(key)
                    result -= 1


        return results
        
# m -> length of num1
# n -> length of num2 

# Time Complexity: O (m + n)
# Space Complexity: O (m + n)