lists=[[1,2,3,[4,5]],[6,7,[8,9]],[10,[11,12,13]]]
def print_nested_list(lists):
    for i in lists:
        if type(i)==list:
            print_nested_list(i)
        else:
            print(i,end=" ")
print_nested_list(lists)
