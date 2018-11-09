from utils.generatePolygon import generatePolygon

class ShapeGenerator:
    def __init__(self, center_cords):
        self.center_cords = center_cords

    def generate(self):
        raise NotImplementedError()


class LowPolyGenerator(ShapeGenerator):
    def __init__(self, center_cords):
        super().__init__(center_cords)

    def generate(self):
        return generatePolygon(ctrX=self.center_cords[0], ctrY=self.center_cords[1])
