# Ask user for width and loop until they
# enter a number that is more than zero

error = "Please enter a number that is more then zero\n"
while True:

    try:

        width= float(input("width:"))
        if width > 0:
            break
        else:
            print(error)


    except ValueError:
        print:(error)