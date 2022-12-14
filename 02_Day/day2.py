# Today we look at operators 

print('Addition : ', 2 + 7)  
print('Substraction: ', 9 - 2)
print('Multiplication: ', 4 * 3)
print('Division: ', 6 / 2)                 # return floating point number
print('Reminder: ', 50 % 3)
print('Exponential: ', 4 ** 3)             # return square value 
print('Floor Division: ', 8 // 3)          # return whole number i.e. 2

# complex number
print('Complex number: ', 4 + 2j)
print('Multiplying complex numbers: ', (4+2j) * (4-2j))

# declaring the variable and do some opeartions

a = 10  # a is a variable and stored 10 as integer(int) data type
b = 5   # b is a variable and stored 5 as integer(int) data type

# Do some Arithematic operations

total = (a + b)
difference = abs(a - b)  # we want differnce not negative value
product = a * b
division = a /1/ b
floor_division = a // b
exponential = a ** b
reminder  = a % b 

# now print function
print('a + b = ', total)
print('a - b = ', difference) 
print('a * b = ', product)
print('a / b = ', division)
print('a // b = ', floor_division)   # return whole number only 
print('a % b = ', reminder)

# Now I will make operation through variable.
numOne = 5
numTwo = 30

# Arithmetic operators
total = numOne + numTwo
diff = numTwo - numOne
product = numOne * numTwo
division = numTwo / numOne
remainder = numTwo % numOne

# printing the value
print('Total: ',total)
print('difference: ', diff)
print('product: ', product)
print('Division: ', division)
print('remainder: ', remainder)

# Find some area of particluar shape
# square
length = 4
area_of_square  = 4 * length
print('area of square: ', area_of_square)

# reactangle 
length = 10
width = 20
area_of_reactangle = length * width
print('Area of reactangle: ', area_of_reactangle)

# Circle
radius = 6
area_of_circle = 3.14 * radius ** 2
print('Area of circle: ', area_of_circle)

# conditions return true or false
print(4 > 2)
print(5 >= 5)
print(5 >= 50)
print(5 < 3)
print(5 > 3)
print(5 == 3)
print(5 != 3)

# Some string maniplulation methods with comparision
print(len('apple'))                           # 5
print(len('samsung'))                         # 7
print(len('apple') == len('samsung'))         # False
print(len('Python') <= len('javascript'))     # True

# Boolean comparision
print('True == True: ', True == True)
print("True == False: ", True == False)
print('False == False: ', False == False)
print('True or False: ', True or False)
print('True and False: ', True and False)
print('False and False: ', False and False)
print('True and True: ', True and True)

# some other way comparision
print('1 is 1: ', 1 is 1)
print('1 is 2: ', 1 is 2)
print('1 is not 2: ', 1 is not 2)
print('B in Beast: ', "B" in "Beast")
print("A in Sound: ", "A" in "Sound")
print('4 is 2 **2: ', 4 is 2**2)

print(3 > 2 and 4 > 2)           # True
print(4 > 6 and 4 < 6)           # False
print(4 > 6 or 4 < 6)            # True
print(3 > 2 or 4 > 2)            # True
print(not 3 > 4)                 # True
print(not True)                  # False
print(not not True)              # True
print(not False)                 # True
print(not not False)             # False    
print(not not not False)         # True