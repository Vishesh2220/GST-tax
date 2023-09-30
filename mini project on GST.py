cp=eval(input("enter the cost price of object: "))
c=eval(input('enter the tax % imposed by central,ie.CGST: '))
s=eval(input('enter the tax % imposed by state,ie.SGST: '))
total=cp*c/100+cp*s/100+cp
print("total cost of product is:",total)
