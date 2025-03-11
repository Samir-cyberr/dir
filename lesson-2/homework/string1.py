# User name 
a=input(" Write your name:")
# User year of birth
b=int(input("Write your year of birth:"))
if b<2025:
    c=2025-b
    print(f"Your name is {a}")
    print(f"Your age is {c}")
else:
    print("Write true year of your birth")