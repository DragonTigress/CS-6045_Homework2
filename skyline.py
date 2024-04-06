# def process_inputs(input_lists):
#     height = []
#     left = []
#     right = []
#     for line in input_lists:
#         inputs = line.split(', ')
#         height.append(inputs[0])
#         left.append ((inputs[1], (-inputs[0])))
#         right.append((inputs[2], inputs[0]))

#     return height, left, right

# def skyline(height, left, right):
#     points = []
#     temp_Height = height
#     temp_x = left
#     # if we don't sort, the first in line will be starting point, append the first point
#     if temp_Height != height:
    
#     else:
#         points.append((temp_Height, temp_x))

# height, left, right = process_input(input_lists)
# points = skyline(height, left_right)
# # Hi , Lxi , Rxi
# input_lists = [
#     (6, 1, 6),
#     (8, 3, 5),
#     (4, 4, 9),
#     (2, 7, 12)
#     (7, 11, 14),
# ]
# (1, 6), (6, 6), (3, 8), (5, 8), (4, 4), (9, 4), (7, 2), (12, 2), (11, 7), (14, 7)
# expected result
# Hi, X
# output = [
#     (6, 1),
#     (8, 3),
#     (6, 5),
#     (4, 6),
#     (2, 9),
#     (7, 11),
#     (0, 14),
# ]

class Building:
    def __init__(self, ht, left, right):
        self.left = left
        self.ht = ht
        self.right = right

class Strip:
    def __init__(self, left=0, ht=0):
        self.left = left
        self.ht = ht

class SkyLine:
    def __init__(self, cap):
        self.arr = []
        self.capacity = cap
        self.n = 0

    def count(self):
        return self.n

    def merge(self, other):
        res = SkyLine(self.n + other.n)
        h1, h2, i, j = 0, 0, 0, 0
        while i < self.n and j < other.n:
            if self.arr[i].left < other.arr[j].left:
                x1, h1 = self.arr[i].left, self.arr[i].ht
                maxh = max(h1, h2)
                res.append(Strip(x1, maxh))
                i += 1
            else:
                x2, h2 = other.arr[j].left, other.arr[j].ht
                maxh = max(h1, h2)
                res.append(Strip(x2, maxh))
                j += 1
        while i < self.n:
            res.append(self.arr[i])
            i += 1
        while j < other.n:
            res.append(other.arr[j])
            j += 1
        return res

    def append(self, st):
        if self.n > 0 and self.arr[self.n-1].ht == st.ht:
            return
        if self.n > 0 and self.arr[self.n-1].left == st.left:
            self.arr[self.n-1].ht = max(self.arr[self.n-1].ht, st.ht)
            return
        self.arr.append(st)
        self.n += 1

    def print_skyline(self):
        print("Skyline for given buildings is")
        for i in range(self.n):
            print(" ({}, {}),".format(self.arr[i].ht, self.arr[i].left), end="")
        print()

def find_skyline(arr, l, h):
    if l == h:
        res = SkyLine(2)
        res.append(Strip(arr[l].left, arr[l].ht))
        res.append(Strip(arr[l].right, 0))
        return res
    mid = (l + h) // 2
    sl = find_skyline(arr, l, mid)
    sr = find_skyline(arr, mid+1, h)
    res = sl.merge(sr)
    return res

arr = [Building(6, 1, 6), Building(8, 3, 5), Building(4, 4, 9), Building(2, 7, 12), Building(7, 11, 14)]
n = len(arr)
skyline = find_skyline(arr, 0, n-1)
skyline.print_skyline()