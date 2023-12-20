from circle import Circle
from color import Color
from rectangle import Rectangle
from square import Square

if __name__ == "__main__":
    print(Rectangle(15, 10, Color("синий")))
    print(Circle(15, Color("зеленый")))
    print(Square(15, Color("красный")))
