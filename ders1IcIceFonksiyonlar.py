 #encapsulation
def outer(num1):
    print(num1,'outer calisti')
    def innerIncrement(num1):
        print(num1,'inner calisti')
        return num1+1
    num2=innerIncrement(num1)
    print(num1,num2)        
    
outer(10)

def factorial(number):
    def innerFactorial(number):
        if (number<=1):
            return 1
        return number*innerFactorial(number-1)
    return innerFactorial(number)

print(factorial(5))
