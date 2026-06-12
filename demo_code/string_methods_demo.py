def main():
    my_name = "anish"
    
    #capitalize a string
    print(f"My name capitalized: {my_name.capitalize()}")

    # make a string uppercase
    print(f"My name uppercased: {my_name.upper()}")

    # make a string lowercase
    last_name = "SUDDALA"
    print(f"My full name lowercased: {my_name.lower()} {last_name.lower()}")

    # compare two strings
    my_name_title_case = "Anish"
    if(my_name.lower() == my_name_title_case.lower()):
        print("The strings are equal")
    else:
        print("The strings are not equal")

    print("\nUsing the Startswith() Methoiod\n--------------")
    #determine if a string starts with a set of characters
    print(f"{my_name} starts with a A or a: {my_name.startswith("A") or my_name.startswith("a")}")

    if((not my_name.startswith("Anish")) and (not my_name.startswith("anish"))):
        print(f"You spelled {my_name} incorrectly")
    else:
        print(f"You spelt {my_name} correctly")
    
    print("\nUsing the Endswith() Method\n---------------")
    print(f"{my_name} ends with 'ish': {my_name.endswith('ish')}")

    print("\nUsing the Find() Method\n----------------" )
    # find the i in anish
    search_letter = "ish"
    index_of_substring = my_name.find(search_letter)
    if index_of_substring !=-1:
        print(f"The '{search_letter}' is at index {my_name.find(search_letter)} in {my_name}")
    else:
        print(f"The '{search_letter}' is not in {my_name} ")
    
    print("\nLooping through a string\n------------------")
    for letter in my_name:
        print(letter)
    print(f"My name as {len(my_name)} letters")
    # print the letters in a string along with the index positions
    for letter_index in range(0,len(my_name)):
        print(f"Letter {letter_index+1}: {my_name[letter_index]}")
    
    print("\nSearch a string\n-----------")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    #Expected output: 3
    start_index = 0
    number_of_dogs = 0
    search_word = "dog"
    while (True):
        # start at the beginning of the string
        #search for the occurence of the word "dog" starting at index 0
        dog_index = sentence.find(search_word, start_index)
        # continue searching the string form the next ubdex after the dog we just found
        #update the starting index by 1
        if dog_index == -1:
            break
        else:
            # if we find dog, add 1 to sonme variable we use to keep track of the number of dogs we find
            number_of_dogs += 1
            #update the starting index by 1
            start_index = dog_index + 1
        # search until we don't find anymore dogs: when find() returns -1
    print(f"There are {number_of_dogs} {search_word}(s) in the sentence. ")




main()
