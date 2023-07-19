import math
import random


class FloydRivest:
    def __init__(self, input_array):
        self.partitionIterations = 0
        self.arr = input_array

    def sign(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        return 0

    def select(self, k: int, left: int,
               right: int):
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
                sd = 0.5 * math.sqrt(z * s * (n-s)/n) * self.sign(i-n / 2)
                newLeft = int(max(left, k-i * s / n + sd))
                newRight = int(min(right, k + (n - i) * s / n + sd))
                self.select(k, newLeft, newRight)
            t = self.arr[k]
            i = left
            j = right
            self.arr[left], self.arr[k] = self.arr[k], self.arr[left]
            if self.arr[right] > t:
                self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
            while i < j:
                self.partitionIterations += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i = i + 1
                j = j-1
                while self.arr[i] < t:
                    i = i + 1
                while self.arr[j] > t:
                    j = j-1

            if self.arr[left] == t:
                self.arr[left], self.arr[j] = self.arr[j], self.arr[left]
            else:
                j = j + 1
                self.arr[right], self.arr[j] = self.arr[j], self.arr[right]

            # Updating the left and right indices
            # depending on position of k-th element
            if j <= k:
                left = j + 1
            if k <= j:
                right = j-1
        return self.arr[k]
