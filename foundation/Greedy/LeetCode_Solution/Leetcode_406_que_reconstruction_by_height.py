class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))


        que = []


        for ele in people:
            que.insert(ele[1], ele)

        return que