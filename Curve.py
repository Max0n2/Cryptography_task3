from Point import Point

class Curve:
    def __init__(self, a, b) -> None:
        self.ValidateECurve(a, b)
        self.a = a
        self.b = b

    def ValidateECurve(self, a, b):
        if (a == 0 and b == 0):
            raise ValueError('Такої кривої не існує.')

    def AddECPoints(self, P: Point, Q: Point) -> Point:
        m = (P.y - Q.y) / (P.x - Q.x)

        x = m**2 - P.x - Q.x
        y = P.y + m * (x - P.x)

        return Point(int(x), int(y))

    def EquationToString(self):
        return f'Р-ня еліптичної кривої: y² = x³ + {self.a}x + {self.b}'

    def PrintEquation(self) -> None:
        print(self.EquationToString())

    def BasePointGGet(self) -> Point:
        x = 14234567
        y = 5489564

        return Point(int(x), int(y))    