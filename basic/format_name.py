string_to_process = "   sMitH, aLeX    "

string_to_process = string_to_process.strip()

name_parts = string_to_process.split(",")

last_name = name_parts[0].strip().title()
first_name = name_parts[1].strip().title()

formatted_name = first_name + " " + last_name

print(formatted_name)

# Expected output: "Alex Smith"