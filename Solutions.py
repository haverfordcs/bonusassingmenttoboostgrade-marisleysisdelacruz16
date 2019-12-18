def compute_binary(number):
    if isinstance(number, float) or isinstance(number,int): #making sure the number is an integer or float (decimal)
        if number > 1:
            compute_binary(number // 2)
        result = number % 2
        print(result, end='')
    return '' #in order to remove the none values from print statements

def gcd(number1, number2):
    if (isinstance(number1, float) or isinstance(number1, int)) and (isinstance(number2,float) or isinstance(number2,int)):
        if (number1 == 0):
            return number2
        if (number2 == 0):
            return number1
        if (number1 == number2): # base case
            return number1
        if (number1 > number2):
            return gcd(number1 - number2, number2)
        else:
            return gcd(number1, number2 - number1)
    else:
        return False

def sum_digits(num):
    if (isinstance(num, float) or isinstance(num, int)):
        if num == 0:
            return 0
        else:
            return (num % 10 + sum_digits(int(num / 10)))
    else:
        return False

def big_diff(L):
    max = L[0]
    for i in L:
        if i > max:
            max = i
    min = L[0]
    for i in L:
        if i < min:
            min = i
    return max - min

def centered_average(L):
    sum = 0
    min_value = L[0]
    max_value = L[0]
    for i in L:
        min_value = min(min_value, i)
        max_value = max(max_value, i)
        sum += i
    return (sum - max_value - min_value) // (len(L) - 2)

if __name__ == "__main__":
    import doctest #running doctest through here instead of on the test_suit.txt file
    doctest.testfile("test_cases.txt")
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