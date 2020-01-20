# Sumuje liczby nturalne parzyste z przedziału <from_n,to_n>
def sum_even(from_m,to_n):
    sum = 0
    if type(from_m) != int or type(to_n) != int:
        raise TypeError("Liczby powinny być całkowite!")
    for i in range(from_m,to_n + 1):
        if i%2 == 0 and i>=0: # liczba parzysta
            sum += i
    return sum

def main():
    m = 1
    n = 6
    print(f"Suma liczb naturalnych parzystych z przedziału <{m},{n}> wynosi {sum_even(1,6)}")

if __name__ == "__main__":
    main()