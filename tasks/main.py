# Task 1
# Check a prime number
def check_prime(number):
    divisors = []
    for i in range(1, number + 1):
        if(number % i == 0):
            divisors.append(i)

    if len(divisors) == 2:
        return True
    return False


input_number = int(input("Enter a number\n"))
print(check_prime(input_number))


# Task 2
# Merge two sorted arrays
def merge_sorted_lists(list1, list2):
    sorted(list1 + list2)
    return sorted(list1 + list2)


print(merge_sorted_lists([5, 10, 7, 82, 109, 2], [70, 0, 16, 9, 23, 27]))
