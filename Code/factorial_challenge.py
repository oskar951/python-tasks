

def function(num):
 
 #num = int(input("enter a number:"))
 factorial = 1


 if num == 0:
    return "The factorial of 0 is 1"
 else:
    for i in range(1,num + 1):
        factorial = factorial*i
    return "The factorial of" + " " + str(num) + " " + "=" + " " + str(factorial) 

