

# Map function 

def square(num: int):
    return num ** 2

lst = [1, 2, 3, 4, 5]

new_list = map(square, lst)

print(type(new_list))

print(list(new_list))