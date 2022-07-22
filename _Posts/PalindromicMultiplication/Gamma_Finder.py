def get_factors(num):
    f = []
    for i in range(2, num + 1):
        if num % i == 0:
            f.append(i)
    return f

def base(value, base):
    digits = []
    exp = 1
    while value > 0:
        newDig = value % base
        digits.append(newDig)
        value = value // base
        exp += 1
    digits.reverse()
    return digits

def all_ones(nums):
    for num in nums:
        if num != 1:
            return False
    return True

def find_gamma(val, nums):
    for factor in nums:
        base_rep = base(val, factor)
        print(f'{val} in base {factor}:\t', base_rep)
        if all_ones(base_rep):
            println()
            return factor
    return 0

def println():
    print('-' * 60)

print('\n\n')
m = int(input("Enter your m value (must be an integer greater than 2 for this to work):\t\t\n")) - 1
println()
factors = get_factors(m)
print(f'Factors of {m}:\n\t', factors)
println()
print('Checking each factor:\n')
m += 1
print(f'Base representation of {m} with the most ones:\t', find_gamma(m, factors))

# cool_numbers = {}
# m = 3

# while m < 100002:
#     m -= 1
#     println()
#     factors = get_factors(m)
#     m += 1
#     gamma = find_gamma(m, factors)
#     if len(base(m, gamma)) > 4:
#         cool_numbers[m] = gamma
#     m += 1

# print(cool_numbers)
