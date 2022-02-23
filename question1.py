
# A. Write a function that asks the user her/his age, makes sure it is actually a number and if
# that’s the case prints it on the screen. If it is not a number, just print “not a number”. Make sure
# that you write a function to perform the above. (12.5 marks)

def get_age():
    # get age as input
    age = input("Please enter your age(in years) ")

    # check age is number or not if true then number else not a number
    if(age.isnumeric()):
        print("Your age is", age, "in years")
    else:
        print("not a number")




# B. Write a function which receives a list containing numbers as parameter. Your function
# should return True if all the elements in the list are in order, and False otherwise. Make sure
# that you write a function to perform the above. (12.5 marks)


def list_sorted(alist):
    check_sort = 0
    i = 1
    while i < len(alist):
        # Check list is sorted or not and if not then update check_sort flag to 1
        if (alist[i] < alist[i - 1]):
            check_sort = 1
        i += 1

    # check check_sort flag if 0 then sorted else not
    if (not check_sort):
        print("Yes, List is sorted.")
    else:
        print("No, List is not sorted.")

alist=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9]


section = input("Run section A or B ")
if(section.upper() == 'A'):
    # Function for get age
    get_age()
else:
    # Pass list contain number as parameter and check that list is sorted or not
    list_sorted(alist)