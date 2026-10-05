try:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    count = len(lines)

    first_two = lines[:2]

    # Write the result to output.txt
    with open("output.txt", "w") as file:
        file.write("Total lines: " + str(count) + "\n")
        for line in first_two:
            file.write(line)

    print("Data written successfully to output.txt")

except FileNotFoundError:
    print("Error: File not found")