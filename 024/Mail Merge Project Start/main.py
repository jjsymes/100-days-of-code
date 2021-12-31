#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"
with open("./Input/Letters/starting_letter.txt") as f:
    starting_letter = f.read()

with open("./Input/Names/invited_names.txt") as f:
    invited_names = f.read().splitlines()

for name in invited_names:
    output_letter = starting_letter.replace(PLACEHOLDER, name)
    with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as f:
        f.write(output_letter)
