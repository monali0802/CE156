# Question 3:
# Write a function that receives a string as parameter and then returns a dictionary mapping
# frequency to letters.
# Eg. If the string is ‘hello’, the dictionary should be:
# {1:['h', 'e', 'o'], 2:['l'],} (25 marks)


def strListToFreqDict(str):
    # count frequency of character in string
    strfreq = [str.count(p) for p in str]
    # merge with str and strfreq and covert into list
    newlist = list(zip(strfreq, str))
    dictionary = dict()
    # list to dictionary
    for index, value in newlist:
        new_value = []
        if index in dictionary:
            if value not in dictionary[index]:
                dictionary[index].append(value)
        else:
            new_value.append(value)
            dictionary[index] = new_value
            
    print(dictionary)

str = "hello"
strListToFreqDict(str)