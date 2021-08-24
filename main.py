def smallest_diff(arr_1, arr_2):  # First Solution, but the runtime is O(n^2)
    smallest = float('inf')
    pair = [0, 0]

    for n1 in arr_1:
        for n2 in arr_2:
            diff = abs(n1 - n2)  # get always the absolute value of the difference

            if diff < smallest:  # new smallest
                smallest = diff
                pair[0] = n1
                pair[1] = n2

    print("%d. That is, the pair {%d, %d}" % (smallest, pair[0], pair[1]))


def opt_smallest_diff(arr_1, arr_2):  # Optimization of the first solution; runtime is O(n log n)
    # Sort both arrays
    arr_1.sort()
    arr_2.sort()

    smallest = float('inf')
    pair = [0, 0]
    i = 0  # Index of arr_1
    j = 0  # Index of arr_2

    # Instead of a nested loop, we go through one array at a time depending on the current number
    while i < len(arr_1) and j < len(arr_2):

        diff = abs(arr_1[i] - arr_2[j])

        if diff < smallest:  # new smallest
            smallest = diff
            pair[0] = arr_1[i]
            pair[1] = arr_2[j]

        # Add index of the array with the current smaller value
        if arr_1[i] < arr_2[j]:
            i += 1
        else:
            j += 1

    print("%d. That is, the pair {%d, %d}" % (smallest, pair[0], pair[1]))


def run_tests():  # Automated Tests
    ipt_file = open('inputs.txt')
    inputs = ipt_file.readlines()

    for arrays in inputs:
        arrays = arrays.split(', ')

        array_1 = [int(n) for n in arrays[0].split(' ')]
        array_2 = [int(n) for n in arrays[1].split(' ')]

        print("<Input: {}, {}>".format(array_1, array_2))
        print("First solution:")
        smallest_diff(array_1, array_2)

        print("\nOptimized solution:")
        opt_smallest_diff(array_1, array_2)
        print()


run_tests()  # Run automated tests

# Manual Inputs
# array_1 = input().split(" ")
# array_2 = input().split(" ")
#
# array_1 = [int(n) for n in array_1]
# array_2 = [int(n) for n in array_2]
#
# print("First solution:")
# smallest_diff(array_1, array_2)
#
# print("\nOptimized solution:")
# opt_smallest_diff(array_1, array_2)
