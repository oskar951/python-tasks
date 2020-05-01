ISBN1 = int(input("What is you ISBN number?:"))


ISBN = list(str(ISBN1))

ISBN = [int(i) for i in ISBN]


number = (10 - ((ISBN[0] + ISBN[1] * 3 + ISBN[2] + ISBN[3] * 3 + ISBN[4] + ISBN[5] * 3 + ISBN[6] + ISBN[7] * 3 + ISBN[8] + ISBN[9] * 3 + ISBN[10] + ISBN[11] * 3)%10))



print(ISBN1, "-", number)

