#24-August-Error Handling

#155___________________________
while True:
    try:
        age=int(input("Whats your age = "))
        print(age)
    except:  # only executed if there is a problem in the try block
        print("\n Please enter a number :")
    else: # only executed if there is no error. Basically then both the try & else block will be executed if there is no error..?
        print('\n THank you')
        break

# If we want to handle different errors such as different input type, and a valid integer with specific range, we can update the except block


# Can add different exceptions

while True:
    try:
        age=int(input("Whats your age = "))
        print(age)
    except ValueError: # for data types other than integer
        print("\n Please enter a number :")
    except ZeroDivisionError:
        print('\nEnter a value greater than 0 :')
    else: 
        print('\n THank you')
        break

# except block will run only once and catches the first exception encountered. If duplicates exceptions present also, also runs only once 

#156________________________________________________________________________
def sum(num1, num2):
    try:
        return num1+num2
    except TypeError as err:
        #print('Please enter the number'+err) # can be used to display the error along with the message to the user.
        print(f'Pease enter a number:  [{err}]')

#err- is actaully an error object
print(sum(1,'2'))
#- - - - - - -- - - ---------------- 
while True:
    try:
        age=int(input("Whats a you age = "))
        print(age/1)
    except(TypeError,ZeroDivisionError) as err: # can also combime different types of errors and use one display message
        print(err)
    else: 
        print('\n THank you')
        break

#157_____________________________________________________________

while True:
    try:
        age=int(input("Whats a you age = "))
        print(age/1)
    except(TypeError,ZeroDivisionError) as err: 
        print(err)
    else: 
        print('\n THank you')
        break
    finally:
        print('ok, I am finally Done') #runs eveytime regardless of the presence of an error. 

#whatever other conditions will not get executed after the try,else,finally bock if a break statement is present in any one of them. 

#We can throw in our own exceptions by using the 'raise' keyword

while True:
    try:
        age=int(input("Whats a you age = "))
        print(age/1)
        raise ValueError('hey cut it out')
        #raise Exception('hey cut it off...!') - Can also raise an exception
    else: 
        print('\n THank you')
        break
    finally:
        print('ok, I am finally Done')