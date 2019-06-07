def countTriplets(arr, r):
    count = 0
    dict = {}
    dictPairs = {}

    for i in reversed(arr):
        print("i: " + str(i))
        if i * r in dictPairs:
            count += dictPairs[i * r]
            print("count: " + str(count))
        if i * r in dict:
            dictPairs[i] = dictPairs.get(i, 0) + dict[i * r]
            print("dictPairs: " + str(dictPairs))

        dict[i] = dict.get(i, 0) + 1
        print("dict: " + str(dict))

    return count

a = [1,2,1,2,4]


count = countTriplets(a,2)
print(count)