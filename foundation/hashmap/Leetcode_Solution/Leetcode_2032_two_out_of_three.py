# Method 1 - manually drop the duplicate 

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        mapps = dict()
        result = []

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        nums3 = sorted(nums3)
    
        for i in range(len(nums1)):
            if i > 0 and nums1[i] == nums1[i - 1]:
                continue
            mapps[nums1[i]] = 1

        for i in range(len(nums2)):
            if i > 0 and nums2[i] == nums2[i - 1]:
                continue
            if nums2[i] in mapps.keys():
                mapps[nums2[i]] += 1
            else:
                mapps[nums2[i]] = 1

        for i in range(len(nums3)):
            if i > 0 and nums3[i] == nums3[i - 1]:
                continue
            if nums3[i] in mapps.keys():
                mapps[nums3[i]] += 1
            else:
                mapps[nums3[i]] = 1
        
        for key, value in mapps.items():
            if value >= 2:
                result.append(key)
        
        return result


# Method 2: use python API to drop the duplicate 
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        list1 = list(set(nums1))
        list2 = list(set(nums2))
        list3 = list(set(nums3))

        total_list = list1 + list2 + list3

        mapps = dict()
        result = []


        for num in total_list:
            mapps[num] = mapps.get(num, 0) + 1
        
        for key, value in mapps.items():
            if value >= 2:
                result.append(key)
        
        return result


        
        
        