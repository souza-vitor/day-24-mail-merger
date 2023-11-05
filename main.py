#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as names:
    guest_list = names.readlines()
    for name in guest_list:
        guest_list[guest_list.index(name)] = name.strip("\n")

for name in guest_list:
    with open("./Input/Letters/starting_letter.txt") as letter:
        body_letter = letter.readlines()
        body_letter[0] = f"Dear {name},\n"
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as final_letter:
            for line in body_letter:
                final_letter.write(line)
