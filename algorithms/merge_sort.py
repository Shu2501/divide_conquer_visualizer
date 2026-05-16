def merge_sort(arr, left, right):

    # Base case
    if left >= right:
        return

    # Middle index
    mid = (left + right) // 2

    # Sort left half
    yield from merge_sort(arr, left, mid)

    # Sort right half
    yield from merge_sort(arr, mid + 1, right)

    # Merge sorted halves
    yield from merge(arr, left, mid, right)


def merge(arr, left, mid, right):

    left_part = arr[left:mid + 1]

    right_part = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    # Merge both halves
    while i < len(left_part) and j < len(right_part):

        colors = ["#00ADB5"] * len(arr)

        # Left partition
        for x in range(left, mid + 1):
            colors[x] = "#4CAF50"

        # Right partition
        for x in range(mid + 1, right + 1):
            colors[x] = "#2196F3"

        # Current merge index
        colors[k] = "#FFC107"

        if left_part[i] <= right_part[j]:

            arr[k] = left_part[i]

            i += 1

        else:

            arr[k] = right_part[j]

            j += 1

        k += 1

        # Yield AFTER updating
        yield arr, colors

    # Remaining left elements
    while i < len(left_part):

        colors = ["#00ADB5"] * len(arr)

        colors[k] = "#FFC107"

        arr[k] = left_part[i]

        i += 1
        k += 1

        yield arr, colors

    # Remaining right elements
    while j < len(right_part):

        colors = ["#00ADB5"] * len(arr)

        colors[k] = "#FFC107"

        arr[k] = right_part[j]

        j += 1
        k += 1

        yield arr, colors