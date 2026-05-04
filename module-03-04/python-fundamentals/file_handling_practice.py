with open("tasks.txt", "w") as f:
    f.writelines(["1) Do Laundry\n", "2) Make Dinner\n", "3) Read book\n"])

with open("tasks.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())

with open("tasks.txt", "a") as f:
    f.write("4) Sleep")    

with open("tasks.txt", "r") as f:
    lines = f.readlines()
    print(f"Total number of lines: {len(lines)}")    