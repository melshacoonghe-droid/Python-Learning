for i in range(4, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

    for i in range(1, 11):
      if i == 6:
        break
    print(i)

    for i in range(1, 11):
      if i == 6:
        continue
    print(i)

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

    for i in range(1, 21):
      if i % 7 == 0:
        print("Found:", i)
        break
    print(i)