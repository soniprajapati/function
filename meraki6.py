def calculator(number_x,number_y,operation):
    if operation=="add":
        print(number_x+number_y)
    elif operation=="subtract":
        print(number_x-number_y)
    elif operation=="multiply":
        print(number_x*number_y)
    elif operation=="divide":
        print(number_x/number_y)
number_x=int(input(" enter number: "))
number_y=int(input(" enter number: "))
operation=input(" enter operation: ")
calculator(number_x,number_y,operation)
