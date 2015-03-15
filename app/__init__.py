import fibo


print "Hello I am in the global namespace of  __init__.py"

def disp():
    print "hello printing __name__ from  __init__ ", __name__


if __name__ =='__main__':
    disp()

