def mangle (string):
    string = string.upper()
    vowels= ["A","E","I", "O","U"]
    for letter in string:
        # print (letter, end="")
    # for letter in vowels:
    #     print(letter, end="")
        if letter in vowels:
            a = letter
            # return a
        else:
            b = letter
            # print (b, end="")
            return b

# mangle( "hello")
# mangle("HI")
# mangle("EEK")
# mangle("apple")
# mangle("banana")
# mangle("date")
def main():
    input_string = ["hi", "hello", "EEK!", "halo", "bla"]
    for letter in (input_string):
        # for letter in range(len(input_string)):
    #     mangle(input_string(letter))
    #     print (mangle(input_string[4]))
        print(input_string[4], "  ", end="")
        #     print(letter, end="")
        # print(mangle(input_string[letter]), end="")
            # print(mangle(input_string[letter]), end="")
            # print(letter)
main()

