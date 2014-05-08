# Import the time library so delays can be added to the program.
import time
# Ask the user how many bottles to start with.
bottles = int(input("How many green bottles are hanging on the wall?: "))
# Prin the verses from the specified number of bottles to 0 bottles.
for i in range(bottles,0,-1):
    # Lanuguage change to account for '1 green bottle'.
    if i == 1:
        for j in range(2):
            print("1 green bottle hanging on the wall,")
        print("And if 1 green bottle should accidently fall,")
        print("There'll be 0 green bottles hanging on the wall.\n")
    # Otherwise print the normal verses.
    else:
        for j in range(2):
            print("{0} green bottles hangning on the wall,".format(i))
        print("And if 1 green bottle should accidently fall,")
        # Lanuguage change to account for '1 green bottle'.
        if i == 2:
            print("There'll be 1 green bottle hanging on the wall.\n".format(i-1))
        else:
            print("There'll be {0} green bottles hanging on the wall.\n".format(i-1))
    # Time delay between printing verses.
    time.sleep(1)
