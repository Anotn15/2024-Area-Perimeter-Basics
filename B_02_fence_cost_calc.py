# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):

    error = "Please enter a number that is more then zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))
            if response > 0:
                return response
            else:
                print(error)


        except ValueError:
            print(error)

#Main Routine starts here....

keep_going = ""
while keep_going == "":

    #Get width and height

    width = num_check("width: ")
    height = num_check("Height: ")
    cost_per_meter= num_check("Cost per meter: ")


    # Calculate perimeter

    perimeter = 2 * (width + height)
    cost = perimeter * cost_per_meter
    # Display output
    print ()
    print(f"Perimeter : {perimeter} units")
    print(f"Cost : ${cost:.2f}")



    # Ask user if they want to keep going
    #
    keep_going = input ("press enter to keep going or any key to quit. ")
    print()

print("Thank you for using the area / perimeter caculator")
