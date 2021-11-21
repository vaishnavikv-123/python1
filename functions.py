def greet():
    print('Hello')
greet()


def f(x,y,z):
    v=x*y*z
    return v
print('Enter the three sides of a cuboid:')
a=int(input())
b=int(input())
c=int(input())
print('Volume of cuboid:'+str(f(a,b,c)))


def f(a,b,c,d):
    s=a+b+c+d
    return s
print('Enter four numbers:')
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print('Sum of the numbers:'+str(f(a,b,c,d)))