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

    def size(self):
        return len(self.lists), len(self.lists[0])


exec(stdin.read())
