# Method 1: Python set()


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_num1 = set()
        set_num2 = set()

        for num in nums1:
            if num not in set_num1:
                set_num1.add(num)

        for num in nums2:
            if num not in set_num2:
                set_num2.add(num)

        ans = set_num1.intersection(set_num2)

        return list(ans)


# Method 2: Hash array

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = [0] * 1000
        count2 = [0] * 1000

        for num in nums1:
            count1[num] += 1

        for num in nums2:
            count2[num] += 1
        
        ans = []

        for i in range(len(count1)):
            if count1[i] != 0 and count2[i] != 0:
                ans.append(i)
        
        return ans
        
# Method 3: dict + ans array

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        val_dic = {}
        ans = []

        for num in nums1:
            val_dic[num] = 1
        
        for num in nums2:
            if num in val_dic.keys() and val_dic[num] == 1:
                ans.append(num)
                # 去重
                val_dic[num] = 0
        
        return ans 
