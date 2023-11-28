#!/usr/bin/python3

for i in range(10):    
    for j in range(8):
        if (j + 1 + i) < 10 :
            print("{}{}".format(i, (j + 1 + i)), end="")
            if (i < 8):
                print(", ", end="")
print("")
