#offer a function to read a file as a numpy arary.
import numpy as np
class ReadNP(object):
    def __init__(self,fileName, k = 1):

        self.fileName = fileName
        self.npData       = None
        self.npDataT      = None
        self.toNp(k)

    def toNp(self, k):
        
        self.npData  = np.loadtxt(self.fileName)
        self.npDataT = self.npData.T
        
        self.xaXis = self.npDataT[0]
        self.yaXis = self.npDataT[k]  

class ReadString(object):
    def __init__(self, x):
        self.fileName = None
        self.int    = None

    def readString(self, fileName):
        fileH       = open(fileName, r)
        lines       = fileH.readlines()

if __name__ == '__main__':
    instanceOfReadNP = ReadNP('forPlot')
    print instanceOfReadNP.npData.T

