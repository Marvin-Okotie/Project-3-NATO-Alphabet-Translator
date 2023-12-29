'''Project 3 - NATO Alphabet Translator
Author: Marvin Okotie
'''

# This function reads the NATO Alphabets file interprets it accordingly
def get_dictionary():
    dictionary = {}
    dictionary[' '] = 'Space'
    dictionary['-'] = 'Dash'
    file = open('alphabet.txt', 'r')
    for line in file.readlines():
        dictionary[line[:1]] = (line[2:]).strip()

    return dictionary

# This function categorizes each line of data to a certain ID type based on the number of character on that line
def categorize_identifier(identifier):
    id_length = len(identifier)
    if 5 <= id_length <= 8:
        return "TAG"
    elif id_length == 17:
        return "VIN"
    elif id_length == 10:
        return "BOAT"
    else:
        return "INVALID"

# This function transcribes each letter in the NATO alphabet and assigns the word for that letter to each character in the file.
def get_spelling(dictionary, identifier):
    chars = list(identifier)
    spelling = ""

    for char in chars:
        spelling += ((dictionary[char]) + " ")

    spelling = spelling[:-1]
    return spelling

# This basically just puts all the functions together and tells the program to print the type of ID it is and then the NATO alphabet translation
def main():
    num_processed = 0
    invalid = 0
    dictionary = get_dictionary()
    file = open("identifiers.txt", 'r')
    for line in file.readlines():
        identifier = line.strip().upper()
        id_type = categorize_identifier(identifier)
        if id_type != "INVALID":
            num_processed += 1
            print(f"{id_type} : {identifier}")
            print(get_spelling(dictionary, identifier))
        else:
            invalid += 1
            print(f"{id_type} : {identifier}")

        print()
    print(f"Number of Identifiers Processed: {num_processed}")
    print(f"Number of invalid identifiers: {invalid}")


if __name__ == '__main__':
    main()
