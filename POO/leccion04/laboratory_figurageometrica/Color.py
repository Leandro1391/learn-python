class Color:
    def __init__(self, color) -> None:
        self._color = color

    @property
    def get_color(self):
        return self._color
    
    @get_color.setter
    def set_color(self, color):
        self._color = color

    def __str__(self) -> str:
        return f'Color: {self._color}'