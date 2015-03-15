#import __init__ as init

print "I am in the global namespace of fibo"
def  fib(n):
    a, b= 0, 1
    while b< n:
        print b
   	a, b= b, a+b
'''
def disp():
    print __name__
'''

if __name__ == '__main__':
    fib(20)
    disp() 
