filename = input("Enter filename: ") #get filename
if not filename:
    filename = "data/third_task.data.txt"  #adding default value, just in case
with open(filename, "r") as file:
    data = file.readlines() #Open and read file
counter_u = 0 #create counters for letters
counter_v = 0
counter_w = 0

for string in data:
    for char in string: #parsing file data per letter
        if char == "u":  #check conditions and count u, v and w
            counter_u += 1
        elif char == "v":
            counter_v += 1
        elif char == "w":
            counter_w += 1

print(f"{counter_u}u {counter_v}v {counter_w}w")  #finally print answer
