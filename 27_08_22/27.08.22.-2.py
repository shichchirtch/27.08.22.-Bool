class Vector:
    def __init__(self, *args):
        self.arr=[]
        for x in args:
            if isinstance(x, (int, float)):
                self.arr.append(x)
    def __len__(self):
        print("__len__")
        return len(self.arr)

    def compare_len(self, other):
        if len(self) == len(other):
            return True
        else:
            raise ArithmeticError('размерности векторов не совпадают')

    def __add__(self, other):
        if self.compare_len(other):
            new_arr = []
            for x, y in zip(self.arr, other.arr):
                new_arr.append(x+y)
            new_vec = Vector(*new_arr)
            return new_vec
    def __iadd__(self, other):
        if type(other) == Vector:
            if self.compare_len(other):
                for x in range (len(self.arr)):
                    self.arr[x] = self.arr[x]+other.arr[x]
                return self
        if type(other) in (int, float):
            for x in range(len(self.arr)):
                self.arr[x] = self.arr[x]+other
            return self

    def __sub__(self, other):
        if self.compare_len(other):
            new_arr = []
            for x, y in zip(self.arr, other.arr):
                new_arr.append(x-y)
            new_vec = Vector(*new_arr)
            return new_vec

    def __isub__(self, other):
        if type(other) == Vector:
            if self.compare_len(other):
                for x in range (len(self.arr)):
                    self.arr[x] = self.arr[x]-other.arr[x]
                return self
        if type(other) in (int, float):
            for x in range(len(self.arr)):
                self.arr[x] = self.arr[x]-other
            return self
    def __mul__(self, other):
        if self.compare_len(other):
            new_arr = []
            for x, y in zip(self.arr, other.arr):
                new_arr.append(x*y)
            new_vec = Vector(*new_arr)
            return new_vec
    def __eq__(self, other):
        return self.arr==other.arr




p1 = [5,2,9]
p2 = [1,2,3,]
v1 = Vector(*p1)
v2 = Vector(*p2)
print(v2.arr)
print(len(v1), len(v2))
# print(v1!=v2)
v_res = v1-v2
print("v_res= ", v_res.arr)
# v1+=10
# # print(v1.arr)
# v_res+=v1
# print(v_res.arr)
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print("****************************************************",(v1 + v2).arr)  # [5, 7, 9]
print((v1 - v2).arr)  # [-3, -3, -3]
print((v1 * v2).arr)  # [4, 10, 18]

v1 += 10
print(v1.arr)  # [11, 12, 13]
v1 -= 10
print(v1.arr)  # [1, 2, 3]
v1 += v2
print(v1.arr)  # [5, 7, 9]
v2 -= v1
print(v2.arr)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True
