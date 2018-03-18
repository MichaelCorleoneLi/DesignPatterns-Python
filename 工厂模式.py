class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print('画圆!')

class Square(Shape):
    def draw(self):
        print('画正方形')

class ShapeFactory():
    @staticmethod
    def getShape(shape):
        if shape == 'Circle':
            return Circle()
        elif shape == 'Square':
            return Square()
        else:
            raise Exception('没有此类型')

if __name__ == '__main__':
    circle = ShapeFactory.getShape('Circle')
    square = ShapeFactory.getShape('Square')
    circle.draw()
    square.draw()