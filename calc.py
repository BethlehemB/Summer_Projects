def add(a,b):
    answer = a+b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")


def subtract(a,b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")
    

def multiply(a,b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")


def divide(a,b):
    answer = a/b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

while True:
    print ("A: Addition")
    print( "B: Subtraction")
    print ("C: Multiplication")
    print ("D: Division")
    print ("E: Exit")

    choice = input("What would you like to calculate today? ")

    if choice == "A" or choice == "a":
        print ("You chose addition!")
        a = int(input("Please enter your first number: "))
        b = int(input("Please enter your second number: "))
        add(a,b)

    if choice == "B" or choice == "b":
        print ("You chose subtraction!")
        a = int(input("Please enter your first number: "))
        b = int(input("Please enter your second number: "))
        subtract(a,b)

    elif choice == "C" or choice == "c":
        print ("You chose multiplication!")
        a = int(input("Please enter your first number: "))
        b = int(input("Please enter your second number: "))
        multiply(a,b)

    elif choice == "D" or choice == "d":
        print ("You chose division!")
        a = int(input("Please enter your first number: "))
        b = int(input("Please enter your second number: "))
        divide(a,b)

    elif choice == "E" or choice == "e":
        print ("Hope we helped have a nice day!")
        quit()


