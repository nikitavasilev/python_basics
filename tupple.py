my_list = [0, 1, 45, 3]

print(my_list[2])

my_list.append(56) 

print(my_list) # expect [0, 1, 45, 3, 56]

my_list.insert(0, 'z')

print(my_list)

another_list = ['one', 'two', 'three']

my_list.extend(another_list) # same as my_list += another_list

print(my_list)