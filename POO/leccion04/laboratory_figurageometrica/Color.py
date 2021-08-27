class Color:
    def __init__(self, color) -> None:
        self._color = color

    @property
    def getColor(self):
        return self._color
    
    @getColor.setter
    def setColor(self, color):
        self._color = color

    def __str__(self) -> str:
        return f'Color: {self._color}'