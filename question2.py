# Question 2:
# Say that I have a dictionary “d” that I need to post-process:
# d={'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'1', 'f':'1’, ‘g’:’2’, ‘h’:’3’, ‘i’:’1’}
# The above dictionary maps letters to numbers (frequencies). My main task is to develop a
# function that inverts the dictionary, i.e. maps numbers to letters.
# Use a for loop to perform this. (25 marks)

def change_map_numbertoletter(dictionary):
    new_dictionary = dict()
    new_value = []
    # for loop traverse dictionary
    for index, value in dictionary.items():
        # check already exist value as index in new dictionary if exist then append in that else add new index
        if value in new_dictionary:
            # check new_dictionary[value] is string or not if string then append as list
            # else append in new_dictionary[value]
            if type(new_dictionary[value]) == str:
                new_value.append(new_dictionary[value])
                new_value.append(index)
                new_dictionary[value] = new_value
            else:
                new_dictionary[value].append(index)
            new_value = []
        else:
            new_dictionary[value] = index
    print(new_dictionary)

dictionary = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '1', 'f': '1', 'g': '2', 'h': '3', 'i': '1'}
# Pass dictionary for change mapping
change_map_numbertoletter(dictionary)