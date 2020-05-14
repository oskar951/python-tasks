import random


def function():
    rand = [] 
    for i in range(5): 
        rand.append(random.randint(100, 201)) 
  
    return rand


print(function())