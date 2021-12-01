from square import Square

side_square = int(input('Square measure: '))
color_square = input('Color: ')
square1 = Square(side_square, color_square)
print(square1)
print(square1.area())