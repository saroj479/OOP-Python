mylist = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
totalsum = 0


while True:
    usertype = int(input("Type Number"))
    if usertype == 0:
        print(totalsum)
        payment=int(input("Payment"))
        if payment < totalsum:
            print("Not enough money")
            break
        change=payment - totalsum
        print("Change ",change)
        break
    else:
        for i in range(len(mylist)):
            if usertype == i:
                i-=1
                print(mylist[i])
                totalsum += mylist[i]
                print("hi")

