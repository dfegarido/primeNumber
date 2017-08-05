import time
start_time = time.time()

def prime(n):
    zero = 0
    for i in range(1, n+1):
        ans = n % i
        if ans == 0:
            zero += 1
    return zero   

def list_of_prime(n):
    x = []
    for i in range(1, n+1):
        if prime(i) == 2:
            x.append(i)
    return x

print(list_of_prime(100))

print('')
print('')
print('')
print('It took = ',time.time() - start_time)
