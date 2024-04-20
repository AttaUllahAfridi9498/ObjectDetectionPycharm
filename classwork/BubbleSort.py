def bubble_sort(list):
    n = len(list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                # Swap elements
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True

        # If no swapping occurred in this pass, the array is already sorted
        if not swapped:
            break
    return list

# Example usage:
list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(list)
print("Sorted array:", sorted_list)
