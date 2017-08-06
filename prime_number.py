import time
start_time = time.time()

def prime(n):
    '''Check if the Number is Prime or not'''
    zero = 0
    for i in range(1, n+1):
        if zero >= 2:
            return False
        if n % i == 0:
            zero += 1
    return zero
        

def list_of_prime(low, high):
    '''Append all the prime number to a list'''
    x = []
    for i in range(low, high+1):
        if prime(i) == 2:
            x.append(i)
    return x

print(list_of_prime(9000,10000))



print('It took = ',time.time() - start_time)
