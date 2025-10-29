def num_check(question):
    error = "Please enter a number greater than zero.\n"
    while True:
        try:
            response = float(input(question))
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

# Main Routine starts here....

keep_going = ""
while keep_going == "":
    # Get width and height
    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate area and perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")
    print()

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit: ")
    print()

print("Thank you for using the area/perimeter calculator!")