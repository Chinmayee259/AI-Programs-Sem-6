# AI 5. Implement Greedy search algorithm for following application Selection Sort & Minimum Spanning Tree
# Selection Sort works by repeatedly finding the smallest element and placing it at the correct position.
# How it works
# 1) Find the minimum element in the array
# 2) Swap it with the first position
# 3) Then find next minimum for second position
# 4) Repeat until array is sorted

# ----------------- Selection sort -------------------
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# ---------- INPUT -----------
arr = list(map(int, input("Enter elements: ").split()))

# ---------- OUTPUT -----------
print("Sorted Array: ", selection_sort(arr))


# Enter elements: 64 25 12 22 11
# Sorted array: [11, 12, 22, 25, 64]