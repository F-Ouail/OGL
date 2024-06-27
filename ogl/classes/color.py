class Color:
    def __init__(self, r:int, g:int, b:int) -> None:
        self.r = r
        self.g = g
        self.b = b
    def value(self) -> tuple[int, int, int]:
        return (self.r ,self.g, self.b)
    def opposite(self):
        return Color(
            (255 - self.r) % 256,
            (255 - self.g) % 256,
            (255 - self.b) % 256
        )
    def shift(self):
        return Color(self.r * 0.85, self.g * 0.85, self.b * 0.85)
    def __str__(self) -> str:
        return f"{self.r} {self.b} {self.g}"