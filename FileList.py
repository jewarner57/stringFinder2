from os import listdir
from os.path import isfile, join

class FileList:
    def __init__(self, directoryPath):
        self.path = directoryPath
        self.files = []
        self.getFiles()

    def getFiles(self):
        for fileName in listdir(self.path):

            if isfile(join(self.path, fileName)):
                self.files.append(join(self.path, fileName))
                
        print(self.files)
    
        
    