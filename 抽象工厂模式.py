class Shape:
    '''形状基类'''
    def draw(self):
        pass

class Circle(Shape):
    '''圆'''
    def draw(self):
        print('画圆！')

class Square(Shape):
    '''正方形'''
    def draw(self):
        print('画正方形！')

class Color:
    '''颜色基类'''
    def fill(self):
        pass

class Red(Color):
    '''红色'''
    def fill(self):
        print('用红色')

class Green(Color):
    '''绿色'''
    def fill(self):
        print('用绿色')

class AbstractFactory:
    '''工厂基类'''
    def Product(self, stuff):
        pass

class ShapeFactory(AbstractFactory):
    '''形状工厂'''
    def Product(self, stuff):
        if stuff == 'Circle':
            return Circle()
        elif stuff == 'Square':
            return Square()
        else:
            raise Exception('没有这种形状！')

class ColorFactory(AbstractFactory):
    '''颜色工厂'''
    def Product(self, stuff):
        if stuff == 'Red':
            return Red()
        elif stuff == 'Green':
            return Green()
        else:
            return Exception('没有这种颜色！')

class Factory:
    '''工厂的工厂'''
    @staticmethod
    def GetFactory(setting):
        if setting == 'Shape':
            return ShapeFactory()
        elif setting == 'Color':
            return ColorFactory()
        else:
            raise Exception('没有这种工厂!')

if __name__ == '__main__':
    shapeFac = Factory.GetFactory('Shape')
    circle = shapeFac.Product('Circle')
    square = shapeFac.Product('Square')
    circle.draw()
    square.draw()

    colorFac = Factory.GetFactory('Color')
    red = colorFac.Product('Red')
    green = colorFac.Product('Green')
    red.fill()
    green.fill()