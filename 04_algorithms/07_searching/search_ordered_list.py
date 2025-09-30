
def search_ordered(ordered_list, term):
    ordered_list_size = len(ordered_list)
    for i in range(ordered_list_size):
        if term == ordered_list[i]:
            return i
        elif ordered_list[i] > term:
            return None

    return None



list1 = [2, 3, 4, 6, 7]

search_term = 6
index_position1 = search_ordered(list1, search_term)

if index_position1 is None:
    print(f"{search_term} not found")
else:
    print(f"{search_term} found at position {index_position1}")


list2 = ['book','data','packt', 'structure']

search_term2 = 'structure'
index_position2 = search_ordered(list2, search_term2)


if index_position2 is None:
    print(f"{search_term2} not found")
else:
    print(f"{search_term2} found at position {index_position2}")