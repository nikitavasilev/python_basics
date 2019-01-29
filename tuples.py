my_list = [0, 1, 45, 3]
print(my_list[2])

my_list.append(56) 
print(my_list) # expect [0, 1, 45, 3, 56]

my_list.insert(0, 'z')
print(my_list)

another_list = ['one', 'two', 'three']
my_list.extend(another_list) # same as my_list += another_list
print(my_list)

del my_list[0] # del method works with the index, it can also delete the whole variable
print(my_list)

my_list.remove(0) # remove method works with the element itself
print(my_list)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i = 0
while i < len(alphabet):
    print(alphabet[i])
    i += 1

for elt in alphabet: # same as the while loop before, but much shorter
    print(elt)

for elt in enumerate(alphabet): # once a tuple is created, you cannot change it
    print(elt)

for i, elt in enumerate(alphabet):
    print('In index {}, you can find {}.'.format(i, elt))

empty_tuple = () # list = [], and tuple = ()

not_empty_tuple = (1,) # even with only one element, don't forget the coma, it's mandatory when you create a tuple

def decompose(integer, divided_by):
    entire_part = integer // divided_by
    rest = integer % divided_by
    return entire_part, rest

print(decompose(20, 3)) # we can return more than one value, in tuples!