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