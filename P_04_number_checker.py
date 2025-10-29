# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):


    error = "Please enter a number that is more then zero\n"
    while True:

        try:

            response= float(input(question))
            if response > 0:
                return response
            else:
                print(error)


        except ValueError:
            print:(error)

 #Main Routine Goes Here
 Width= num_check("width: ")
 print(width)
