#values for area calculations
area = 0
side = 0
length = 0
width = 0
radius = 0
height = 0
base = 0


#Presentation
print ("==================\nArea Calculator 📐\n==================")



input_shape = input(" Choose a shape (square, rectangle, circle, triangle): ")




if input_shape == "square":

    side_input = input("Enter the length of the side followed by the unit (e.g., cm, m): ")
    parts = side_input.split()     # ["6", "cm"]
    side = float(parts[0])         # 6.0
    unit = parts[1]                # "cm" Assuming both dimensions have the same unit

    square = side**2
    print(f"The area of your square is {square} {unit}²")



elif input_shape == "rectangle" :

    length = input("Enter the length followed by the unit (e.g., cm, m): ")
    width = input("Enter the width followed by the unit (e.g., cm, m): ")

    length_parts = length.split()    # ["6", "cm"]
    width_parts = width.split()      # ["6", "cm"]
    length = float(length_parts[0])  # 6.0
    width = float(width_parts[0])    # 6.0
    unit = length_parts[1]           # "cm" Assuming both dimensions have the same unit

    rectangle = length * width

    print(f"The area of your rectangle is {rectangle} {unit}²")



elif input_shape == "circle" :

    radius = input("Enter the radius followed by the unit (e.g., cm, m): ")

    parts = radius.split()          # ["6", "cm"]
    radius = float(parts[0])        # 6.0
    unit = parts[1]                 # "cm" Assuming both dimensions have the same unit

    circle = 3.14 * radius**2

    print(f"The area of your circle is {circle} {unit}²")




elif input_shape == "triangle" :

    height = input("Enter the height followed by the unit (e.g., cm, m): ")
    base = input("Enter the base followed by the unit (e.g., cm, m): ")

    height_parts = height.split()     # ["6", "cm"]
    base_parts = base.split()         # ["6", "cm"]
    height = float(height_parts[0])   # 6.0
    base = float(base_parts[0])       # 6.0
    unit = height_parts[1]            # "cm" Assuming both dimensions have the same unit

    triangle = (height * base) / 2

    print(f"The area of your triangle is {triangle} {unit}²")