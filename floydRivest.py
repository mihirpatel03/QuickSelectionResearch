import math
import random

# Function to return the
# sign of the number


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0

# Function to return kth smallest number


def select(arr: list, left: int,
           right: int, k: int):
    while right > left:

        # Choosing a small subarray
        # S based on sampling.
        # 600, 0.5 and 0.5 are
        # arbitrary constants
        if right-left > 600:
            n = right - left + 1
            i = k - left + 1
            z = math.log(n)
            s = 0.5 * math.exp(2 * z / 3)
            sd = 0.5 * math.sqrt(z * s * (n-s)/n) * sign(i-n / 2)
            newLeft = int(max(left, k-i * s / n + sd))
            newRight = int(min(right, k + (n - i) * s / n + sd))
            select(arr, newLeft, newRight, k)
        t = arr[k]
        i = left
        j = right
        arr[left], arr[k] = arr[k], arr[left]
        if arr[right] > t:
            arr[left], arr[right] = arr[right], arr[left]
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
            j = j-1
            while arr[i] < t:
                i = i + 1
            while arr[j] > t:
                j = j-1

        if arr[left] == t:
            arr[left], arr[j] = arr[j], arr[left]
        else:
            j = j + 1
            arr[right], arr[j] = arr[j], arr[right]

        # Updating the left and right indices
        # depending on position of k-th element
        if j <= k:
            left = j + 1
        if k <= j:
            right = j-1
    return arr[k]
