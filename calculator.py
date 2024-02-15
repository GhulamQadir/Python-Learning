heading="CALCULATOR"
centHeading = heading.center(30)
print(centHeading)
num1 =float(input("Enter a first number: "))
operator = input("Enter the opertor like:\n(+, -, x, /, %): ")
num2 =float(input("Enter a second number: "))

if operator=="+": 
 print("The result is: ",num1+num2)
elif operator=="-":
 print("The result is: ",num1-num2)
elif operator=="x":
 print("The result is: ",num1*num2)
elif operator=="/":
 print("The result is: ",num1/num2)
elif operator=="%":
 print("The result is: ",num1%num2)
else: 
  print("Invalid input!")    