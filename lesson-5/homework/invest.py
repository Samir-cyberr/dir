def invest(amount: float, rate: float, years: int):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

def main():
    # Get user input
    principal = float(input("Enter the initial investment amount: "))
    annual_rate = float(input("Enter the annual rate of return (as a decimal, e.g., 0.05 for 5%): "))
    num_years = int(input("Enter the number of years: "))
    
    # Call invest function
    invest(principal, annual_rate, num_years)

if __name__ == "__main__":
    main()
