import random


class DualPivot:
    def __init__(self, input_array, findConstant):
        self.partitionIterations = 0
        self.findConstant = findConstant
        self.constantsList = []
        self.arr = input_array

    def qs(self, k, l, r):
        if r == l:
            return self.arr[l]
        if r-l == 1:
            if k == 0:
                return self.arr[l]
            else:
                return self.arr[r]
        dualPivots = random.sample(range(l, r), 2)
        p = self.partition(dualPivots[0], dualPivots[1], l, r)
        left_length = p[0]-l
        right_length = r-p[1]
        middle_length = p[1]-p[0]-1
        if (left_length+1 == k):
            return self.arr[p[0]]
        elif (left_length+middle_length+2 == k):
            return self.arr[p[1]]
        elif left_length+1 > k:
            if self.findConstant:
                constant = (left_length)/(r-l)
                percent = constant*100
                print("now recurring on a subarray that is " +
                      str(percent) + "% of the original array's size")
                self.constantsList.append(constant)
            return self.qs(k, l, p[0]-1)
        elif (left_length+middle_length+2 > k):
            if self.findConstant:
                constant = (middle_length)/(r-l)
                percent = constant*100
                print("now recurring on a subarray that is " +
                      str(percent) + "% of the original array's size")
                self.constantsList.append(constant)
            return self.qs(k-left_length-1, p[0]+1, p[1]-1)
        else:
            if self.findConstant:
                constant = (right_length)/(r-l)
                percent = constant*100
                print("now recurring on a subarray that is " +
                      str(percent) + "% of the original array's size")
                self.constantsList.append(constant)
            return self.qs(k-(left_length+middle_length+2), p[1]+1, r)

    def partition(self, p1, p2, l, r):

        if self.arr[p1] > self.arr[p2]:
            self.arr[p1], self.arr[p2] = self.arr[p2], self.arr[p1]

        idx_l, idx_r = l, r
        p1_val, p2_val = self.arr[p1], self.arr[p2]
        self.arr[l], self.arr[p1] = self.arr[p1], self.arr[l]
        self.arr[r], self.arr[p2] = self.arr[p2], self.arr[r]

        idx_l += 1
        idx_r -= 1
        m = idx_l

        while m <= idx_r:
            if self.arr[m] < p1_val:
                self.arr[idx_l], self.arr[m] = self.arr[m], self.arr[idx_l]
                idx_l += 1
                m += 1
            elif self.arr[m] > p2_val:
                self.arr[m], self.arr[idx_r] = self.arr[idx_r], self.arr[m]
                idx_r -= 1
            else:
                m += 1

        idx_l -= 1
        idx_r += 1

        self.arr[l], self.arr[idx_l] = self.arr[idx_l], self.arr[l]
        self.arr[idx_r], self.arr[r] = self.arr[r], self.arr[idx_r]
        return [idx_l, idx_r]
