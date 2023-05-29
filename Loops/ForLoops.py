#  It is used for iterating over a string, lists, sets, dicts, range, tuples
# n = 10
# (i = 1 ; i<= n; i++)
# (i = 10 ; i>= n; i--)

# for loop


# i = [2,4,6,1];
# for element in i:
#    if element % 2 == 0:
#        print("It is an even number")
#    else:
#        print("It is an odd number")


# Check if the lists contain an even number

def assume(i):
    for element in i:
        if element % 2 == 0:
            print("List contains even number")
            break
    else:
        print("List does not contain even number")
    print("list 1")
    assume([2, 4, 6, 1])
    print("List 2")
    assume([1, 1, 1, 1])
