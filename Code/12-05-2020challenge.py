
def function(num1, num2):

    num1 = int(input("Enter the start of range: ")) 
    num2 = int(input("Enter the end of range: ")) 
    list1 = []

    for num in range(num1, num2 + 1): 
      
    
        if num % 2 == 0: 
            list1.append(num)
    
    list1 = ",".join(str(i) for i in list1)
    
    return list1
            

print(function(1,2))