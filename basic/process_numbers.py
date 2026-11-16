string_to_process = "  18,27,35,20  "

string_to_process = "  18,27,35,20  "

string_to_process = string_to_process.strip()

values = string_to_process.split(",")

total = int(values[0]) + int(values[1]) + int(values[2]) + int(values[3])

average = total / 4

print("Total: " + str(total))

print("Average: " + str(average))

# Expected Output:
# "Total: 100"
# "Average: 25.0"
# Expected Output:
# "Total: 100"
# "Average: 25.0"