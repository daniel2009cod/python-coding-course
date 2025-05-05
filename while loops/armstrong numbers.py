number = int(input("Enter a number: "))

total_digits = len(str(number))

temp = number

sum = 0

while temp > 0:

 digit = temp % 10

 sum = sum + digit ** total_digits

 temp = temp // 10

if number == sum:

 print("It is an Armstrong number")

else:

 print("It is not an Armstrong number")