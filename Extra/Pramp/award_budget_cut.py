

def find_grants_cap(grantsArray, newBudget):
    arr = sorted(grantsArray)
    count = len(grantsArray)
    newBudget = float(newBudget)

    for i in range(len(arr)):
        award = arr[i] * count

        if award > newBudget:
            return newBudget / count



        newBudget -= arr[i]
        count -= 1

print(find_grants_cap([2, 100, 50, 120, 1000], 190))


# Time Complexity: O(n)
# Space Complexity: O(1)