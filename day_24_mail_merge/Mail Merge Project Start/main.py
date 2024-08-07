#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

TEMPLATE = "[name]"

with open("Input/Names/invited_names.txt") as names:
    names = names.readlines()

with open("Input/Letters/starting_letter.txt") as file:
    mail_text = file.read()
    for name in names:
        stripped_names = name.strip()
        new_text = mail_text.replace(TEMPLATE, stripped_names)
        with open(f"Output/ReadyToSend/letter_for_{stripped_names}.txt", mode='w') as result:
            result.write(new_text)
