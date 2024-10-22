def celciusToFahrenheit(temp):
    return  (9/5)*temp+32

def fahrenheitToCelcius(temp):
    return  (temp-32)*5/9

print("Enter desired conversion: \n \'a\' for Celsius to Fahrenheit \n \'b\' for Fahrenheit to Celsius")
choice = input()

if choice == 'a' or choice == 'A':
    temp = float(input("Enter temperature in Celcius: "))
    print("Fahrenheit: ", celciusToFahrenheit(temp))

elif choice == 'b' or choice == 'B':
    temp = float(input("Enter temperature in Fahrenheit: "))
    print("Celsius: ", fahrenheitToCelcius(temp))
else:
    print("Enter a valid choice!")