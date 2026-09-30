for i in range(1, 11, 1):
    for x in range(11, i, -1):
      print(" ",end=" ")
    for y in range(1, i, 1):
      print("*",end=" ")
    for z in range(1,i,1):
      print("*", end=" ")
    print()
for i in range(11, 0 , -1):
    for x in range(11, i, -1):
        print(" ", end=" ")
    for y in range(1, i, 1):
        print("*", end= " ")
    for z in range(1, i, 1):
        print("*", end=" ")
    print()
