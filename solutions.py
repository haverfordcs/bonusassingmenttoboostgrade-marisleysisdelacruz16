def compute_binary(number):
    # comment this pass and write your code here 
    pass 

def gcd(number1, number2):
    # comment this pass and write your code here 
    pass

def sum_digits(num):
    # comment this pass and write your code here 
    pass

def big_diff(L):
    # comment this pass and write your code here 
    pass

def centered_average(L):
    # comment this pass and write your code here 
    pass


if __name__ == "__main__":
    a = 0
    b = -1
    c = 25
    d = 255
    e = 256
    print(compute_binary(a))
    print(compute_binary(b))
    print(compute_binary(c))
    print(compute_binary(d))
    print(compute_binary(e))

    num1 = 7
    num2 = 21
    print(gcd(num1, num2))

    num1 = 60
    num2 = 16
    print(gcd(num1, num2))

    num1 = 7
    num2 = 17

    print(gcd(num1, num2))

    print(sum_digits(126))  # → 9
    print(sum_digits(49))  # → 13
    print(sum_digits(12))  # → 3

    print(big_diff([10, 3, 5, 6]))  # → 7
    print(big_diff([7, 2, 10, 9]))  # → 8
    print(big_diff([2, 10, 7, 2]))  # → 8

    print(centered_average([1, 2, 3, 4, 100]))  # → 3
    print(centered_average([1, 1, 5, 5, 10, 8, 7]))  # → 5
    print(centered_average([-10, -4, -2, -4, -2, 0]))  # → -3

