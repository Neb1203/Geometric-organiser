from Window import Window
from PIL import Image
window = Window()
class CenterButton:
    def centerButtonWidth(self, filePath):
        image = Image.open(filePath)
        width = image.width

        centerWidth = 1/2 * (window.vduDimensions[0] - width)
        return centerWidth

    def centerButtonHeight(self, filePath, totalNumButtons, margins, buttonNum):
        image = Image.open(filePath)
        self.height = image.height
        self.centerHeight = 1 / 2 * (window.vduDimensions[1] - ((self.height * (totalNumButtons+1)) + (margins * totalNumButtons)))
        if buttonNum > totalNumButtons:
            print("Error: button number immpossibe")
        elif buttonNum == 0:
            return self.centerHeight
        elif buttonNum > 0:
            self.centerHeight = self.centerHeight + ((buttonNum + 1) * (self.height + 20))
            return self.centerHeight