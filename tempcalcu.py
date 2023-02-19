### Celsius to Fahrenheit Calculator and vice versa
## I am Jake and this is my first mini project in Python! 
## The TempCalcu converts user inputted temperature to 
## Fahrenheit if user input is Celsius, and vice versa. 
## Made: 2/19
## More Conditional Structures

## Enjoy! :D 
## Start of code: 

# v1

temp = input("Please enter a temperature, format: 36C or 100F. Go: ") 
remove = int(temp[:-1])
if temp[-1] == "C":
    # remove_c = int(temp[:-1])
    print(temp + " in Fahrenheit is " + str((remove * 9/5) + 32) + "°F")
elif temp[-1] == "F":
    # remove_f = int(temp[:-1])
    print(temp + " in Celsius is " + str((remove - 32) * 5/9) + "°C")
else: print(temp + " is wrong syntax!")

# Done v1 Feb 19, 9:23am