from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, lists):
        self.lists = deepcopy(lists)

    def __str__(self):
        strRep = ""
        amount = 0
        for lists in self.lists:
            if amount != 0:
                strRep += "\n"
            new_str = "\t".join(str(elem) for elem in lists)
            strRep += new_str
            amount += 1
        return strRep

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.lists)):
            for j in range(len(self.lists[0])):
                sum = int(self.lists[i][j]) + int(other.lists[i][j])
                numbers.append(sum)
                if len(numbers) == len(self.lists[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

    def __mul__(self, other):
        result = []
        numbers = []
        for i in range(len(self.lists)):
            for j in range(len(self.lists[0])):
                mul = int(self.lists[i][j]) * other
                numbers.append(mul)
                if len(numbers) == len(self.lists[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

    __rmul__ = __mul__

    def size(self):
        return len(self.lists), len(self.lists[0])


exec(stdin.read())
