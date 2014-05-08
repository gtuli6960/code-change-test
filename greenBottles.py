import time
bottles = int(input("How many green bottles are hanging on the wall?: "))
for i in range(bottles,0,-1):
    if i == 1:
        for j in range(2):
            print("1 green bottle hanging on the wall,")
        print("And if 1 green bottle should accidently fall,")
        print("There'll be 0 green bottles hanging on the wall.\n")
    else:
        for j in range(2):
            print("{0} green bottles hangning on the wall,".format(i))
        print("And if 1 green bottle should accidently fall,")
        if i == 2:
            print("There'll be 1 green bottle hanging on the wall.\n".format(i-1))
        else:
            print("There'll be {0} green bottles hanging on the wall.\n".format(i-1))
    time.sleep(1)
