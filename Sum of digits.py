# Program to find sum of digits of a number
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def main():
    num = int(input("Enter a number: "))
    print(f"Sum of digits: {sum_of_digits(num)}")

if __name__ == "__main__":
    main()
