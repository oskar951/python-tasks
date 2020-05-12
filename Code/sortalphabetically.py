def sortlist(a):
    a = input("enter your words separated by commas:")
    list1 = a
    list1 = list1.split(",")
    list1.sort()

    list1 = ",".join(list1)

    return list1

print(sortlist(" "))