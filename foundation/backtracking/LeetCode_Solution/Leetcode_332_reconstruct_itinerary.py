from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dict = defaultdict(list)

        for ticket in tickets:
            dict[ticket[0]].append(ticket[1])

        for key in dict.keys():
            # sort lexa order 
            dict[key].sort()

   
        path = ["JFK"]
        def backtracking(startPoint):
            # base case 
            if len(path) == len(tickets) + 1:
                return True 
            
            # choose element from the set 
            for _ in dict[startPoint]:
                element = dict[startPoint].pop(0)
                path.append(element)
                if backtracking(element) == True:
                    return True 
                path.pop()
                dict[startPoint].append(element)


        backtracking("JFK")

        return path 


# Time Complexity: O(n). n -> number of edges
# Space Complexity: O(n). n -> number of edges





