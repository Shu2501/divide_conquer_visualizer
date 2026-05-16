def quick_sort(arr, low, high):

    if low < high:

        pivot_index = yield from partition(
            arr,
            low,
            high
        )

        # Left side
        yield from quick_sort(
            arr,
            low,
            pivot_index - 1
        )

        # Right side
        yield from quick_sort(
            arr,
            pivot_index + 1,
            high
        )


def partition(arr, low, high):

    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        colors = ["#00ADB5"] * len(arr)

        # Pivot color
        colors[high] = "#E91E63"

        # Current comparison
        colors[j] = "#FFD369"

        yield arr, colors

        if arr[j] < pivot:

            i += 1

            # Swap
            arr[i], arr[j] = arr[j], arr[i]

            colors[i] = "#FF5722"
            colors[j] = "#FF5722"

            yield arr, colors

    # Final pivot swap
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    colors = ["#00ADB5"] * len(arr)

    colors[i + 1] = "#9C27B0"

    yield arr, colors

    return i + 1