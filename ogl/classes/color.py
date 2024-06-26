class Color:
    def __init__(self, r:int, g:int, b:int) -> None:
        self.r = r
        self.g = g
        self.b = b
    def value(self) -> tuple[int, int, int]:
        return (self.r ,self.g, self.b)
    def Not(self):
        r = self.r + 50 % 255
        g = self.g + 50 % 255
        b = self.b + 50 % 255
        return Color(r,g,b)
    def __str__(self) -> str:
        return f"{self.r} {self.b} {self.g}"