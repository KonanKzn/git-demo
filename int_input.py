# KZN revision
while True: 
    try:
        cost = int(input("Enter the number:"))        
        if cost <= 0:
            print("Invalid value.", end = " ")
            continue
        else:
            break    
    except ValueError:
        print("Invalid value.", end = " ")
print("cost:", cost)

'''
# from internet
while True:
    try:
        numb = int(input("Enter the number:"))
    except ValueError:
        continue # продолжнает цикл; break  выводит с цикла
    if numb % 2 == 0:
        print("this number is EVEN")
    elif numb % 2 != 0:
        print("this number is ODD")
'''
