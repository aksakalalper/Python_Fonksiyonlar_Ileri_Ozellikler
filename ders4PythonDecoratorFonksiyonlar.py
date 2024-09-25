import time
import math

def myDecorator(func):
    def wrapper():
        print("fonksiyondan onceki islemler")
        func()
        print("fonksiyondan sonraki islemler")
    return wrapper

@myDecorator
def sayHello():
    print("hello")


def sayGreeting():
    print("greetings")


sayHello()




def zamanHesapla(func):
    def inner(*args,**kwargs):
        start=time()
        func(*args,**kwargs)
        finish=time()
        print(f"fonksiyon "+func.__name__+str(finish-start)+" saniye surdu")
    return inner

@zamanHesapla
def usAlma(a,b):
    
    print(pow(a,b))
    
@zamanHesapla
def faktoriyel(num):

    print(math.factorial(num))
 
usAlma(2,3)
faktoriyel(5)



def decorator(function):
    def wrapper(a,b):
        print(f'hazirliklar yapiliyor...{a} ve {b} toplanacaktir')
        start=time.time()
        function(a*2,b)
        finish=time.time()
        print(f"fonksiyon "+function.__name__+str(finish-start)+" saniye surdu")
        print('fonksiyon calisti.')
    return wrapper

@decorator
def operation(a,b):
    print('fonksiyon calisiyor.')
    print(a/b)
    
operation(2,3)


