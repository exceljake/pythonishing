### Celsius to Fahrenheit Calculator and vice versa
## I am Jake and this is my first mini project in Python! 
## The TempCalcu converts user inputted temperature to 
## Fahrenheit if user input is Celsius, and vice versa. 
## Made: 2/19
## More Conditional Structures

## Enjoy! :D 
## Start of code: 

temp = input("Please enter a temperature, format: 36C or 100F. Go:") 
print(temp[-1])
if temp[-1] == "C":
    removelastchar = int(temp[:-1])
    print(removelastchar * 10)

# Next thing to do is to divide removelastchar by 1.8 to produce Fahr