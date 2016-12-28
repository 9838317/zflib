"""
This program enables to generate a list, either sorted or un sorted.

_____________
ran(len, max):       return a list       with
    length : len, 
    maximum: max

_____________
ranSorted(len, max): return a sorted list with
    length : len, 
    maximum: max

_____________
ranSortTest(target, len(optional), range(optional)):
randomly generate a sorted list, and then see whether the target is in the list.


"""
import random

#instaltiate a new class for storing the array
class Random(object):
    def __init__(self, lengthOfList = 100, ranger = 10000):
        self.ranList      = None 
        self.initial(lengthOfList, ranger)
        
    def initial(self, lengthOfList, ranger):
        if self.ranList is None:
            self.ran(lengthOfList, ranger)

    #generate a new array if it is none.
    def ran(self, lengthOfList = None, ranger = None):
        if lengthOfList != None and ranger != None:
            
            ranList = []
            for i in range(lengthOfList):
                ranList.append(int(random.random() * ranger))
                
            self.ranList = ranList
            return ranList
        elif lengthOfList == None or ranger == None:
            return self.ranList

    def ranSorted(self, lengthOfList = None, ranger = None):
        if lengthOfList == None or ranger == None:
            return sorted(instanceOfRandom.ranList)
        else:
            return sorted(self.ran(lengthOfList, ranger))

    def ranSortTest(self, target, lengthOfList = 100, ranger = 10000):
        if type(ranger) == list:
            rantestList = ranger
        else:
            rantestList = self.ranSorted(lengthOfList, ranger)
            
        if target not in rantestList:
            key = False
        else:
            key = rantestList.index(target)
        return [rantestList,key]    


if __name__ == '__main__':
    instanceOfRandom = Random()
    print Random().ranSortTest(100)
    print Random().ranSortTest(6, 1000, [1,2,3,4,5,6,8])
