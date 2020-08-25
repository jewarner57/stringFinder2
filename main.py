from UserInterface import UserInterface
from FileList import FileList

userInterface = UserInterface()

try:
    #create the gui window
    userInterface.createTkWindow()
except:
    #if that fails then use terminal input instead
    print("Interface window Could not be opened... Defaulting to text")
    userInterface.getTerminalInput()

#get the form data from the user input
directoryPath = userInterface.directoryPath
searchString = userInterface.searchString
outputOrder = userInterface.outputOrder

files = FileList(directoryPath)