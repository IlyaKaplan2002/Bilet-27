def read_file(filename = "data/third_task.data.txt"): #let's use function code style for future unittest
    if not filename:
        filename = "data/third_task.data.txt"  #adding default value, just in case
        print("Using default 'data/third_task.data.txt'")
    with open(filename, "r") as file:
        data = file.readlines() #Open and read file
    counter_u = 0 #create counters for letters
    counter_v = 0
    counter_w = 0

    for string in data:
        for char in string.lower(): #parsing file data per letter
            if char == "u":  #check conditions and count u, v and w
                counter_u += 1
            elif char == "v":
                counter_v += 1
            elif char == "w":
                counter_w += 1

    return f"{counter_u}u {counter_v}v {counter_w}w" #get answer

if __name__ == "__main__":
    filename = input("Enter filename: ") #get file name
    print(read_file(filename)) # use function print answer
