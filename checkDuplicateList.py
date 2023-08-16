import random

list_set = set()
duplicate_list = []
all_lists = []

for _ in range(10):
    random_list = [random.randint(1, 2) for _ in range(5)]
    all_lists.append(random_list)

for sub_list in all_lists:

    # Convert the list to a tuple
    tuple_list = tuple(sub_list)

    if tuple_list in list_set:
        duplicate_list.append(tuple_list) #duplicate list added 

    #add tuple to the set
    list_set.add(tuple_list)

if duplicate_list:
    print(f"{list(duplicate_list)} This Duplicate lists found more than 1 time")
else:
    print("No duplicate lists found.")