'''
Below are three set's of numbers. Create three variables that are equal to each set: one number minus the other
'''
set1, set2, set3, = [25, 10], [50, 27], [61, 38]
var1 = 25-10
var2 = 50-27
var3 = 61-38
print(var1)
print(var2)
print(var3)
'''
Below are three set's of numbers. Create three variables and make them equal to the result of when the first number entered from one set is raised to the power of the second number.
'''
set4, set5, set6, = [2, 3], [10, 7], [5, 4]
var4 = 2**3
var5 = 10**7
var6 = 5**4
print (var4)
print (var5)
print (var6)

'''
Below are three set's of numbers.  Create three variables and make them equal to the number of times the second number can be divided into the first number. For example if the first number entered was 23 and the second number entered was 4 the program should report 5 times
'''
set7, set8, set9, = [23, 4], [19, 3], [81, 13]
var7 = 23//4
var8= 19//3
var9 = 81//13
print(var7)
print(var8)
print(var9)

'''
Below is an empty variable called my_name. Assign your name to the variable and then add the string "hello " to the
front of it. Assign the result to the variable greeting 
'''
my_name="Hector"
greeting="Hello my name is " + my_name
print (greeting)


'''
Below is a list of even and odd numbers. Can you write a block of code that loops through the list and tells you whether the number is even of odd?
'''
numbers = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in range (1,10):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

