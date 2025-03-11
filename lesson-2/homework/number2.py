try:
    a=float(input("Write first number: "))
    b=float(input("Write second number: "))
    c=float(input("Write third number: "))
    print(max(a,b,c))
    print(min(a,b,c))
except ValueError:
     print("Invalid input! Please enter a valid float number.")