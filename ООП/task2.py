class TriangleChecker:
    """Это класс, проверяющий на возможность построить треугольник из данных отрезков"""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        print(self.__dict__)
        if type(self.a) != int or type(self.b) != int or type(self.c) != int:
            return 'Вводи числа'
        elif self.a < 0 or self.b < 0 or self.c < 0:
            return 'С отрицаткльными числами нельзя'
        elif self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return 'Из этого треугольник не построить'
        else:
            return 'Можно построить треугольник'


triangle = TriangleChecker(3, 4, 5)
print(TriangleChecker.is_triangle(triangle))
triangle1 = TriangleChecker(1, 4, 5)
print(TriangleChecker.is_triangle(triangle1))
triangle2 = TriangleChecker((1, 3), 4, 5)
print(TriangleChecker.is_triangle(triangle2))
triangle3 = TriangleChecker(-23, 4, 5)
print(TriangleChecker.is_triangle(triangle3))
print(TriangleChecker.__doc__)
