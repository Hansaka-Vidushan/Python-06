from os import write

# Using Mode For File
file = open("data.txt" , "t+w")

# File Write
for i in range(0,100):
    file.write(str(i) + "\n")

# Using For Loop
for i ,line in enumerate(file):
    print(i,"." , line)


file.close()

# File is auto closing
with open("data.txt") as file:
    # Using While Loop
    while True:
        contents = file.readline()

        if not contents:
            break

        print(contents)










