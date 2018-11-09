from utils.generatePolygon import generatePolygon
import random


class ShapeGenerator:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def generate(self):
        raise NotImplementedError()


class LowPolyGenerator(ShapeGenerator):
    def __init__(self, dimensions):
        super().__init__(dimensions)

    def generate(self):
        x, y = 0, 0
        while x <= 200 and y <= 200:
            x = self.dimensions[0]//random.randint(1, 4)
            y = self.dimensions[1]//random.randint(1, 4)
        return ['polygon', generatePolygon(ctrX=x, ctrY=y)]


class HorizontalLineGenerator(ShapeGenerator):
    def __init__(self, dimensions):
        super().__init__(dimensions)

    def generate(self):
        line_list = []
        itr = random.randint(5,60)
        for y in range(itr):
            line_list.append(
                [
                    (random.randint(0, self.dimensions[0]), random.randint(y, itr)),
                    (random.randint(0, self.dimensions[0]), random.randint(
                        itr, self.dimensions[1]))
                ]
            )
        return ['line', line_list]
