def cube(number):
    return number*number*number
def devisions(number):
    if (number%3==0):
        return cube(number)
    else:
        print("number is not divisible by 3")

print(devisions(9))
print(devisions(10))