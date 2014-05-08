import time
for i in range(10,0,-1):
    for j in range(2):
        print("{0} green bottles hangning on the wall,".format(i))
    print("And if 1 green bottle should accidently fall,")
    print("There'll be {0} green bottles hanging on the wall.\n".format(i-1))
    time.sleep(1)
