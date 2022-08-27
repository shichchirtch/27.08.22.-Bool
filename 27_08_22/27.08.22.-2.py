class Vector:
    def __init__(self, *args):
        self.arr=[]
        for x in args:
            if isinstance(x, (int, float)):
                self.arr.append(x)
    def __len__(self):
        return len(self.arr)
    def compare_len(self, other):
        if len(self) == len(other):
            return True
        raise ArithmeticError('размерности векторов не совпадают')

    def __add__(self, other):
        if other.compare_len(other):
            new_arr = []
            for x, y in zip(self.arr, other.arr):
                new_arr.append(x+y)
            new_vec = Vector(*new_arr)
            return new_vec
    def __iadd__(self, other):
        if type(other) == Vector:
            if other.compare_len(other):
                for x in range (len(self.arr)):
                    self.arr[x] = self.arr[x]+other.arr[x]
                return self
        if type(other) in (int, float):
            for x in range(len(self.arr)):
                self.arr[x] = self.arr[x]+other
            return self

    def __sub__(self, other):
        if other.compare_len(other):
            new_arr = []
            for x, y in zip(self.arr, other.arr):
                new_arr.append(x-y)
            new_vec = Vector(*new_arr)
            return new_vec

    def __isub__(self, other):
        if type(other) == Vector:
            if other.compare_len(other):
                for x in range (len(self.arr)):
                    self.arr[x] = self.arr[x]-other.arr[x]
                return self
        if type(other) in (int, float):
            for x in range(len(self.arr)):
                self.arr[x] = self.arr[x]-other
            return self
    def __eq__(self, other):
        return self.arr==other.arr



p1 = [1,2,3]
p2 = [0,2,3]
v1 = Vector(*p1)
v2 = Vector(*p2)
print(v1!=v2)
v_res = v1-v2
print(v_res.arr)
# v1+=10
# print(v1.arr)
v_res+=v1
print(v_res.arr)
