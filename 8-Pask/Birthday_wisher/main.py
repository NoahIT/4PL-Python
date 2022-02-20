PLACEHOLDER = "[NAME]"

with open("./Names/names.txt") as name_file:
    names = name_file.readlines()

with open("./Letters/letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)

        with open(f"./Output/letter-{stripped_name.lower()}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
