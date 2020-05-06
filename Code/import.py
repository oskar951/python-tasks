numbers = 0

for num in range(2,30 + 1):  
    for i in range(2,num):  
        if (num % i) == 0:  
            break  
    else:  
        print(num) 

        numbers += 1 

print("number of primes =" + " " + str(numbers))