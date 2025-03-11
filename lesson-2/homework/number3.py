try:
    a=float(input("Write any distance in kilometer: "))
    b=a*1000
    c=a*100000
    print(b, "meter")
    print(c, "milecentimeter")
except ValueError:
    print("Invalid input! Please enter a valid float number.")