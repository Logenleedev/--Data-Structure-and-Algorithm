# Method 1: Hash

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        mapps = dict()
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sum = nums1[i] + nums2[j]
                if sum in mapps:
                    mapps[sum] += 1
                else:
                    mapps[sum] = 1
        count = 0
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                key = - nums3[i] - nums4[j]
                if key in mapps.keys():
                    count += mapps[key]
        return count 
        
                        

