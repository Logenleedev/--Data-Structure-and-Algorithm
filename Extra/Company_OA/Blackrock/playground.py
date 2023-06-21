'''
USD,CAD,1.3;USD,GBP,0.71;USD,JPY,109;GBP,JPY,155
USD
JPY
'''



import sys

conversion_rate = sys.stdin.readline().strip()  # read first line
conversion = conversion_rate.split(";")  # Separate string into an array of strings by ";"
# e.g. ["USD,JPY,109", "USD,GBP,0.71"]

currency1 = sys.stdin.readline().strip()  # read first currency
currency2 = sys.stdin.readline().strip()  # read target currency

if currency2 == currency1:  # if both currencies are the same, return 0
    print(1)
    sys.exit()

queue = []  # to store the graph and perform breadth-first search
visited = []  # to keep track of visited currencies


for temp in conversion:
    conversion_one = temp.split(",")  # separate currencies and conversion rate
    # e.g. ["USD", "JPY", 109]


    if conversion_one[0] == currency1:
        queue.append(conversion_one[1])  # add currency not visited yet
        queue.append(conversion_one[2])  # add rate
    elif conversion_one[1] == currency1:
        d = 1 / float(conversion_one[2])  # invert the conversion rate
        d = round(d, 2)  # round up to two decimal places
        queue.append(conversion_one[0])  # add currency not visited
        queue.append(str(d))  # add its rate

visited.append(currency1)  # currency1 already visited, add it to the visited list
max_conversion_rate = -1.0  # to calculate the maximum conversion rate

while queue:
    currency = queue.pop(0)  # pop the first element of the queue, i.e., currency
    rate = float(queue.pop(0))  # pop the first element of the queue, i.e., rate

    if currency == currency2:  # check whether it is the target currency
        if rate > max_conversion_rate:  # update max_conversion_rate
            max_conversion_rate = rate
    else:
        for temp in conversion:
            conversion_one = temp.split(",")

            if conversion_one[0] == currency and currency not in visited:
                # check new currency that has not been visited earlier
                d = float(conversion_one[2])
                d = d * rate  # multiply the rate of multiple currencies to achieve the result
                d = round(d, 2)  # round up to two decimal places
                queue.append(conversion_one[1])  # add currency
                queue.append(str(d))  # add to the queue
            elif conversion_one[1] == currency and currency not in visited:
                d = 1 / float(conversion_one[2])  # invert the rate
                d = d * rate  # multiply the rate of multiple currencies to achieve the result
                d = round(d, 2)  # round up to two decimal places
                queue.append(conversion_one[0])  # add currency
                queue.append(str(d))  # add its rate

        visited.append(currency)  # update the visited list as all the nodes of the currency have been visited

print(max_conversion_rate)  # print the maximum currency conversion
