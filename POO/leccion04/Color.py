class Color:
    def __init__(self, color) -> None:
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def coor(self, color):
        self._color = color

    def __str__(self) -> str:
        return f'{super().__str__()} - color: {self._color}'