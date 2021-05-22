# This program is a geometry calculator. It uses a while loop to return to the main menu. It uses if/else statements to provide appropriate output for each option. Functions are declared above the if/else portion of code, which are called after input of type float is received from the user. It checks the to see if the input is a positive value before performing the calculation.
import math
print ("Program Author: Renfred Mok")
print ("ID#: 3451103 ")
print ("Program 4 - Functions")
print ()
print("CALCULATIONS MENU")
print("1) AREA (SQUARE)")
print("2) AREA (RECTANGLE)")
print("3) AREA (CIRCLE)")
print("4) PERIMETER (SQUARE)")
print("5) PERIMETER (RECTANGLE)")
print("6) CIRCUMFERENCE (CIRCLE)")
print("7) EXIT")

def areaSquare (a):
    if a < 0:
        print("Please make sure this measurement is positive.")
        areaSquare(float(input("Try again. ")))
    else:
        print("The area of your square is ", str(a**2))

def areaRectangle(a,b):
    if a < 0 or b < 0:
        print("Please make sure both measurements are positive.")
        areaRectangle(float(input("Let's try again, width? ")),float(input("Length? ")))
    else:
        print("The area of your rectangle is ", str(a*b))

def areaCircle (a):
    if a < 0:
        print("Please make sure this measurement is positive.")
        areaCircle(float(input("Try again. ")))
    else:
        print("The area of your circle is ", str(math.pi * (a**2)))

def perimSquare (a):
    if a < 0:
        print("Please make sure this measurement is positive.")
        perimSquare(float(input("Try again. ")))
    else:    
        print("The perimeter of your square is ", str(a*4))

def perimRectangle(a,b):
    if a < 0 or b < 0:
        print("Please make sure both measurements are positive.")
        perimRectangle(float(input("Let's try again, width? ")),float(input("Length? ")))
    else:    
        print("The perimeter of your rectangle is ", str(2*(a + b)))

def perimCircle (a):
    if a < 0:
        print("Please make sure this measurement is positive.")
        perimCircle(float(input("Try again. ")))
    else:
        print("The circumference of your circle is ", str(math.pi * a * 2)) 

loop = 1
choice = 0
while loop == 1:
    choice = input("Please enter an option number from the menu above (1-7). ")
    if choice == "1":
        print("You have selected to calculate the area of a square.")
        areaSquare(float(input("Please enter the measurement of any side. "))) 
    elif choice == "2":
        print("You have selected to calculate the area of a rectangle.")
        areaRectangle(float(input("Please enter the width. ")),float(input("Now the length. ")))
    elif choice == "3":
        print("You have selected to calculate the area of a circle.")
        areaCircle(float(input("Please enter the radius. ")))
    elif choice == "4":
        print("You have selected to calculate the area of a square.")
        perimSquare(float(input("Please enter the measurement of any side. ")))
    elif choice == "5":
        print("You have selected to calculate the area of a rectangle.")
        perimRectangle(float(input("Please enter the width. ")),float(input("Now the length. ")))
    elif choice == "6":
        print("You have selected to calculate the circumference of a circle.")
        perimCircle(float(input("Please enter the radius. ")))
    elif choice == "7":
        loop = 0
    else:
        print("You have entered an invalid value, please try again.")

print("Thanks for using Ren's simple geometry calculator!")