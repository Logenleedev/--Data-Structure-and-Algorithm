'''
Busiest Time in The Mall
data = [ [1487799425, 14, 1], 
                 [1487799425, 4,  0],
                 [1487799425, 2,  0],
                 [1487800378, 10, 1],
                 [1487801478, 18, 0],
                 [1487801478, 18, 1],
                 [1487901013, 1,  0],
                 [1487901211, 7,  1],
                 [1487901211, 7,  0] ]
'''

from collections import defaultdict

def find_busiest_period(data):
    ref = defaultdict(int)

    for element in data:
        timestamp = element[0]
        count = element[1]
        state = element[2]

        if state == 1:
            ref[timestamp] += count
        elif state == 0:
            ref[timestamp] -= count

   

    max_count = max(ref.values())

    for key, value in ref.items():
        if value == max_count:
            return key 


data = [ [1487799425, 14, 1], 
                 [1487799425, 4,  0],
                 [1487799425, 2,  0],
                 [1487800378, 10, 1],
                 [1487801478, 18, 0],
                 [1487801478, 18, 1],
                 [1487901013, 1,  0],
                 [1487901211, 7,  1],
                 [1487901211, 7,  0] ]

print(find_busiest_period(data))

