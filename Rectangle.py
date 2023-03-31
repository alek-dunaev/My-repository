class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

# Метод расчитывающий площадь
    def getArea(self):
        return self.width * self.height

rectangle = Rectangle(20, 30)
print(rectangle.getArea())
