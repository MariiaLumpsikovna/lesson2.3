numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    is_prime = True
    for j in range(2, numbers[i]):
        if numbers[i] % j == 0:
            is_prime = False
            break
    if is_prime == True:
        primes.append(numbers[i])
    if is_prime == False:
        not_primes.append(numbers[i])
print(primes)
print(not_primes)













# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
# a = 0
# while a < len(numbers):
#     a += 1
#     if numbers[a] == 1:
#         a += 1
#     if numbers[a] % b == 0:
#         not_primes.append(numbers[a])

#
# print(primes)
# print(not_primes)