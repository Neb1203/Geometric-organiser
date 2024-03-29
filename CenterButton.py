from Window import Window
from PIL import Image
window = Window()
class CenterButton:
    def centerButtonWidth(self, width):
        centerWidth = 1/2 * (window.vduDimensions[0] - width)
        return centerWidth

    def centerButtonHeight(self, height, totalNumButtons, margins, buttonNum):
        self.height = height
        self.centerHeight = 1 / 2 * (window.vduDimensions[1] - ((self.height * (totalNumButtons + 1)) + (margins * totalNumButtons)))
        if buttonNum > totalNumButtons:
            print("Error: button number immpossibe")
        elif buttonNum == 0:
            return self.centerHeight
        elif buttonNum > 0:
            self.centerHeight = self.height - self.centerHeight + ((buttonNum + 1) * (self.height + 20))
            return self.centerHeight