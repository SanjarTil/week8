def chop(lst):
    if len(lst) >= 2:
        del lst[0]
        del lst[-1]
    else:
        lst.clear()
def middle(lst):
    return lst[1:-1]
my_list = [3, 4, 5, 6, 7]
print("Original List:", my_list)
chop(my_list)
print("After chop:", my_list)
new_list = middle(my_list)
print("Middle elements List:", new_list)
