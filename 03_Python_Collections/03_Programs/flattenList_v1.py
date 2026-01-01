
nst_lst = [[1, 2, 3], [[[[1, 2, 3, 4, 5]]]], []]

flat_lst = []

def flattenlist(nst_lst):
    if len(nst_lst) > 0:
        for item in nst_lst:
            if isinstance(item, list):
                flattenlist(item)
            else:
                flat_lst.append(item)
        

     

flattenlist(nst_lst)

print("flatten list: ", flat_lst)

# print(len(nst_lst[1]))