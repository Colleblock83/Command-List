
#Colors and centers the text in the console
text = "\033[34mCheat-Sheet: Important commands to know for beginners!\033[0m"
ubrsch = text.center(130)
print(ubrsch)

print("")

print("")
print("Please choose an option below: ")
for cmds in ["\033[31m(1)\033[0m \033[33mprint()\033[0m", "\033[31m(2)\033[0m \033[33mlen()\033[0m",
             "\033[31m(3)\033[0m \033[33mclasses ~:\033[0m", "\033[31m(4)\033[0m \033[33minput()\033[0m",
             "\033[31m(5)\033[0m \033[33mrange()\033[0m", "\033[31m(6)\033[0m \033[31mEnd the Program\033[0m"]:
    print(cmds)
numbr = int(input("Option: "))

while True: #Endlessloop which can only be stopped by "break" by the "True" statement

    if numbr == 1:
        print("\033[33mprint(): \033[0m")
        for cmd_liste in["• Outputs text or variables to the console.", "• Can format output using f-strings or format method.", "• Supports multiple arguments separated by commas"]:
            print(cmd_liste)
    elif numbr == 2:
        print("\033[33mlen()\033[0m")
        for cmd_liste in["• Returns the length (number of elements) of a string, list, or other iterable.", "• Useful for checking the size of collections.", "• Can be used with various data types like tuples and dictionaries."]:
            print(cmd_liste)
    elif numbr == 3:
        print("\033[33mclasses ~:\033[0m")
        for cmd_liste in["• Takes user input as a string from the console.", "• Supports encapsulation, inheritance, and polymorphism.", "• Can have attributes (variables) and methods (functions)."]:
            print(cmd_liste)
    elif numbr == 4:
        print("\033[33minput()\033[0m")
        for cmd_liste in["• Generates a sequence of numbers, commonly used in loops.", "• Can prompt the user with a message.", "• Always returns input as a string, so type conversion is often necessary."]:
            print(cmd_liste)
    elif numbr == 5:
        print("\033[33mrange()\033[0m")
        for cmd_liste in["• Returns the data type of a variable or value.", "• Can take one, two, or three arguments (start, stop, step).", "• Returns an immutable sequence type.", "• Useful for iterating over a fixed number of times in loops."]:
            print(cmd_liste)
    elif numbr == 6:
        print("Press enter to close this window...")
        break
    elif not (1<=numbr <=5):
        print("\033[33mPlease enter an number between 1 and 5.\033[0m")
    numbr = int(input("Option: "))










