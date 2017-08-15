def roots(a,b,c,d):
    if d==0:
        print("roots are real and equal:" , -b/(2*a) ," ", -b/(2*a))
    elif d>0:
        print("roots are real:" , (-b+(d**(1/2.0)))/(2*a) ," ", (-b-(d**(1/2.0)))/(2*a))
    else:
        print("roots are complex:" , (-b+(d**(1/2.0)))/(2*a) ," ", (-b-(d**(1/2.0)))/(2*a))
a=float(input("enter coefficient of x^2:"))
b=float(input("enter coefficient of x^1:"))
c=float(input("enter the constant value:"))

d=(b*b)-(4*a*c)
roots(a,b,c,d)
