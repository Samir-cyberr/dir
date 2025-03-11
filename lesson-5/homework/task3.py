def find_factors(n: int):
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")

def main():
    num = int(input("Enter a positive integer: "))
    find_factors(num)

if __name__ == "__main__":
    main()
