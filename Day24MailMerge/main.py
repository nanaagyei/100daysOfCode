PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as names_file:
    name_list = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as starting_file:
    letter = starting_file.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as output_letter:
            output_letter.write(new_letter)


# with open("./Input/Names/invited_names.txt", "r") as names_file:
#     name_list = names_file.readlines()
#
# new_name_list = []
#
# for name in name_list:
#     new_name_list.append(name.strip("\n"))
#
# with open("./Input/Letters/starting_letter.txt", "r") as starting_file:
#     letter = starting_file.readlines()
#
# new_letter = []
# for line in letter:
#     new_line = line.strip("\n")
#     if new_line != "":
#         new_letter.append(new_line)
#
# for name in new_name_list:
#     with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as output_letter:
#         for line in new_letter:
#             if "[name]" in line:
#                 output_letter.write(line.replace("[name]", f"{name}") + "\n")
#                 output_letter.write("\n")
#             else:
#                 output_letter.write(line + "\n")
#                 output_letter.write("\n")
