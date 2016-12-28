try:
    import Image 
except:
    from PIL import Image

class Zfcf(object):
    def __init__(self):
        self.file     = None
        self.crop     = None
        self.fileName = None
        self.region   = None
    def setName(self, fileName):
        self.fileName = str(fileName)
        self.file     = Image.open(self.fileName)
    def setRegion(self, x1, y1, x2, y2):
        self.region = (x1, y1, x2, y2)
        self.crop   = self.file.crop(self.region)
        self.crop.show()
        self.crop.save("crop_" + self.fileName)

def runCrop(fileName, x1, y1, x2, y2):
    img = Zfcf()
    img.setName(fileName)
    img.setRegion(x1, y1, x2, y2)
    

if __name__ == "__main__":
    runCrop("1.jpg",0,0,400,400)
    
    
